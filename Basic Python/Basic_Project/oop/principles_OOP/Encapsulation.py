class BankAccount:
    def __init__(self, name, age, amount):
        self.name = name #public
        self._age = age #protect
        self.__amount = amount #private

    def showMessage(self):
        print('Depositing and withdrawing in the account')

    def _deposit(self, deposit):
        self.__amount += deposit 
        print(f'Deposit {deposit} sum {self.__amount}')

    def __withdraw(self, withdraw):
        self.__amount -= withdraw
        print(f'withdraw {withdraw} sum {self.__amount}')

    # def getAmount(self):     #Getter
    #     return self.__amount
    
    # def setAmount(self,amount):     #Setter
    #     self.__amount = amount
    @property
    def amounts(self):     #Getter
        return self.__amount
    @amounts.setter
    def amounts(self,amount):     #Setter
        self.__amount = amount


    # data = property(getAmount,setAmount)

class Employee(BankAccount):
    def __init__(self, name, age, amount):
        super().__init__(name, age, amount)

if __name__ == '__main__':
    employee = Employee('Steve',18,100000)
    print(employee.name)
    print(employee._age)
    # print(employee.data)
    print(employee.amounts)

    # employee.data= 200000
    # print(employee.data)
    employee.amounts= 200000
    print(employee.amounts)
    


    # employee.showMessage()
    # employee._deposit(5000)