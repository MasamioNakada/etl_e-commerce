import csv
from operator import ge
import os



labels = ['Clientes.csv', 'Compra.csv', 'Gasto.csv', 'Localidades.csv', 'Proveedores.csv', 'Sucursales.csv', 'Venta.csv']

def get_delimiter(path, bytes=4096):
    sniffer = csv.Sniffer()
    data = open(path,'r').read(bytes)
    delimiter = sniffer.sniff(data).delimiter
    print(delimiter)

for names in labels:
    print(get_delimiter(os.path.join('in',names)))



    