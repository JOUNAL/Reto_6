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
Para este reto se utilizo el codigo del reto 5, agregando excepciones para cada caso necesario

### Shapes, Shapies y demas

Para este caso, se necesito incluir la excepcion de ValueError en cada parte del codigo y de los paquetes donde se realizaban calculos numericos

Codigo Shapes:
```python
from packages.squaris import *
from packages.trianglis import *
import math


class Point:
    
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
    def reset(self):
        self.x = 0
        self.y = 0
    def compute_distance(self, point)-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance

first_point = Point(x=1, y=2)
second_point = Point(x=2, y=3)



class Line:

    def __init__(self,startp,endp):
        self.startp=startp
        self.endp=endp

    def compute_lenght(self):
        try:
            self.lenght=(((self.endp.y-self.startp.y))**2+((self.endp.x-self.startp.x)**2))**0.5
            return self.lenght
        except TypeError as Error:
            print(f"Error:{Error}")
    
    def compute_slope(self):
        try:
            if self.startp.x!=self.endp.x:
                self.slope=(self.endp.y-self.startp.y)/(self.endp.x-self.startp.x)
            else:
                self.slope=0
            return self.slope
        except TypeError as Error:
            print(f"Error:{Error}")
    
    def compute_degree(self):
        try:
            if self.startp.x!=self.endp.x:
                self.degree=math.degrees(math.atan2((self.endp.y-self.startp.y),(self.endp.x-self.startp.x)))
            else:
                self.degree=0
            return self.degree
        except TypeError as Error:
            print(f"Error:{Error}")
    
    def compute_vertical_cross(self):
        try:
            self.intersecty=self.startp.y-(self.slope*self.startp.x)
            if self.startp.x<=0<=self.endp.x:
                return self.intersecty
            else:
                return False
        except TypeError as Error:
            print(f"Error:{Error}")

    def compute_horizontal_cross(self):
        try:
            if self.startp.x!=self.endp.x:
                self.intersectx=(self.startp.y*0-self.intersecty)/self.slope

            else:
                self.intersectx=self.startp.x

            if self.startp.y<=0<=self.endp.y:
                return self.intersectx
            else:
                return False
        except TypeError as Error:
            print(f"Error:{Error}")

Linea0=Line(startp=first_point,endp=second_point)
print("La longitud de la linea es: " + str(Linea0.compute_lenght()))
print("La pendiente de la linea es: " + str(Linea0.compute_slope()) + ", y eso con un angulo de: " + str(Linea0.compute_degree()) + "°")

if (Linea0.compute_vertical_cross())== False:
    print("La linea no corta el eje Y")
else:
    print("La linea corta en Y en:" + str(Linea0.compute_vertical_cross))

if (Linea0.compute_horizontal_cross())== False:
    print("La linea no corta el eje X")
else:
    print("La linea corta en X en:" + str(Linea0.compute_vertical_cross))

tp1=Point(x="a",y=2)
tp2=Point(x=3,y=5)
tp3=Point(x=5,y=2)

tL1=Line(startp=tp1,endp=tp2)
tL2=Line(startp=tp2,endp=tp3)
tL3=Line(startp=tp3,endp=tp1)

tedges1=[tL1,tL2,tL3]
tvertices1=[tp1,tp2,tp3]

triangulo1=Iscoceles(edges=tedges1,vertices=tvertices1)
print("Los angulos internos del triangulo son:" + str(triangulo1.compute_inner_angles()))


rp1=Point(x="a",y=2)
rp2=Point(x=7,y=5)
rp3=Point(x=12,y=5)
rp4=Point(x=12,y=2)

rL1=Line(startp=rp1,endp=rp2)
rL2=Line(startp=rp2,endp=rp3)
rL3=Line(startp=rp3,endp=rp4)
rL4=Line(startp=rp4,endp=rp1)

redges1=[rL1,rL2,rL3,rL4]
rvertives1=[rp1,rp2,rp3,rp4]

rectangulo1=Rectangle(edges=redges1,vertices=rvertives1)

print("El perimetro del triangulo es de:" + str(triangulo1.compute_perimeter()))
print("El area del triangulo es de:" + str(triangulo1.compute_area()))
print("El area del rectangulo es de:" + str(rectangulo1.compute_area()))
print("El perimetro del rectangulo es de:" + str(rectangulo1.compute_perimeter()))
```

Codigo Shapies:

```python
import math

class Shape:
    def __init__(self,edges,vertices):
        self.edges=edges
        self.vertices=vertices

    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar calcular area()")
    
    def compute_perimeter(self):
        try:
            a=0
            for const in range(len(self.edges)):
                a+=(self.edges[const]).compute_lenght()
            self.perimeter=a
            return self.perimeter
        except TypeError as Error:
            print(f"Error:{Error}")
    
    def compute_inner_angles(self):
        raise NotImplementedError("Subclases deben implementar calcular angulos internos()")
    
    def set_vertices(self, vertices):
        self.vertices=vertices
    
    def get_vertices(self):
        return self.vertices
    
    def set_edges(self, edges):
        self.edges=edges
    
    def get_edges(self):
        return self.edges
    
    def get_perimeter(self):
        return self.perimeter
    
    def get_inner_angles(self):
        return self.inner_angles
```

Codigo Squaris:

```python
from packages.shapies import Shape
import math

class Rectangle(Shape):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)
        self.inner_angles=([90]*4)

    def compute_area(self):
        try:
            a=1
            for const in range(len(self.edges)):
                a*=(self.edges[const]).compute_lenght()
            self.area=math.sqrt(a)
            return self.area
        except ValueError as Error:
            print(f"Error:{Error}")

class Square(Rectangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)
        self.inner_angles=([90]*4)
```

Codigo Triangis:

```python
from packages.shapies import Shape
import math
    
class Triangle(Shape):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)

    def compute_area(self):
        try:
            a=0
            for const in range(len(self.edges)):
                a+=(self.edges[const]).compute_lenght()
            self.perimeter=a
            s=(self.perimeter)/2
            self.area=math.sqrt(s*(s-((self.edges[0]).compute_lenght()))*(s-((self.edges[1]).compute_lenght()))*(s-((self.edges[2]).compute_lenght())))
            return self.area
        except TypeError as Error:
            print(f"Error:{Error}")

    def compute_inner_angles(self):
        try:
            a = self.edges[0].compute_lenght()
            b = self.edges[1].compute_lenght()
            c = self.edges[2].compute_lenght()
            angle_alpha = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
            angle_beta = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
            angle_gamma = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
            self.inner_angles = [angle_alpha, angle_beta, angle_gamma]
            return self.inner_angles
        except TypeError as Error:
            print(f"Error:{Error}")

class Iscoceles(Triangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)


class Equilateral(Triangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)
        self.inner_angles=[60]*3

class Scalene(Triangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)

class Rectangle(Triangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)
```


Muchas Gracias por leer.

