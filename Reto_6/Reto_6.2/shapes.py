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
