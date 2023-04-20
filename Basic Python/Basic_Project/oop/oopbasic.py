# oopbasic.py

class Student: #นักเรียน

    def __init__(self,name,age,gender):  #กำหนด
        self.name = name
        self.age = age
        self.gender = gender
        
    def study(self):            #เรียน
        print(f'{self.name} studying')

    def sayHello(self):        #ทักทาย
        if self.gender == 'male':
            lastWord = 'krub'
        else:
            lastWord = 'ka'
        print(f'Hello {lastWord}. My name is {self.name}')

class SpecialStudent(Student): #เด็กพิเศษ

    def __init__(self,name,age,gender,parent):   
        super().__init__(name,age,gender)
        self.parent = parent

    def hello(self, person='friend'):
        if person == 'friend':
            print('Hey What\'s up. Do you have money?')
        else:
            print('Yo!!! Who are you?')

    def sayHello(self):
        print(f'What\'s sup dude. I\'m {self.name} ')

    def showoff(self):
        print(f'Do you know {self.parent} is my fater')

class Teacher: #ครู
    def __init__(self,name,gender,subject):
        self.name = name
        self.gender = gender
        self.subject = subject

    def teach(self):
        print(f'Teacher {self.name} now teaching {self.subject}')

if __name__ == '__main__': #ใส่ไว้ตรวจสอบ

    
    #Generate 
    student1 = Student('Steve',14,'male')
    student2 = Student('Alex',14,'female')

    special_student = SpecialStudent('Patrick',16,'male','Prayut')
    
    teacher1 = Teacher('John','male','Math')
    
    print(teacher1.name)
    print(teacher1.subject)

    #Start activity
    print('---------8:30AM-------------')
    student1.sayHello()
    student2.sayHello()
    teacher1.teach()
    student1.study()
    student2.study()
    print('---------9:00AM-------------')
    special_student.sayHello()
    print('Walk to table')
    special_student.hello()
    special_student.showoff()