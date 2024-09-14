lista_pala=[]
no_vacio=True
while no_vacio==True:
    palabra= str(input("Digite las palabras que quiera evaluar que tengan los mismos caracteres; o deje el cambio vacio para terminar:"))
    if palabra !="":
        lista_pala.append(palabra)
    else:
        break
    
def letras_palabras(lista_palabras):
    palabras_bien=[]
    lista_aux=[]+lista_palabras
    palabra_base: str
    palabra_ahora: str
    letra: str
    i=0
    g=0
    d=0
    while i<len(lista_palabras):
        palabra_base=lista_palabras[i]
        j=0
        palabra_letras=[]
        c=0
        while c<len(palabra_base):
            palabra_letras.append(palabra_base[c])
            c +=1
        c=0
        while c<len(palabra_letras):
            d=0
            h=0
            while h<len(palabra_letras):
                a=palabra_letras[h]
                b=palabra_letras[c]
                if palabra_letras[h]==palabra_letras[c]:
                    
                    d +=1
                if d>1:
                    palabra_letras.pop(h)
                    h -=1
                    d -=1
                h +=1
            c +=1
        
        while j<len(lista_palabras):
            palabra_ahora=lista_palabras[j]
            k=0

            t=0
            while k<len(palabra_letras):
                w=0
                
                while w<len(palabra_ahora):
                    if (palabra_letras[k]==palabra_ahora[w])==True:
                        t +=1
                
                    w +=1
                k +=1
            if t==len(palabra_ahora):
                palabras_bien.append(j)
            j +=1
        i +=1


    c=0

    i=len(palabras_bien)
    while c<i:
        h=0
        d=0
        while h<i:
            if palabras_bien[h]==palabras_bien[c]:
                d+=1
            h +=1
        if d==1:
            palabras_bien.pop(c)
            i=len(palabras_bien)
            c -=1
        c+=1 

    c=0
    i=len(palabras_bien)
    while c<i:
        h=0
        d=0
        while h<i:
            a=palabras_bien[h]
            b=palabras_bien[c]
            if palabras_bien[h]==palabras_bien[c]:
                d+=1
            h +=1
        if d>1:
            palabras_bien.pop(c)
            i=len(palabras_bien)
            c -=1
        c+=1 


    palabras_bien=sorted(palabras_bien)
    c=0
    i=len(palabras_bien)
    while c<i:
        h=int(palabras_bien[c]) - c
        lista_aux.pop(h)
        c+=1


    c=0
    i=len(lista_palabras)
    while c<i:
        h=0
        b=len(lista_aux)
        while h<b:
            if lista_palabras[c]==lista_aux[h]:
                lista_palabras.pop(c)
                i=len(lista_palabras)
                c -=1  
            h +=1
        c+=1 
    return lista_palabras

print(letras_palabras(lista_pala))
