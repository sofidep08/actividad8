

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
