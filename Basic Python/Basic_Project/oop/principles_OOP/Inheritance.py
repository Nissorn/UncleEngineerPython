class One:
    name = None

    def __init__(self,name):
        self.name = name

    def walk(self):
        print('I can walk')

class Two(One):
    nickname = 'Uncle'

    def __init__(self, name, nickname):
        super().__init__(name)
        self.nickname = nickname

    def run(self):
        print('I can run')

class Three(One):
    def eat(self):
        print('I can eat')

class Four(Two):
    def fly(self):
        print('i can fly')

if __name__ == '__main__':
    # three = Three()
    # print(three.name)

    # three.eat()
    # three.walk()

    # print("__________________")

    # four = Four()
    # print(four.name)
    # print(four.nickname)

    # four.walk()
    # four.run()
    two = Two('Nissorn','O')
    print(two.name)
    print(two.nickname)