def operacion():
    opt = str(input("Que opcion desea realizar?[suma - resta]: "))
    n1 = int(input("Digite el primer numero; "))
    n2 = int(input("Digite el segundo numero; "))

    if(opt == "suma"):
        resultado = n1 + n2
        return resultado
    elif(opt == "resta"):
        resultado = n1 - n2
        return resultado
    else:
        return False

res = operacion()

if(res != False):
    print('El resultado de la operacion es:', res)
else:
    print("Error, intentelo nuevamente")