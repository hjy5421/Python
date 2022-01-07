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
