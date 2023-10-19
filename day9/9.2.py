import math


class Point:

    def __init__(self, x, y, z):
        self.x = 0
        self.y = 0
        self.z = 0
        print(f"创建了point({self.x}, {self.y}, {self.z})")

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, Point):
            print("不能相加")

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        if isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __eq__(self, other):
            if self.x == other.x and self.y == other.y and self.z == other.z:
                return True
            else:
                return False
            
    def __lt__(self, other):
            return (self.x ** 2 + self.y ** 2 + self.z ** 2)**0.5 < (other.x ** 2 + other.y ** 2 + other.z ** 2)**0.5

    def __del__(self):
        print(f"销毁了point({self.x}, {self.y}, {self.z})")


class Vector:

    def __init__(self, x, y, z):
        self.x = 0
        self.y = 0
        self.z = 0

    def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        
    def __lt__(self, other):
            return  (self.x ** 2 + self.y ** 2 + self.z ** 2)**0.5 < (other.x ** 2 + other.y ** 2 + other.z ** 2)**0.5
    
    def __mul__(self, du):
        rad = math.radians(du)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y, self.z)

    def __truediv__(self, du):
        rad = math.radians(du)
        new_x = self.x * math.cos(rad) + self.y * math.sin(rad)
        new_y = -self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y, self.z)

    def __eq__(self, other):
            if self.x == other.x and self.y == other.y and self.z == other.z:
                return True
            else:
                return False    