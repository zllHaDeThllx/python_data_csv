import pandas as pd

# Piede el nombre del archivo para analizar
x = str(input("Ingrese el nombre del archivo: "))
# Lectura de los datos
datos = pd.read_csv(f"{x}.csv")
datos.info()

# Contar el numero de lineas o filas que hay en el archivo
with open("datos.csv") as myfile:
    total_lines = sum(1 for line in myfile)
    print(total_lines) 

### Iterar en cada una de las filas del archivo ###
cont = 0
years_line_2019 = []
years_line_2020 = []
years_line_2021 = []
years_line_2022 = []
for i in range(total_lines - 2):
    # Iterar en cada fila del archivo
    time_line = datos.iloc[i, 0]
    datos_line = datos.iloc[i]
    # Crear un control visual de carga
    cont = cont + 1
    loader = (cont / total_lines) * 100
    print(f"Cargando: {round(loader,2)}%")
    # Dividir los datos por año
    if time_line[5:7] == "19" or time_line[6:8] == "19":  # 2019
        years_line_2019.append((datos_line))
    elif (
        time_line[4:6] == "20" or time_line[5:7] == "20" or time_line[6:8] == "20"
    ):  # 2020
        years_line_2020.append((datos_line))
    elif (
        time_line[4:6] == "21" or time_line[5:7] == "21" or time_line[6:8] == "21"
    ):  # 2021
        years_line_2021.append((datos_line))
    elif (
        time_line[4:6] == "22" or time_line[5:7] == "22" or time_line[6:8] == "22"
    ):  # 2022
        years_line_2022.append((datos_line))

# Guaradar los datos por años
df_2019 = pd.DataFrame(years_line_2019)
df_2019.to_csv(".\\Datos\\Datos_2019.csv", index=False)

df_2020 = pd.DataFrame(years_line_2020)
df_2020.to_csv(".\\Datos\\Datos_2020.csv", index=False)

df_2021 = pd.DataFrame(years_line_2021)
df_2021.to_csv(".\\Datos\\Datos_2021.csv", index=False)

df_2022 = pd.DataFrame(years_line_2022)
df_2022.to_csv(".\\Datos\\Datos_2022.csv", index=False)
