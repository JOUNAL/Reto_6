lista_total=[]
valor=0
numero=True
while numero==True:
    nuevo_numero= input("Digite numeros para verificar si son primos, o una letra para parar:")
    if nuevo_numero.isnumeric()==True:
        lista_total.append(nuevo_numero)
    else:
        break
def num_primos(lista_x):
    try:
        i: int=0
        lista_prima=[]
        while i<len(lista_x):
            j: int=2
            while j < int(lista_x[i]):
                if int(lista_x[i]) % j != 0:
                    j +=1
                    if j==int(lista_x[i]):
                        lista_prima.append(lista_x[i])
                else:
                    break
            i +=1
        i=0
        return lista_prima
    except ValueError as Error:
        print(f"Error:{Error}")


a=[-1,-2,-3,-4]

print("Los numeros primos de la lista digitada son:")
while valor<len(num_primos(lista_total)):
    print(num_primos(lista_total)[valor])
    valor +=1
print(num_primos(a))