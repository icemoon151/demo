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



