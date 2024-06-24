print(
    "Este programa separará, depurará, ordenará en tablas y graficara la infomación porporcionada por la estación meteorológica"
)    
print(  
    "Menú: \n 1) Separar los datos por años. \n 2) Depurar los datos. \n 3) Promediar los datos por mes del año elegido, y graficar. \n 4) Salir."
)
x = str(input(" Elija una opción: "))

# Evita errores si los que ingresa el usuario no es valido
while x != "1" or x != "2" or x != "3" or x != "4":
    if x == "1" or x == "2" or x == "3" or x == "4":
        break
    x = str(input(" Elija una opción válida: "))

# Dependiendo de la opción importa el codigo correspondiente
if x == "1":
    try:  # Evita el error "FileNotFoundError" si no encuentra el archivo
        import A_Main
    except FileNotFoundError:
        print(
            "\nNo se encuentra el archivo o la carpeta (Datos), asegúrese de pasarlo a esta carpeta o directorio.\n"
        )
elif x == "2":
    try:  # Evita el error "FileNotFoundError" si no encuentra el archivo
        import B_Debug
    except FileNotFoundError:
        print(
            "\nArchivos no encontrados o no existe la carpeta (Datos), recuerde que para la ejecución de este codigo usted necesita tener los archivos ya separados por años."
            "\nSi nos los tiene aseguresé de ejecutar la opción 1.\n"
        )
elif x == "3":
    try:  # Evita el error "FileNotFoundError" si no encuentra el archivo
        import C_Prom
    except FileNotFoundError:
        print(
            "\nArchivos no encontrados o puede que la carpeta (Tablas) aún no esté creada, recuerde que para la ejecución de este codigo usted necesita tener los archivos ya separados por años."
            "\nSi nos los tiene aseguresé de ejecutar la opción 1, y si le marca error asegurese de depuerar los datos con la opción 2.\n"
        )
elif x == "4":
    print("Gracias por elegirnos")
