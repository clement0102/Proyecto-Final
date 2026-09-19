#Sistema de Registro y Evaluación

print("=" * 50)
print("   SISTEMA DE REGISTRO Y EVALUACIÓN DE ESTUDIANTES")
print("=" * 50)
print("\n¡Bienvenido al sistema académico!")
print("Se registrarán 3 estudiantes.")
print("Las calificaciones deben estar entre 0 y 100.")
print("La nota mínima para aprobar es 60.")
print("=" * 50)

estudiantes = []
calificaciones = []
notas_finales = []

def ingresar_nota(parcial):
    try:
        nota = float(input(f"Ingrese la nota del {parcial}: "))

        if 0 <= nota <= 100:
            return nota
        else:
            print("Nota fuera de rango. Se asignó 0.")
            return 0

    except ValueError:
        print("Entrada inválida. Se asignó 0.")
        return 0


def calcular_nota_final(nota1, nota2):
    return (nota1 + nota2) / 2


for i in range(3):
    print(f"\n--- Registro del estudiante {i + 1} ---")

    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")

    parcial1 = ingresar_nota("Parcial 1")
    parcial2 = ingresar_nota("Parcial 2")

    nota_final = calcular_nota_final(parcial1, parcial2)

    estudiantes.append(nombre + " " + apellido)
    calificaciones.append([parcial1, parcial2])
    notas_finales.append(nota_final)


print("\n" + "=" * 50)
print("             REPORTE ACADÉMICO")
print("=" * 50)

for i in range(3):
    nota = notas_finales[i]

    if nota < 60:
        estado = "REPROBADO"
    elif nota > 95:
        estado = "SOBRESALIENTE"
    else:
        estado = "APROBADO"

    print(f"\nEstudiante: {estudiantes[i]}")
    print(f"Parcial 1: {calificaciones[i][0]}")
    print(f"Parcial 2: {calificaciones[i][1]}")
    print(f"Nota final: {nota:.2f}")
    print(f"Estado académico: {estado}")

print("\n" + "=" * 50)
print("        FIN DEL REPORTE ACADÉMICO")
print("=" * 50)