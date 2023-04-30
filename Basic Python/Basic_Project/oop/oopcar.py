class Car:
    brand = None
    year = None
    fuel = None
    status = None

    def __init__(self, brand='Toyota', year=2022, fuel=100, status=True):
        self.brand = brand
        self.year = year
        self.fuel = fuel
        self.status = status

    def checkStatus(self):
        if self.status == True:
            print('This car is pass from check')
        else:
            print('This car don\'t check again pass')

    def drive(self):
        print('This car is driving')

if __name__ == '__main__':
    car1 = Car('BMW', 2021, 50.0, True)
    car2 = Car('Honda', 2022, 50, False)
    car3 = Car()
    print(f'Brand is {car1.brand}')
    print(f'Years is {car1.year}')
    print(f'Fuel is {car1.fuel}')

    car1.drive()
    car1.checkStatus()
    print('-------------------')
    print(f'Brand is {car3.brand}')
    print(f'Years is {car3.year}')
    print(f'Fuel is {car3.fuel}')

    car3.checkStatus()