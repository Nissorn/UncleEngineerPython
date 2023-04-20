#while1.py

money = 1000
transfer = 8000

print('Check:', money < transfer)

while money < transfer:
    print('Please Enter again')
    transfer = int(input('new transfer: '))
    if transfer > 1000000:
        print('It a lot of money i will call police to checks')
        break

print('Bye')