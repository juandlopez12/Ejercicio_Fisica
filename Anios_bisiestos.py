'''
Los años bisiestos son aquellos años en donde se agrega un día más al año en el mes de febrero con el propósito de realizar 
un ajuste razonable con respecto al año solar. Esto se debe a que un año solar no equivale a exactamente 365 días, 
sino a 365.2425 días aproximadamente. Para definir si un año bisiesto se aplica una serie de reglas.


- Los años divisibles entre 4 son bisiestos.
- Los años que son divisibles entre 4, pero no entre 100, son bisiestos.
- Los años divisibles entre 100, pero que no son divisibles entre 400 no son bisiestos.
- Los años divisibles entre 100 y entre 400 son bisiestos

En este ejercicio deberá realizar un programa que reciba un año y determine si es un año bisiesto o no.
'''

año = int(input("Escriba el año en numero entero: "))

if año%4 == 0 and año%400 == 0: 
  print("Es un año bisiesto")
else: 
  if año%4 == 0 and año%100 != 0 and año%400 == 0:
    print("Es un año bisiesto")
  else:
     if año%100 == 0 and año%400 == 0:
       print("Es un año bisiesto")
     else:
       if año%4== 0 and año%100 != 0:
         print("Es un año bisiesto")
       else:
        print("No es un año bisiesto")