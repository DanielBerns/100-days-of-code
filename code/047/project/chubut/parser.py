# https://nanonets.com/blog/extract-text-from-pdf-file-using-python/

# importing required modules
from typing import Generator, List
from .doc import Doc


def log_decorator(original_function):
    def wrapper(*args, **kwargs):
        print(
            f"Calling {original_function.__name__} with args: {args}, kwargs: {kwargs}"
        )

        # Call the original function
        result = original_function(*args, **kwargs)

        # Log the return value
        print(f"{original_function.__name__} returned: {result}")

        # Return the result
        return result

    return wrapper


@log_decorator
def next_line(string: str) -> Generator[str, None, None]:
    left: int = 0
    for right, character in enumerate(string):
        if character == "\n":
            line = string[left:right]
            left = right + 1
            yield line


@log_decorator
def extract_prefix(target: Doc, string: str, prefix: str, key: str) -> bool:
    parts = string.split(prefix)
    if len(parts) == 2:
        ok = len(parts[0]) == 0
        if ok:
            target.add(key, parts[1])
        else:
            target.error = "extract_prefix - 1: len(parts[0]) != 0"
        return ok
    else:
        target.error = "extract_prefix - 2: len(parts) != 2"
        return False


@log_decorator
def split(target: Doc, string: str, divisor: str, keys: List[str]) -> bool:
    parts = string.split(divisor)
    if len(parts) == len(keys):
        for k, p in zip(keys, parts):
            target.add(k, p)
        return True
    else:
        target.error = "split - 1: len(parts) != len(keys)"
        return False


@log_decorator
def alpha(
    get_string: Generator[str, None, None], constants: Doc, variables: Doc
) -> bool:
    # INSTITUTO DE SEGURIDAD SOCIAL Y SEGUROS
    string = next(get_string)
    return string == "INSTITUTO DE SEGURIDAD SOCIAL Y SEGUROS"


@log_decorator
def bravo(
    get_string: Generator[str, None, None], constants: Doc, variables: Doc
) -> bool:
    # PROVINCIA DEL CHUBUT
    string = next(get_string)
    return string == "PROVINCIA DEL CHUBUT"


@log_decorator
def charlie(
    get_string: Generator[str, None, None], constants: Doc, variables: Doc
) -> bool:
    # Periodo: mes año
    string = next(get_string)
    return extract_prefix(constants, string, "Periodo: ", "periodo")


@log_decorator
def delta(
    get_string: Generator[str, None, None], constants: Doc, variables: Doc
) -> bool:
    # Apellido y Nombres: APELLIDO NOMBRE1 NOMBRE2
    string = next(get_string)
    return extract_prefix(
        constants, string, "Apellido y Nombres: ", "apellido_y_nombres"
    )


@log_decorator
def echo(
    get_string: Generator[str, None, None], constants: Doc, variables: Doc
) -> bool:
    # Ley: 1820/00Banco: B.CH.CA-COMODORO RIVADAVIA
    string = next(get_string)
    return split(constants, string, "Banco: ", ["ley", "banco"])


@log_decorator
def foxtrot(
    get_string: Generator[str, None, None], constants: Doc, variables: Doc
) -> bool:
    # Tipo y Nro. Doc.: D.N.I. DDDDDDDD
    string = next(get_string)
    return extract_prefix(constants, string, "Tipo y Nro. Doc.: ", "documento")


@log_decorator
def golf(
    get_string: Generator[str, None, None], constants: Doc, variables: Doc
) -> bool:
    # % Jub.: 82.00%Nro. Beneficio: DDDDDNro. Recibo: DDDD
    string = next(get_string)
    return split(constants, string, "Nro. ", ["jub", "beneficio", "recibo"])


@log_decorator
def hotel(
    get_string: Generator[str, None, None], constants: Doc, variables: Doc
) -> bool:
    # Categoria: 020-GABINETISTA CON 20 HS. SEM
    string = next(get_string)
    return extract_prefix(constants, string, "Categoria: ", "categoria")


@log_decorator
def india(
    get_string: Generator[str, None, None], constants: Doc, variables: Doc
) -> bool:
    string = next(get_string)
    return string == "CODIGO CONCEPTO UN. CALC. HABERES DESCUENTOS"


@log_decorator
def variable(string: str, divisor: str, target: Doc) -> bool:
    parts = string.split(divisor)
    if len(parts) == 2:
        target.add(parts[0], parts[1])
        return True
    else:
        target.error = "variable - 1: len(parts) != 2"
        return False


@log_decorator
def juliet(
    get_string: Generator[str, None, None], constants: Doc, variables: Doc
) -> bool:
    # TOTALES Hab.: Desc.: Sal. Fam. :
    # Neto Efectivo:$ DDD,DDD.23 $ DD,DDD.DD $ D,DDD.DD
    string = next(get_string)
    running = len(string)
    if not running:
        variables.error = "juliet - 1: unexpected string"
        return False
    while string != "TOTALES Hab.: Desc.: Sal. Fam. :":
        string = next(get_string) if variable(string, "$", variables) else ""
        running = len(string) > 0
        if not running:
            variables.error = "juliet - 2: unexpected input"
            return False
    if not running:
        variables.error = "juliet - 3: not running"
        return False
    prefix = "Neto Efectivo:"
    string = next(get_string)
    parts = string.split(prefix)
    running = len(parts) == 2
    if not running:
        variables.error = "juliet - 4: len(parts) != 2"
        return False
    suffix = parts[1]
    divisor = "$"
    parts = suffix.split(divisor)
    running = len(parts) == 4
    if not running:
        variables.error = "juliet - 5: len(parts) != 4"
        return False
    variables.add("haberes", parts[1])
    variables.add("descuentos", parts[2])
    variables.add("salario_familiar", parts[3])
    return True


@log_decorator
def kilo(
    get_string: Generator[str, None, None], constants: Doc, variables: Doc
) -> bool:
    # $ 514,833.33
    string = next(get_string)
    return extract_prefix(variables, string, "$", "neto")


@log_decorator
def parse(content: Doc, constants: Doc, variables: Doc) -> bool:
    tasks = [
        alpha,
        bravo,
        charlie,
        delta,
        echo,
        foxtrot,
        golf,
        hotel,
        india,
        juliet,
        kilo,
    ]
    running = len(tasks) > 0
    get_string = content.values()
    for t in tasks:
        running = t(get_string, constants, variables) if running else False
    return running
