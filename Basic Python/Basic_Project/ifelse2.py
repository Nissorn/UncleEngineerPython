employee = ['Tim','Steve','Ive'] #listชื่อคนที่สามารถเข้ามาได้
employee2 = {'Tim':'Tim Cuk',
             'Steve':'Steve Jub'} #dictionaryคนที่เรารู้ชื่อ และจะทักทายด้วยชื่อ

visitor = 'Ive'

if visitor in employee or visitor.title() in employee: # .title .upper .lower คือคำสั่งเปลี่ยนรูปแบบอักษร
    print('They are headquarter, Come in!')
    if visitor in employee2 or visitor.title() in employee2:
        print('Hello ' + employee2[visitor.title()])
    else:
        print('Hello')
else: 
    print('Who are you!!')