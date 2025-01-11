#Programa que solicite nombre y edad y devuelva un saludo y el año en que naciste
año = 2025
nombre = input("¿Cuál es tu nombre? -->")
edad = input("¿Cuántos años tienes? -->")
# Validar que la entrada sea un número
edad = int(edad) #NO sabemos si el usuario puso algo que no sea puede transformar

# Calcular el año de nacimiento
año_nacimiento = año - edad

print(f"Hola {nombre} naciste en el año {año_nacimiento}")



