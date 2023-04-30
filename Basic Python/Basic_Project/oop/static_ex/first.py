class First:
    language = 'Python'

    def learn(): #static method
        print(f'I\'m stuyding {First.language}')

    def teach(self):
        First.learn()
        print(f'I can teach {self.language}')

if __name__ == '__main__':
    print(f'This is {First.language}')
    First.learn()

    first = First()
    first.teach()