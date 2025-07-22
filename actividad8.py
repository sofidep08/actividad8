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
def contar_letra(palabra, letra):
    if len(palabra) == 0:
        return 0
    else:
        return (1 if palabra[0] == letra else 0) + contar_letra(palabra[1:], letra)
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * exponente
def invertir_cadena(cadena):
    if len(cadena) == 0:
        return "vacio"
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

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
            case 4:
                palabra = input("Ingrese una palabra: ")
                letra = input("Ingrese la letra que deseas contar: ")
                cantidad = contar_letra(palabra, letra)
                print(f"La letra {letra} aparece {cantidad} en la palabra {palabra}")
            case 5:
                texto = input("Ingrese un texto o palabra: ")
                texto_invertido = invertir_cadena(texto)
                print("Texto o palabra invertida:", texto_invertido)
            case 6:
                base = int(input("Ingrese un numero entero positivo: "))
                exponente = int(input("Ingrese un numero entero positivo: "))
                print(potencia(base, exponente))
            case 7:
                print("SALIENDO DEL MENU....")
