'''
Selectiva simple If
script que solicite al usuario su edad e indicarle si es mayor de edad
'''
edad=int(input("Ingrese su edad: "))
if edad>18:
    print(f"Usted es mayor de edad con {edad} años.")

'''
script en python que genere un numero aleatorio entre 1 y 10 y le pida al usuario adivinarlo y si adivina felicitarlo.
'''
#agrega el modulo random al programa
import random
secreto=random.randint(1,10)
print("acabo de generar un numero aleatoro")
numero=int(input("adivine el numero y luego de enter."))
if numero == secreto:
    print(f"usted adivino el numero {secreto}")
print(f"Lo siento, el numero secreto es: {secreto}")

'''
script en python que solicite la calificacion y cantidad de existencias a un curso
si la calificacon es mayor a 60 y la cantidad de asistencias es mayor a 20 entonces indicarle que aprobo el curso
'''

calificacion=int(input("Ingrese la calificacion: "))
asistencias=int(input("ingrese la cantidad de asistencias: "))
if calificacion > 60 and asistencias  >20:
    print("usted aprobo el curso.")
    print(f"su calificacion fue {calificacion} y su asistencia fue de {asistencias} dias.")
else:
    print("usted no aprobo el curso")

'''
Script en python que le pregunta al usuario cual es la temperatura y si el valor se encuentre entre 18 y 27 que le indique que la temperatura es agradable
'''
temperatura=int(input("Ingrese la temperatura del ambiente: "))
if 18 < temperatura < 27:
    print(f"Con {temperatura} grados, la temperatura es agradable.")


