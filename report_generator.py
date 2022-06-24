from markdownmaker.document import Document
from markdownmaker.markdownmaker import *

doc = Document()

doc.add(Header("Report Data Quality de Luchito"))
with HeaderSubLevel(doc):
    doc.add(Header("Ventas DataSet"))
    doc.add(Image(url="out/Venta_data_quality.png", alt_text="Venta"))

    with HeaderSubLevel(doc):
        doc.add(Header("Valores Nulos:"))


print(doc.write())
