# Proyecto: Sistema de Registro de Estudiantes

estudiantes = []
calificaciones = []
notas_finales = []

for i in range(3):
    print(f"\nRegistro del estudiante {i + 1}")

    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")

    try:
        parcial1 = float(input("Nota del Parcial 1: "))
    except ValueError:
        parcial1 = 0
        print("Entrada inválida. Se asignó 0.")

    try:
        parcial2 = float(input("Nota del Parcial 2: "))
    except ValueError:
        parcial2 = 0
        print("Entrada inválida. Se asignó 0.")

    nota_final = (parcial1 + parcial2) / 2

    estudiantes.append(nombre + " " + apellido)
    calificaciones.append([parcial1, parcial2])
    notas_finales.append(nota_final)

print("\n===== REPORTE ACADÉMICO =====")

for i in range(3):
    nota = notas_finales[i]

    if nota < 60:
        estado = "Reprobado"
    elif nota > 95:
        estado = "Sobresaliente"
    else:
        estado = "Aprobado"

    print(f"\nEstudiante: {estudiantes[i]}")
    print(f"Parcial 1: {calificaciones[i][0]}")
    print(f"Parcial 2: {calificaciones[i][1]}")
    print(f"Nota final: {nota:.2f}")
    print(f"Estado académico: {estado}")