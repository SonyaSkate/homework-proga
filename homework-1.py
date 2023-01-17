import math
class NotValid(Exception):
    pass

class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        if not self.is_valid():
            raise NotValid
    
    def square(self):
        p = (self.side_1 + self.side_2 + self.side_3) / 2
        return round(math.sqrt(p*(p-self.side_1)*(p-self.side_2)*(p-self.side_3)))

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3
        
    def is_valid(self):
        return self.side_1 < self.side_2 + self.side_3, self.side_2 < self.side_1 +self.side_3, self.side_3 < self.side_1 + self.side_2

result_tringle = Triangle(8, 7, 13)
print(result_tringle.square())
print(result_tringle.perimeter())

class Circle:
    def __init__(self, r):
        self.r = r
        if not self.is_valid():
            raise NotValid

    def length(self):
       return round(2 * math.pi * self.r)
    
    def circle_square(self):
        return round(math.pi *self.r **2)

    def is_valid(self):
        if type(self.r) in (int, float):
            return self.r > 0
     
result_circle = Circle(3)
print(result_circle.length())
print(result_circle.circle_square())



