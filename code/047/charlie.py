# https://nanonets.com/blog/extract-text-from-pdf-file-using-python/

# importing required modules
from typing import Generator, Dict, List, Tuple, Callable
from PyPDF2 import PdfReader

import pdb


def log_decorator(original_function):
    def wrapper(*args, **kwargs):
        print(f"Calling {original_function.__name__} with args: {args}, kwargs: {kwargs}")

        # Call the original function
        result = original_function(*args, **kwargs)

        # Log the return value
        print(f"{original_function.__name__} returned: {result}")

        # Return the result
        return result
    return wrapper


def next_value(string: str) -> Generator[str, None, None]:
    left: int = 0
    for right, character in enumerate(string):
        if character == '\n':
            value = string[left:right]
            left = right + 1
            # print(value, '----', string[left:left+10], left, right)
            yield value            
                
class Doc:
    def __init__(self) -> None:
        self._attributes: Dict[str, str] = {}
        self._ok: bool = True
        self._error: str = ""
        
    @property
    def ok(self) -> bool:
        return self._ok
    
    @ok.setter
    def ok(self, value: bool) -> None:
        self._ok = value

    @property
    def error(self) -> str:
        return self._error
    
    @error.setter
    def error(self, value: str) -> None:
        if value:
            self._error = value
            self.ok = False
        
    def add(self, key: str, value: str) -> None:
        self._attributes[key] = value
    
    def get(self, key: str, value: str) -> str:
        return self._attributes.get(key, value)
    
    def show(self) -> None:
        for key, value in self._attributes.items():
            print(f"{key:s}: {value:s}")

    def values(self) -> Generator[str, None, None]:
        for value in self._attributes.values():
            yield value

def extract_prefix(target: Doc, string: str, prefix: str, key: str) -> bool:
    parts = string.split(prefix)
    if len(parts) == 2:
        target.add(key, parts[1])
        return True
    else:
        return False

def split(target: Doc, string: str, divisor: str, keys: List[str]) -> bool:
    parts = string.split(divisor)
    if len(parts) == len(keys):
        for k, p in zip(keys, parts):
            target.add(k, p)
        return True
    else:
        return False

def alpha(get_string: Generator[str, None, None], target: Doc) -> bool:
    # INSTITUTO DE SEGURIDAD SOCIAL Y SEGUROS
    string = next(get_string)
    return string == "INSTITUTO DE SEGURIDAD SOCIAL Y SEGUROS"
    
def bravo(get_string: Generator[str, None, None], target: Doc) -> bool:
    # PROVINCIA DEL CHUBUT
    string = next(get_string)    
    return string == "PROVINCIA DEL CHUBUT"

def charlie(get_string: Generator[str, None, None], target: Doc) -> bool:
    # Periodo: Diciembre 2023
    string = next(get_string)    
    return extract_prefix(target, string, "Periodo: ", "periodo")

def delta(get_string: Generator[str, None, None], target: Doc) -> bool:
    # Apellido y Nombres: WHITTY VIRGINIA CRISTINA
    string = next(get_string)    
    return extract_prefix(target, string, "Apellido y Nombres: ", "apellido_y_nombres")        
    
def echo(get_string: Generator[str, None, None], target: Doc) -> bool:
    # Ley: 1820/00Banco: B.CH.CA-COMODORO RIVADAVIA
    string = next(get_string)    
    return split(target, string, "Banco: ", ["ley", "banco"])        
    
def foxtrot(get_string: Generator[str, None, None], target: Doc) -> bool:
    # Tipo y Nro. Doc.: D.N.I. 17622771
    string = next(get_string)    
    return extract_prefix(target, string, "Tipo y Nro. Doc.: ", "documento")        

def golf(get_string: Generator[str, None, None], target: Doc) -> bool:
    # % Jub.: 82.00%Nro. Beneficio: 25874Nro. Recibo: 2179
    string = next(get_string)    
    return split(target, string, "Nro. ", ["jub", "beneficio", "recibo"])

def hotel(get_string: Generator[str, None, None], target: Doc) -> bool:
    # Categoria: 020-GABINETISTA CON 20 HS. SEM
    string = next(get_string)    
    return extract_prefix(target, string, "Categoria: ", "categoria")

def india(get_string: Generator[str, None, None], target: Doc) -> bool:
    string = next(get_string)    
    return string == "CODIGO CONCEPTO UN. CALC. HABERES DESCUENTOS"

def element(string: str, target: Doc, number: int) -> bool:
    return split(target, string, "$", [f"code-{number:d}", f"value-{number:d}"])

def juliet(get_string: Generator[str, None, None], target: Doc) -> bool:
    # 100Haber Mensual 30 $ 503,231.81
    # 1101Retroactivo Haberes por Movilidad $ 27,542.42
    # 9900Esposa/o $ 5,757.00
    # 140Adelanto a cuenta de Zona Remunerativa $ 1,800.00
    # 500Aporte personal SER.O.S. 4.25 $ 22,557.90
    # 533Seguro de Vida Obligatorio $ 500.00
    # 535Seguro colectivo familiar $ 390.00
    # 677Cobertura de Transplantes 1 $ 50.00
    # TOTALES Hab.: Desc.: Sal. Fam. :
    # Neto Efectivo:$ 538,331.23 $ 23,497.90 $ 5,757.00
    string = next(get_string)    
    running = len(string)
    if not running:
       return False
    number = 0
    while string != "TOTALES Hab.: Desc.: Sal. Fam. :":
        string = next(get_string) if element(string, target, number) else ""
        number += 1
        running = len(string)
        if not running:
            break
    if running:
        prefix = "Neto Efectivo:"
        string = next(get_string)    
        parts = string.split(prefix)
        content = parts[1] 
        divisor = "$"
        parts = content.split(divisor)
        target.add("haberes", parts[1])
        target.add("descuentos", parts[2])
        target.add("salario_familiar", parts[3])
        return True
    else:
        return False

def kilo(get_string: Generator[str, None, None], target: Doc) -> bool:
    # $ 514,833.33
    string = next(get_string)    
    return extract_prefix(target, string, "$", "neto")


def parse(origin: Doc, target: Doc) -> bool:
    tasks = [alpha, bravo, charlie, delta, echo, foxtrot, golf, hotel, india, juliet, kilo]
    running = True
    get_string = origin.values()
    for t in tasks:
        running = t(get_string, target) if running else False
    return running


resources: List[str] =  [
    "./recibo-octubre.pdf", 
    "./recibo-noviembre.pdf", 
    "./recibo-diciembre.pdf",
    "./3717649.pdf"
    ]

for a_resource in resources:
    # creating a pdf reader object
    reader = PdfReader(a_resource)
    
    # printing number of pages in pdf file
    print("number of pages:", len(reader.pages))
    
    # getting a specific page from the pdf file
    page = reader.pages[0]
    
    # extracting text from page
    text_pypdf = page.extract_text()
    origin = Doc()
    for number, value in enumerate(next_value(text_pypdf)):
        origin.add(str(number), value)

    target = Doc()
    result = parse(origin, target)
    target.show()
