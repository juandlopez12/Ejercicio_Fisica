'''
Según el libro de texto, la posición de un objeto puede ser calculada por la siguiente ecuación:

x =  x0 + v0(t) + 1/2(a*t^2)

Por otro lado, la velocidad de un objeto puede obtenerse a partir de la siguiente ecuación:

v = v0 + a*t

En los ejercicios propuestos la posición inicial es recibida en metros (m), la velocidad en kilometros por hora (km/h), 
la aceleración en metros sobre segundos al cuadrado (m/s2) y el tiempo en segundos (s); mientras que la posición (x) y 
la velocidad (v) son solicitados en metros (m) y kilometros por hora (km/h) respectivamente.

El programa debe calcular la posicion y la velocidad final, Además, para definir una presentación consistente decide 
realizar un redondeo del valor obtenido con dos dígitos decimales para la posición y tres dígitos decimales para la 
velocidad.

'''


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