print("Bienvenido a Suma de Numeros")

cuantosNumerosDeseaSumar = int(input("Cuantos numeros desea sumar? "))

suma = 0
for i in range(cuantosNumerosDeseaSumar):
    numero = int(input("Ingrese el numero: "))
    suma = suma + numero
print(f"La suma de los {cuantosNumerosDeseaSumar} es: {suma}")

