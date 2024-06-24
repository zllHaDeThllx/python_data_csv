import pandas as pd
from pylab import *
# Lectura de cada uno de los Datos
Year = str(input("Ingrese el año el cual desea ver los promedios: "))

# Evita errores si los que ingresa el usuario no es valido
while Year != "2019" or Year != "2020" or Year != "2021" or Year != "2022":
    if Year == "2019" or Year == "2020" or Year == "2021" or Year == "2022":
        break
    Year = str(input("Ingrese el año el cual desea ver los promedios: "))


Datos_Years = pd.read_csv(f".\\Datos\\Datos_{Year}.csv")
with open(f".\\Datos\\Datos_{Year}.csv") as myfile:
    total_lines = sum(1 for line in myfile)


def Prom_Inside_Temp(Mes):
    lines_mes = Mes.count(axis=0)  # Cuenta las lineas que hay en un DataFrame
    lines_mes = lines_mes[1:2]
    x = Mes[Mes.columns[1]]  # Selecciona una columna completa de un DataFrame
    p = round(sum(x) / lines_mes, 2)
    return p  # Retorna el promedio


def Prom_Inside_Hum(Mes):
    lines_mes = Mes.count(axis=0)  # Cuenta las lineas que hay en un DataFrame
    lines_mes = lines_mes[2:3]
    x = Mes[Mes.columns[2]]  # Selecciona una columna completa de un DataFrame
    p = round(sum(x) / lines_mes, 2)
    return p


def Prom_External_Temp(Mes):
    lines_mes = Mes.count(axis=0)  # Cuenta las lineas que hay en un DataFrame
    lines_mes = lines_mes[3:4]
    x = Mes[Mes.columns[3]]  # Selecciona una columna completa de un DataFrame
    p = round(sum(x) / lines_mes, 2)
    return p


def Prom_External_Hum(Mes):
    lines_mes = Mes.count(axis=0)  # Cuenta las lineas que hay en un DataFrame
    lines_mes = lines_mes[4:5]
    x = Mes[Mes.columns[4]]  # Selecciona una columna completa de un DataFrame
    p = round(sum(x) / lines_mes, 2)
    return p


Enero = []
Febrero = []
Marzo = []
Abril = []
Mayo = []
Junio = []
Julio = []
Agosto = []
Septiembre = []
Octubre = []
Noviembre = []
Diciembre = []

for i in range(total_lines - 1):  # Separa los datos por meses
    x = Datos_Years.iloc[i, 0]
    Datos = Datos_Years.iloc[i]
    if x[:1] == "1" and x[:2] != "10" and x[:2] != "11" and x[:2] != "12":
        Enero.append(Datos)
    elif x[:1] == "2":
        Febrero.append(Datos)
    elif x[:1] == "3":
        Marzo.append(Datos)
    elif x[:1] == "4":
        Abril.append(Datos)
    elif x[:1] == "5":
        Mayo.append(Datos)
    elif x[:1] == "6":
        Junio.append(Datos)
    elif x[:1] == "7":
        Julio.append(Datos)
    elif x[:1] == "8":
        Agosto.append(Datos)
    elif x[:1] == "9":
        Septiembre.append(Datos)
    elif x[:2] == "10":
        Octubre.append(Datos)
    elif x[:2] == "11":
        Noviembre.append(Datos)
    elif x[:2] == "12":
        Diciembre.append(Datos)

""" Se establecen las variables de esta manera para crear una 
    nueva lista de manera resumida, pero con los mismos valores
"""
x0 = Enero = pd.DataFrame(Enero)
x1 = Febrero = pd.DataFrame(Febrero)
x2 = Marzo = pd.DataFrame(Marzo)
x3 = Abril = pd.DataFrame(Abril)
x4 = Mayo = pd.DataFrame(Mayo)
x5 = Junio = pd.DataFrame(Junio)
x6 = Julio = pd.DataFrame(Julio)
x7 = Agosto = pd.DataFrame(Agosto)
x8 = Septiembre = pd.DataFrame(Septiembre)
x9 = Octubre = pd.DataFrame(Octubre)
x10 = Noviembre = pd.DataFrame(Noviembre)
x11 = Diciembre = pd.DataFrame(Diciembre)

lista = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]
lista_prom_1 = []
lista_prom_2 = []
lista_prom_3 = []
lista_prom_4 = []
for i in range(4):  # LLama a las funciones para sacar los promedios de cada mes
    if i == 0:
        for j in range(12):
            # Calcula el promedio y lo asigna a el mes correspondiente
            x = Prom_Inside_Temp(lista[j])
            lista_prom_1.append(x)
    elif i == 1:
        for j in range(12):
            x = Prom_Inside_Hum(lista[j])
            lista_prom_2.append(x)
    elif i == 2:
        for j in range(12):
            x = Prom_External_Temp(lista[j])
            lista_prom_3.append(x)
    elif i == 3:
        for j in range(12):
            x = Prom_External_Hum(lista[j])
            lista_prom_4.append(x)

