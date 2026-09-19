#Sistema de Registro y Evaluación

print("=" * 60)
print("     SISTEMA DE REGISTRO Y EVALUACIÓN DE ESTUDIANTES")
print("=" * 60)

print("\n¡Bienvenido al sistema académico!")
print("Se registrarán 3 estudiantes.")
print("Las calificaciones deben estar entre 0 y 100.")
print("La nota mínima para aprobar es 60.")

print("\nESCALA DE APRENDIZAJE")
print("AI: Menor de 60 - Aprendizaje Inicial")
print("AF: 60 a 75 - Aprendizaje Fundamental")
print("AS: 76 a 89 - Aprendizaje Satisfactorio")
print("AA: 90 a 100 - Aprendizaje Avanzado")

print("=" * 60)

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


print("\n" + "=" * 60)
print("                    REPORTE ACADÉMICO")
print("=" * 60)

for i in range(3):

    nota = notas_finales[i]

    # Estado académico
    if nota < 60:
        estado = "REPROBADO"
    else:
        estado = "APROBADO"

    # Escala de aprendizaje
    if nota < 60:
        escala = "AI - Aprendizaje Inicial"
    elif nota <= 75:
        escala = "AF - Aprendizaje Fundamental"
    elif nota <= 89:
        escala = "AS - Aprendizaje Satisfactorio"
    else:
        escala = "AA - Aprendizaje Avanzado"

    print(f"\nEstudiante: {estudiantes[i]}")
    print(f"Parcial 1: {calificaciones[i][0]:.2f}")
    print(f"Parcial 2: {calificaciones[i][1]:.2f}")
    print(f"Nota final: {nota:.2f}")
    print(f"Estado: {estado}")
    print(f"Escala: {escala}")

print("\n" + "=" * 60)
print("              FIN DEL REPORTE ACADÉMICO")
print("=" * 60)