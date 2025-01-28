from typing import Generator, Dict, List, Tuple, Callable, DefaultDict, Any
from pathlib import Path
from collections import defaultdict
from .base import Base
from .doc import Doc
from .parser import parse, next_line, log_decorator
from PyPDF2 import PdfReader

# References
# https://nanonets.com/blog/extract-text-from-pdf-file-using-python/


class Pipeline(Base):
    def __init__(self, content: Doc, constants: Doc, variables: Doc) -> None:
        super().__init__()
        self._content: Doc = content
        self._constants: Doc = constants
        self._variables: Doc = variables

    def bind(self, action: Callable[[Doc, Doc, Doc], bool]) -> "Pipeline":
        ok = (
            action(self._content, self._constants, self._variables)
            if self.ok
            else False
        )
        if not ok:
            self.error = "Pipeline.bind - 1: not ok"
        return self


def create(resource: str) -> Pipeline:
    content = Doc()
    constants = Doc()
    variables = Doc()
    pipeline = Pipeline(content, constants, variables)
    try:
        reader = PdfReader(resource)
        number_of_pages = len(reader.pages)
        page = reader.pages[0]
        text = page.extract_text()
        for line_number, line in enumerate(next_line(text)):
            content.add(str(line_number), line)
    except Exception as error:
        pipeline.error = f"create - 1: {str(error):s}"
    return pipeline


def show(content: Doc, constants: Doc, variables: Doc) -> bool:
    content.show()
    constants.show()
    variables.show()
    return content.ok and constants.ok and variables.ok


# How to type hint the variable db?

DB = DefaultDict[Any, DefaultDict[Any, DefaultDict[Any, List[Any]]]]


def create_db() -> DB:
    db: DB = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    return db


def tf(value: str) -> int:
    return int(value.replace(".", "").replace(",", ""))


def update(amounts: DB, positions: DB, constants: Doc, variables: Doc) -> None:
    periodo = constants.get("periodo", "error")
    apellido_y_nombres = constants.get("apellido_y_nombres", "error")
    documento = constants.get("documento", "error")
    categoria = constants.get("categoria", "error")
    haberes = variables.get("haberes", "0.00")
    descuentos = variables.get("descuentos", "0.00")
    salario_familiar = variables.get("salario_familiar", "0.00")
    neto = variables.get("neto", "0.00")
    for codigo, valor in variables.items():
        amounts[periodo][documento][codigo].append(tf(valor))
    amounts[periodo][documento]["haberes"].append(tf(haberes))
    amounts[periodo][documento]["descuentos"].append(tf(descuentos))
    amounts[periodo][documento]["salario_familiar"].append(tf(salario_familiar))
    amounts[periodo][documento]["neto"].append(tf(neto))
    positions[periodo][documento][categoria].append(tf(neto))


def write(resource: Path, db: DB) -> None:
    with open(resource, "w") as target:
        periodos = sorted([pp for pp in db.keys()])        
        for pp in periodos:
            target.write(f"# Reporte período {pp:s}\n\n")
            target.write("## Reporte por documento y rubro\n\n")            
            totales = {}
            salarios = db[pp]
            target.write(f"| Documento       | Rubro     | Monto |\n")
            target.write(f"| :-------------- | :--------------------------------------------------- | ----------: |\n")
            for documento, persona in salarios.items():
                for codigo, valores in persona.items():
                    suma_valores = sum(valores)
                    totales[codigo] = totales.get(codigo, 0) + suma_valores
                    target.write(f"| {documento:<12s}| {codigo:<50s} | {suma_valores / 100:>10.2f} |\n")
            target.write("\n\n")
            target.write("## Reporte por rubro\n\n")                        
            target.write(f"| Rubro     | Monto |\n")
            target.write(f"| :--------------------------------------------------- | ----------: |\n")                    
            for codigo, valores in totales.items():
                target.write(f"| {codigo:<50s} | {valores / 100:>10.2f} |\n")
                

def collect(origins: List[str], results: str) -> None:
    amounts: DB = create_db()
    positions: DB = create_db()
    for a_resource in origins:
        print(a_resource)
        pipeline = create(a_resource).bind(parse).bind(show)
        update(amounts, positions, pipeline._constants, pipeline._variables)
    write(Path(results, "amounts.md"), amounts)
    write(Path(results, "positions.md"), positions)
