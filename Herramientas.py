def operacion():
    opt = str(input("Que opcion desea realizar?[suma - resta - multiplicacion - division]: "))
    n1 = int(input("Digite el primer numero; "))
    n2 = int(input("Digite el segundo numero; "))
    print("hola bellaco")

    if(opt == "suma"):
        resultado = n1 + n2
        return resultado
    elif(opt == "resta"):
        resultado = n1 - n2
        return resultado
    elif (opt == "multiplicacion"):
        resultado = n1 * n2
        return resultado
    elif (opt == "division"):
        if(n2 > 0):
            resultado = n1 / n2
            return resultado
        else:
            return False
    else:
        return False

res = operacion()

if(res != False):
    print('El resultado de la operacion es:', int(res))
else:
    print("Error, intentelo nuevamente")
