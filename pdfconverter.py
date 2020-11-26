# HTML to PDF converter
# 26-11-2020
# https://stackoverflow.com/questions/23359083/how-to-convert-webpage-into-pdf-by-using-python
# https://pypi.org/project/pdfkit/

import pdfkit

url = input("Welche URL soll in ein PDF verwandelt werden?: ")
try:
    pdfkit.from_url(url, "out.pdf")
    print("Das PDF wurde erstellt: out.pdf")
except:
    print("Ein Fehler ist aufgetreten.")
