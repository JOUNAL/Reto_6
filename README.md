# Reto_6
Excepciones
# Programación Orientada a Objetos - UNAL

## Reto 6.1

Para este reto se utilizaron el codigo realizado en el reto 1, donde se le aplicaron las excepeciones para cada caso pertinente, a continuacion, se explicara el que y el porque se aplicaron las excepciones en cada caso

### Codigo 1: Calculadora
Para este codigo se utilizaron dos excepciones, ValueError, que se aplico en general para toda la funcion; este error se aplico en general por que si se digita un valor no int o float en la operacion, ninguna operacion podra ser realizada, y la segunda excepcion fua aplicada para el caso de la division y fue ZeroDivisionError, esta excepcion solo se aplico aca dado que saltaria error si se llega a hacer una division con el denomidaro igual a cero

Codigo:

```python
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
```

### Codigo 2: Palindromo
En este caso no se aplico ninguna excepcion dado, que la lista puede ir vacio, y tecnica seguiria siendo un palindromo, y no importa que simbolos o caracteres se digite, solo evaula si esa cadena esta escrita igual de derecha a izquierda y de izquierda a derecha

Codigo:

```python
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
```

### Codigo 3: Numero primos
Se agrego solo una excepcion en este codigo, la cual fue ValueError, y esta se aplico debido a que se realizarian operaciones matematicas para verificar si los numeros ingresados en la lista eran primos, y si se ingresaba un valor no numerico a la lista, saltaria un error, del resto, cualquier numero por debajo de 1 tecnicamente no es un numero primo

Codigo:

```python
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
```

### Codigo 4: Mayor suma
Se agregaron dos excepciones en el codigo, la primera, IndexError, debido a que se trabaja con las posiciones de una lista y si se envia una lista vacia, daria error, y la segunda, de ValueError, debido a que se estan haciendo numericas y si se digita algo aparte de un valor numerico en la lista daria error

Codigo:

```python
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
```

### Codigo 5: Caracter iguales
No se agrego ninguna excepcion debido a que solo se esta verificando si los caracteres ingresados en la lista se repiten mas de una vez

Codigo:

```python
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
```


## Reto 6.2
Para este reto se utilizo el
### Visitando de nuevo

En este caso, el restaurante que visitamos por fin implemento la opcion de pago, asi que ya no nos debemos endeudar con un restaurante, se puede pagar en este caso de dos forma, con tarjeta y con efectivo, al pagar con tarjeta se requiere introducir de nuevo el codigo de seguridad, y mostrara en la terminal los ultimos 4 numeros de la tarjeta y que el pago ha sido realizado exitosamente, y al pagar con efectivo, podra mostrar 2 mensajes, pago realizado y cuanto le dan de cambio, o que el pago no se realizo debido a que le faltaba dinero y le dice cuanto le falta
Tambien le adicionaron que si compro 2 objetos o mas en el restaurante, y entre ellos iba un plato principal, se le realizara un descuento del 10%


