import os 

while True:
    os.system("cls" if os.name == "nt" else "clear")
    varreglo = []
    vsuma = 0
    vaprobados = 0
    vreprobados = 0

    print("="*30)
    print("PROCESAMIENTO DE NOTAS")
    print("="*30)

    # 1. Validar cantidad de estudiantes
    while True:
        entrada = input("Ingrese la cantidad de estudiantes: ")
        if entrada.isdigit() and int(entrada) > 0:
            vcantidad = int(entrada)
            break
        else:
            print("Error: Ingrese un número entero positivo.")

    # 2. Entrada de notas
    for i in range(vcantidad):
        while True:
            nota_input = input(f"Indique la nota del alumno {i+1}: ")
            if nota_input.isdigit(): # Validación simple para enteros
                nota = int(nota_input)
                varreglo.append(nota)
                vsuma += nota
                
                # Contar aprobados/reprobados (asumiendo base 10, aprueba con 4)
                if nota >= 4:
                    vaprobados += 1
                else:
                    vreprobados += 1
                break
            else:
                print("Nota no válida. Use números enteros.")

    # 3. Mostrar Resultados
    os.system("cls" if os.name == "nt" else "clear")
    print("\n MOSTRAR INDICADORES DE LA SECCIÓN")
    print("==================================")
    print(f"Las notas ingresadas fueron: {varreglo}")
    print(f"El promedio de la sección es: {round((vsuma/vcantidad), 2)}")
    print(f"Cantidad de alumnos aprobados: {vaprobados}")
    print(f"Cantidad de alumnos reprobados: {vreprobados}")
    print(f"La nota más alta fue: {max(varreglo)}")
    print(f"La nota más baja fue: {min(varreglo)}")
    print("=======================================")

    vresp = input("¿Desea procesar otra sección? [S]i / [N]o: ").upper()
    if vresp == 'N':
        break

print("Programa finalizado exitosamente. Pulse [ENTER]")
