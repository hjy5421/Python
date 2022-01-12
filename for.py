#for in list

#리스트 patterns의 값을 하나씩 꺼내 pattern으로 전달
patterns=['가위','바위','보','가위','바위','보']
for pattern in patterns:
    print(pattern)


#for in range
for i in [0,1,2,3,4]:
    print(i)

for i in range(10):
    print(i)

names=['영수','영희','바둑이','철수']
for i in range(4):
    name=names[i]
    print('{}번 : {}'.format(i,name))

'''
range 함수
: 필요한 만큼의 숫자를 만들어내는 유용한 기능
'''
names=['영수','영희','바둑이','철수','종수']
for i in range(len(names)):
    name=names[i]
    print('{}번 : {}'.format(i,name))

'''
enumerate
: 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
'''
for i, name in enumerate(names):
    print('{}번 : {}'.format(i,name))