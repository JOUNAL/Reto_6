def palindromo(var1):
    i:int=0
    j:int=0
    longitud=int(len(var1))
    j=longitud//2
    while i < j:
        if var1[i]==var1[longitud-(1+i)]:
            i+=1
        else:
            return 0
    return 1

palabra= str(input("Digite la palabra a validar:"))
if palindromo(palabra)==0:
    print(palabra + " no es un palindromo")
else:
    print(palabra + " es un palindromo")