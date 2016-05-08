import math

class Ellipse:
    def _init_me(self,m,n):
        self.m=m
        self.n=n
        x=math.pi*m*n
        return x
        print(x)
class Circle(Ellipse):
    def _init_mc(self,m):
        self.m=m
        x=math.pi*m
        return x
        print(x)

class Rectange():
    def _init_mr(self,m,n):
        self.m=m
        self.n=n
        x=m*n
        return x
        print(x)

class Square(Rectange):
    def _init_ms(self,m):
        self.m=m
        x=m*m
        return x
        print(x)

shapes=[Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)]

ob=[a,b,c,d,e,f,g]

def compute_area(shapes):
    for i in range(0,len(shapes)):
        ob[i]=shapes[i]


total_area=compute_area(shapes)
print(total_area)
