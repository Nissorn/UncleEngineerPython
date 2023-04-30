from abc import ABC, abstractmethod

class Rectangle(ABC):

    @abstractmethod
    def calculate(self):
        pass

class Rectangular(Rectangle):
    def __init__(self,width,length,depth):
        self.width = width
        self.length = length
        self.depth = depth

    def calculate(self):
        return self.width * self.length * self.depth

if __name__ == '__main__':
    # rect = Rectangle()
    # rect.calculate() #This will show error

    rect3D = Rectangular(8,9,10)
    print(f'Rectangular volume = {rect3D.calculate()} ')