nombre = input ("ingresa tu nombre: ")
year_nacimiento = int(input("en que año naciste?: ") )
edad = 2024 - year_nacimiento 

generacion = 0
if year_nacimiento < 1948:
    generacion = str("niños de la posguerra")
elif year_nacimiento < 1968:
    generacion = str("Baby boomer")
elif year_nacimiento < 1980:
    generacion = str("Generacion x")
elif year_nacimiento < 1993:
    generacion = str("Millenial")
elif year_nacimiento < 2010:
    generacion = str("Generacion z")
else:
    generacion = str("Generacion Alfa")

print ("oh entonces tienes",edad,"años, y perteneces a los ",generacion,nombre )