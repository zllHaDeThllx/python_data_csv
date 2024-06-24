import pandas as pd

# Lectura de cada uno de los Datos
Datos_2019 = pd.read_csv(".\\Datos\\Datos_2019.csv")
Datos_2020 = pd.read_csv(".\\Datos\\Datos_2020.csv")
Datos_2021 = pd.read_csv(".\\Datos\\Datos_2021.csv")
Datos_2022 = pd.read_csv(".\\Datos\\Datos_2022.csv")
# Contar la cantidad de filas de cada dato segun su año
lines_year = []
for i in range(4):
    with open(f".\\Datos\\Datos_20{19+i}.csv") as myfile:
        total_lines = sum(1 for line in myfile)
        lines_year.append(total_lines)

# La suma de las lineas de cada archivo
All_lines = sum(lines_year)
# Eliminar las filas donde falten datos
cont = 0
years_line_2019 = []
years_line_2020 = []
years_line_2021 = []
years_line_2022 = []
for i in range(All_lines):
    cont += 1
    carga = round(((cont / All_lines) * 100), 2)  # Mostrar el avance
    print(f"Cangando: {carga}%")
    # Verifica si hay filas vacias
    if i < lines_year[0] - 2:
        if (
            Datos_2019.iloc[i, 1] != "--"
            and Datos_2019.iloc[i, 2] != "--"
            and Datos_2019.iloc[i, 3] != "--"
            and Datos_2019.iloc[i, 4] != "--"
        ):
            years_line_2019.append(
                Datos_2019.iloc[i]
            )  # Separa los datos con la infandmación completa
    if i < lines_year[1] - 2:
        if (
            Datos_2020.iloc[i, 1] != "--"
            and Datos_2020.iloc[i, 2] != "--"
            and Datos_2020.iloc[i, 3] != "--" 
            and Datos_2020.iloc[i, 4] != "--"
        ):
            years_line_2020.append(
                Datos_2020.iloc[i]
            )  # Separa los datos con la infandmación completa
    if i < lines_year[2] - 2:
        if (
            Datos_2021.iloc[i, 1] != "--"
            and Datos_2021.iloc[i, 2] != "--"
            and Datos_2021.iloc[i, 3] != "--"
            and Datos_2021.iloc[i, 4] != "--"
        ):
            years_line_2021.append(
                Datos_2021.iloc[i]
            )  # Separa los datos con la infandmación completa
    if i < lines_year[3] - 2:
        if (
            Datos_2022.iloc[i, 1] != "--"
            and Datos_2022.iloc[i, 2] != "--"
            and Datos_2022.iloc[i, 3] != "--"
            and Datos_2022.iloc[i, 4] != "--"
        ):
            years_line_2022.append(
                Datos_2022.iloc[i]
            )  # Separa los datos con la infandmación completa

# Guarda los datos ya depurados
df_2019 = pd.DataFrame(years_line_2019)
df_2019.to_csv(".\\Datos\\Datos_2019.csv", index=False)

df_2020 = pd.DataFrame(years_line_2020)
df_2020.to_csv(".\\Datos\\Datos_2020.csv", index=False)

df_2021 = pd.DataFrame(years_line_2021)
df_2021.to_csv(".\\Datos\\Datos_2021.csv", index=False)

df_2022 = pd.DataFrame(years_line_2022)
df_2022.to_csv(".\\Datos\\Datos_2022.csv", index=False)
