

#Asignacion de valores

x0 = float(input("Escribra la posicion inicial (m): "))
v0 = float(input("Escriba la velocidad inicial (km/h): "))
a = float(input("Escriba la posicion inical (m/s2): "))
t = float(input("Escriba la posicion inicial (seg): "))


#Operacion 1

v0 = v0 * (1/3.6)
x = x0 + (v0 * t) + 0.5 * (a * (t**2))

#Operacion 2

v = v0 + (a*t)
v = v * 3.6


print(f"La posición final es de {x:.2f} m y la velocidad es de {v:.3f} km/h")
