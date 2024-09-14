num1= input("Digite los numeros a operar:")
num2= input()
operacion= str(input("Digite la operacion a realizar:"))
def Operaciones(numero1: float,numero2: float,opera: str):
    try:
        match opera:
            case "+":
                a=float(numero1)+float(numero2)
                return a
            case "-":
                a=float(numero1)-float(numero2)
                return a
            case "*":
                a=float(numero1)*float(numero2)
                return a
            case "/":
                try:
                    a=float(numero1)/float(numero2)
                    return a
                except ZeroDivisionError as Error:
                    print(f"Error:{Error}")
    except ValueError as Error:
        print(f"Error:{Error}")
print("El resultado de la operacion es:" + str(Operaciones(num1,num2,operacion)))
