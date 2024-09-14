lista_numeros=[]

numero=True
while numero==True:
    nuevo_numero= input("Digite la lista de numeros; o una letra para parar:")
    if nuevo_numero.isnumeric()==True:
        lista_numeros.append(nuevo_numero)
    else:
        break
def sum_mayor(lista_y):
    try:
        i: int=0
        valor=0
        valor_m=0
        posicion=0
        while i<len(lista_y)-1:
            valor=int(lista_y[i])+int(lista_y[i+1])
            if valor>valor_m:
                valor_m=valor
                posicion=i
            i +=1
        print("Los numeros que dan la suma de mayor valor son " + str(lista_y[posicion]) + " y " + str(lista_y[posicion+1]))
        return valor_m
    except IndexError as Error:
        print(f"Error:{Error}")
    except ValueError as Error1:
        print(f"Error:{Error1}")
        
lista_algo=["j","h","h","l"]
print("La mayor suma consecutiva de la lista es:" + str(sum_mayor(lista_numeros)))

print("La mayor suma consecutiva de la lista es:" + str(sum_mayor(lista_algo)))