Y este seria el codigo, con cada una de las clases y subclases definidas (cada una con los setters y getters correspondientes), y lo que seria un ejemplo de la orden de un cliente
```python
class MethodPay:
  def __init__(self):
    pass

  def pay(self):
    raise NotImplementedError("Subclases deben implementar pagar()")

class Card(MethodPay):
  def __init__(self, number, cvv):
    super().__init__()
    self.number = number
    self.cvv = cvv

  def pay(self, mount,cvv2):
    if self.cvv==cvv2:
        print(f"Pagando {mount} con tarjeta {self.number[-4:]}")
    else:
        print("Contraseña incorrecta")

class Cash(MethodPay):
  def __init__(self, delivered_cash):
    self.delivered_cash = delivered_cash

  def pay(self, mount):
    if self.delivered_cash >= mount:
      print(f"Pago realizado en efectivo. Cambio: {self.delivered_cash - mount}")
    else:
      print(f"Fondos insuficientes. Faltan {mount - self.delivered_cash} para completar el pago.")


pago1 = Card("1234567890123456", 123)
pago2 = Cash(50000)

class Order:
    def __init__(self):
        self.list =[]

    def total_price(self):
        self.total = sum([item.subtotal for item in self.list])
        return self.total

    def set_total_price(self):
        self.total = sum([item.subtotal for item in self.list])
        self.total -= self.total * self.discount
        return self.total

    def add_item(self, item):
        self.list.append(item)

    def get_list(self):
        ([item.name for item in self.list])
        print("Nombre                 Precio")
        for item in self.list:
            print(f"{item.name} x {item.quantity}    {item.price}")
    def discount_n(self):
        if len(self.list)>1:
            for item in self.list:
                if item.menu_item=="MainDish":
                    self.discount=0.10
    def get_discount_n(self):
        return self.discount





class MenuItem:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.subtotal= self.price*self.quantity
    
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    
    def set_price(self, price):
        self.price = price
    def get_price(self):
        return self.price
    
    def get_quantity(self):
        return self.quantity

    def get_subtotal(self):
        return self.subtotal


class Juice(MenuItem):
    def __init__(self, name, price,quantity,sugar):
        super().__init__(name, price,quantity)
        self.menu_item="Juice"
        self.sugar=sugar
    
    def set_sugar(self, sugar):
        self.sugar = sugar

    def get_sugar(self):
        return self.sugar

class Soup(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.menu_item="Soup"
        self.kind=kind
    
    def set_kind(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind
     
class Soda(MenuItem):
    def __init__(self, name, price,quantity,sugar):
        super().__init__(name, price,quantity)
        self.menu_item="Soda"
        self.sugar=sugar

    def set_sugar(self, sugar):
        self.sugar = sugar

    def get_sugar(self):
        return self.sugar
        
class IceCream(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.menu_item="IceCream"
        self.kind=kind

    def set_kind(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind
        
class Beer(MenuItem):
    def __init__(self, name, price,quantity,brand):
        super().__init__(name, price,quantity)
        self.menu_item="Beer"
        self.brand=brand
    
    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand
        
class Sandiwch(MenuItem):
    def __init__(self, name, price,quantity,protein):
        super().__init__(name, price,quantity)
        self.menu_item="Sandiwch"
        self.protein=protein
    
    def set_protein(self, protein):
        self.protein = protein

    def get_protein(self):
        return self.protein
        
class MainDish(MenuItem):
    def __init__(self, name, price,quantity,description):
        super().__init__(name, price,quantity)
        self.menu_item="MainDish"
        self.description=description

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
        
class Beef(MenuItem):
    def __init__(self, name, price,quantity,grams):
        super().__init__(name, price,quantity)
        self.menu_item="Beef"
        self.grams=grams

    def set_grams(self, grams):
        self.grams = grams

    def get_grams(self):
        return self.grams
        
class SideDish(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.menu_item="SideDish"
        self.kind=kind

    def set_kind(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind
        
class Appetizer(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.menu_item="Appetizer"
        self.kind=kind

    def set_kind(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind

orden=Order()

orden.add_item(Juice(name="Jugo de mango",price=2000,quantity=3,sugar="No"))
orden.add_item(Soup(name="Sancocho de pescado",price=4000,quantity=2,kind="Sancocho"))
orden.add_item(MainDish(name="Cerdo a la llanera",price=9000,quantity=2,description="Cerdo con salsa de la casa, arroz, patacon y ensalada"))
orden.add_item(Appetizer(name="Parfait",price=3500,quantity=2,kind="Dulce"))

orden.discount_n()
print("El precio total de la orden es:" + str(orden.total_price()))
orden.get_list()
print("Su descuento seria del:" +str((orden.get_discount_n())*100) + "%")

pago1.pay(mount=orden.set_total_price(),cvv2=123)
pago2.pay(mount=orden.set_total_price())
```
El resultado de la terminal seria el siguiente
```
El precio total de la orden es:39000
Nombre                 Precio
Jugo de mango x 3    2000
Sancocho de pescado x 2    4000
Cerdo a la llanera x 2    9000
Parfait x 2    3500
Su descuento seria del:10.0%
Pagando 35100.0 con tarjeta 3456
Pago realizado en efectivo. Cambio: 14900.0
```
