'''
script python que implemente un sistema de redondeo de calificaciones.El usuario es el encargado de ingresar sus calificacion
Si la calificacion le faltan 4 unidades o menos para el siguiente multiplo de 10, entonces su calificacion sera redondeada
al sigiente multiplo de 10, en caso contrario la calificacion no se modificara.
ejemplo:
    si tiene 76 se redondea a 80
    si tiene 77 se redondea a 80
    si tiene 75 se queda en 75
'''
'''
calificacion=int(input("ingrese su calificación: "))
if calificacion >= 0 and calificacion <=10:
    if 10 - calificacion <=4:
        print(f"Su calificacion de {calificacion} sera redondeada a 10")
'''
calificacion=int(input("ingrese su calificacion: "))
residuo = calificacion%10
redondeo= calificacion+(10-residuo)
if residuo >= 6:
    print(f"Su nota {calificacion} sera redondeado a {redondeo}")
print(f"Su nota es {calificacion} ")
'''
7%10=7
13%10=3
98%10=8
'''
