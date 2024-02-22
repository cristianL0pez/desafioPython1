#importamos las librerias
import math 

#variable del input
g = float(input("Ingrese la constante g: "))
r_km = float(input("Ingrese el radio en Kilómetros: "))


r_m = r_km * 1000


ve =  math.sqrt(2 * g * r_m)


print(f"La velocidad de Escape es: {ve} [m/s]")
