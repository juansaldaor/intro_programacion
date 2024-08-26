x= int(input("escribe un numero: "))
y= int(input("escribe otro numero: "))

x_mayor = (x,"es el numero mayor")
y_mayor = (y,"es el numero mayor")

if x > y:
    print (x_mayor)
elif x < y:
    print (y_mayor)
else:
    print ("son numeros iguales")
