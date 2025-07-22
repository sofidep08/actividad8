def factorial(numero):
    if numero ==0 or numero==1:
        return 1
    else:
        print(numero, " * " ,numero-1)
        return numero*factorial(numero-1)

def suma_numeros(numero2):
    if numero2 ==0:
        return 0
    else:
        return numero2 + suma_numeros(numero2-2)
def fibonacci(numero3):
    if numero3 <= 0:
        return 0
    elif numero3 == 1:
        return 1
    else:
        return fibonacci(numero3-1) + fibonacci(numero3-2)


opcion = 0
while opcion != 7:
    print("[1] Calcular el factorial")
    print("[2] Suma de los primeros números naturales")
    print("[3] Calcular el n-ésimo número de Fibonacci")
    print("[4] contar cuantas veces aparece una letra en una tabla")
    print("[5] Invertir una cadena de texto")
    print("[6] Calcular la potencia de un número (base^exponente)")
    print("[7] Salir")
    opcion=int(input("Elija una opcion: "))
    if opcion <=0 or opcion >7:
        print("Ingreso un dato incorrecto")
    else:
        match opcion:
            case 1:
                numero = int(input("Ingrese un numero entero positivo: "))
                if numero < 0:
                    print("Ingreso un dato incorrecto")
                else:
                    print(factorial(numero))
            case 2:
                numero2 = int(input("Ingrese un numero entero positivo: "))
                if numero2 < 0:
                    print("Ingreso un dato incorrecto")
                else:
                    print(suma_numeros(numero2))
            case 3:
                numero3 = int(input("Ingrese un numero entero positivo: "))
                if numero3 < 0:
                    print("Ingreso un dato incorrecto")
                else:
                    print(fibonacci(numero3))