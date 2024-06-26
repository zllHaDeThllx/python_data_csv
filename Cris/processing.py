import os
import pandas as pd
import matplotlib.pyplot as plt


def read_data(file: str):
    file = str(file)
    if not os.path.exists(file):
        print("El archivo proporcinado no se encuentra")
        return None
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None


def process_data(df):

    if df is None:
        print("DataFrame is None, cannot process data.")
        return None

    # Filtering wrong data and creating a copy to avoid SettingWithCopyWarning
    df_filtered = df[df["Hum - %"] != "--"].copy()

    # Correcting data types
    df_filtered["Date & Time"] = pd.to_datetime(
        df_filtered["Date & Time"], format="%m/%d/%y %H:%M"
    )
    numerics = [
        "Hum - %",
        "Temp - °C",
        "Inside Hum - %",
        "Temp - °C",
        "Inside Temp - °C",
    ]
    for item in numerics:
        df_filtered[item] = pd.to_numeric(df_filtered[item], errors="coerce")

    # Adding year and month columns
    df_filtered["year"] = pd.DatetimeIndex(df_filtered["Date & Time"]).year
    df_filtered["month"] = pd.DatetimeIndex(df_filtered["Date & Time"]).month

    df_filtered.drop(labels="Date & Time", axis=1, inplace=True)
    df_filtered.info()
    return df_filtered


def means_by_year(df):

    if df is None:
        print("DataFrame is None, cannot process data.")
        return None

    try:
        years = pd.unique(df["year"])
        by_year = df.groupby("year")
    except Exception as e:
        print(f"Error extracting years: {e}")
    numerics = [
        "Hum - %",
        "Temp - °C",
        "Inside Hum - %",
        "Temp - °C",
        "Inside Temp - °C",
    ]
    lista = []
    for year in years:
        df_year = by_year.get_group(year)
        year_mean = df_year.groupby("month")[numerics].mean()
        lista.append(year_mean)

    fig, ax = plt.subplots(2, 2, figsize=(15, 10))
    ax = ax.flatten()

    handles, labels = [], []  # Inicializa listas vacías para handles y etiquetas

    for i, df_year in enumerate(lista):
        for numeric in numerics:
            # Grafica cada variable por separado con una etiqueta que sea el nombre de la variable
            line = ax[i].plot(df_year.index, df_year[numeric], label=numeric)[
                0
            ]  # Corrección aquí
            if numeric not in labels:
                handles.append(line)
                labels.append(numeric)
        ax[i].set_title(f"Year: {years[i]}")
        ax[i].set_xlabel("Month")
        ax[i].set_ylabel("Value")

    # Utiliza las listas de handles y etiquetas para crear una leyenda única
    fig.legend(handles, labels, loc="upper right", bbox_to_anchor=(1.1, 1.05))
    plt.tight_layout()

    # Storing plot
    try:
        plt.savefig("files_general/Cristian/plots/means_by_month.png")
        print("Save")
    except:
        os.makedirs("files_general/Cristian/plots")

    if os.path.exists("files_genral/Cristian/plots"):
        plt.savefig("files_general/Cristian/plots/means_by_month.png")
        print("Save")


def stats_by_year(df, var: str):
    by_year = df.groupby("year")[var]
    print(by_year.describe())
    pass


def main():
    stop = False
    while not stop:
        print(
            """============================
1. Leer los datos
2. Depurar datos
3. Graficar las medias por mes de cada año
4. Terminar el programa
5. Estadísticas por año
"""
        )
        try:
            option = int(input("Option: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        match option:
            case 1:
                df = read_data(input("Ingrese el nombre del archivo: "))
            case 2:
                df_processed = process_data(df)
            case 3:
                means_by_year(df_processed)
            case 4:
                print("Program finished")
                stop = True
            case 5:
                options = {
                    1: "Hum - %",
                    2: "Temp - °C",
                    3: "Inside Hum - %",
                    4: "Temp - °C",
                    5: "Inside Temp - °C",
                }

                for key, item in options.items():
                    print(f"{key}: {item}")

                elegir = int(input("Elija la variable deseada: "))
                print(f"Estadisticas para {options[elegir]}")
                stats_by_year(df_processed, options[elegir])

            case _:
                print("Valor incorrecto")
    pass


if __name__ == "__main__":
    main()