lista_prom_1 = pd.DataFrame(lista_prom_1)
lista_prom_2 = pd.DataFrame(lista_prom_2)
lista_prom_3 = pd.DataFrame(lista_prom_3)
lista_prom_4 = pd.DataFrame(lista_prom_4)

datos = {
    "MESES": [
        "ENERO",
        "FEBRERO",
        "MARZO",
        "ABRIL",
        "MAYO",
        "JUNIO",
        "JULIO",
        "AGOSTO",
        "SEPTIEMBRE",
        "OCTUBRE",
        "NOVIEMBRE",
        "DICIEMBRE",
    ],
    "TEMPERATURA INTERNA °C": [
        lista_prom_1.iloc[0, 0],
        lista_prom_1.iloc[1, 0],
        lista_prom_1.iloc[2, 0],
        lista_prom_1.iloc[3, 0],
        lista_prom_1.iloc[4, 0],
        lista_prom_1.iloc[5, 0],
        lista_prom_1.iloc[6, 0],
        lista_prom_1.iloc[6, 0],
        lista_prom_1.iloc[8, 0],
        lista_prom_1.iloc[9, 0],
        lista_prom_1.iloc[10, 0],
        lista_prom_1.iloc[11, 0],
    ],
    "HUMEDAD INTERNA %": [
        lista_prom_2.iloc[0, 0],
        lista_prom_2.iloc[1, 0],
        lista_prom_2.iloc[2, 0],
        lista_prom_2.iloc[3, 0],
        lista_prom_2.iloc[4, 0],
        lista_prom_2.iloc[5, 0],
        lista_prom_2.iloc[6, 0],
        lista_prom_2.iloc[6, 0],
        lista_prom_2.iloc[8, 0],
        lista_prom_2.iloc[9, 0],
        lista_prom_2.iloc[10, 0],
        lista_prom_2.iloc[11, 0],
    ],
    "TEMPERATURA EXTERNA °C": [
        lista_prom_3.iloc[0, 0],
        lista_prom_3.iloc[1, 0],
        lista_prom_3.iloc[2, 0],
        lista_prom_3.iloc[3, 0],
        lista_prom_3.iloc[4, 0],
        lista_prom_3.iloc[5, 0],
        lista_prom_3.iloc[6, 0],
        lista_prom_3.iloc[6, 0],
        lista_prom_3.iloc[8, 0],
        lista_prom_3.iloc[9, 0],
        lista_prom_3.iloc[10, 0],
        lista_prom_3.iloc[11, 0],
    ],
    "HUMEDAD EXTERNA %": [
        lista_prom_4.iloc[0, 0],
        lista_prom_4.iloc[1, 0],
        lista_prom_4.iloc[2, 0],
        lista_prom_4.iloc[3, 0],
        lista_prom_4.iloc[4, 0],
        lista_prom_4.iloc[5, 0],
        lista_prom_4.iloc[6, 0],
        lista_prom_4.iloc[6, 0],
        lista_prom_4.iloc[8, 0],
        lista_prom_4.iloc[9, 0],
        lista_prom_4.iloc[10, 0],
        lista_prom_4.iloc[11, 0],
    ],
}
df = pd.DataFrame(datos)
print(df)
save_or_not = str(
    input(
        "Para elegir una opción precione el numero que acompaña a dicha opción \n1) Guardar la tabla. \n2) Salir. \n¿Que desea hacer?: "
    )
)

# Evita errores si los que ingresa el usuario no es valido
while save_or_not != "1" or save_or_not != "2":
    if save_or_not == "1" or save_or_not == "2":
        break
    save_or_not = str(
        input("\n1) Guardar la tabla. \n2) Salir.  \n ¿Que desea hacer?: ")
    )

# Guarda las tablas
if save_or_not == "1":
    k = str(
        input("Guardar en formato: \n1) Excel. \n2) Csv \n¿Que desea hacer?: ")
    )  # Le da formato

    # Evita errores si los que ingresa el usuario no es valido
    while k != "1" or k != "2":
        if k == "1" or k == "2":
            break
        k = str(input("Guardar en formato: \n1) Excel. \n2) Csv \n¿Que desea hacer?: "))
    if k == "1":
        df.to_excel(f".\\Tablas\\Datos_{Year}.xlsx", index=False)  # Excel
        print("Gracias por elegir este sistema")
    elif k == "2":
        df.to_csv(f".\\Tablas\\Datos_{Year}.csv", index=False)  # Csv
        print("Gracias por elegir este sistema")
    elif save_or_not == "2":
        print("Gracias por elegir este sistema")

# Graficar tablas
df.plot()
show()
# """
