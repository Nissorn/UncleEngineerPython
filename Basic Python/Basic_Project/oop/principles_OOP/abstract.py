class Square:
    def __init__(self, length):
        self.length = length
    
    def calculate(self):
        return self.length * self.length
    
class Cube(Square):
    def __init__(self, length):
        super().__init__(length)

    def calculate(self):
        return super().calculate() * self.length
    
if __name__ == '__main__':
    square = Square(5)
    print(f'Area this square = {square.calculate()}')

    cube = Cube(10)
    print(f'Value this cube = {cube.calculate()}')