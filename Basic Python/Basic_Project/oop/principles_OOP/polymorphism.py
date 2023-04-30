from abc import ABC, abstractmethod
class Geometry(ABC):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @abstractmethod
    def calArea(self):
        #คำนวณหาพื้นที่
        pass

class Triangle(Geometry): #Area triangle
    def __init__(self, base, height):
        super().__init__(base,height)

    def calArea(self):
        return 0.5 * self.base * self.height
    
class Parallel(Geometry):
    def __init__(self, base, height):
        super().__init__(base,height)

    def calArea(self):
        return self.base * self.height
    
class Rhombus(Geometry):
    def __init__(self, base, height):
        super().__init__(base,height)
    
    def calArea(self):
        return self.base * self.height

if __name__ == '__main__':
    triangle = Triangle(10, 6)
    print(f'Area Triangle = {triangle.calArea()}')
    parallel = Parallel(10, 6)
    print(f'Area Triangle = {parallel.calArea()}')
    rhombus = Rhombus(10, 6)
    print(f'Area Triangle = {rhombus.calArea()}')