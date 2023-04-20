#forloop1.py

for i in range(5):
    print('Hello',i)

print('---Loop in list---')
employee = ['Tim','Steve','Ive','Job','Alex']

employee2 = {'Tim':'Tim Cuk',
             'Steve':'Steve Jub',
             'Ive':'Jo Ive'}

# for e in employee:
#     print(e)
#     if e == 'Tim':
#         print('Hello Tim Cuk CEO Appie')
#     else:
#         print('Hello')

#show key
for f in employee2:
    print(f)

#show items
for f in employee2.items():
    print(f)

#show key2
for f in employee2.keys():
    print(f)

#show value only
for f in employee2.values():
    print(f)

#show all
for k,v in employee2.items():
    print('Key:',k)
    print('Value:',v)

#ต้องการลำดับ
for f in enumerate(employee, start=1000):
    print(i,f)

#ต้องการลำดับสำหรับ dict
for i,f in enumerate(employee2.items()):
    print(i,f)

#ต้องการลำดับสำหรับ dict แยกkey
for i,(k,v) in enumerate(employee2.items()):
    print(i,k,v)