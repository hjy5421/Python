list=[1, 2, 3, 4, 5]
dict={ 1 : 'one', 2 : 'two'}

#tuple
#값의 변경이 불가능한 list
#1. 한번 정해진 순서 바꿀 수 없음
#2. 값의 변경과 삭제 불가능
tuple1=(1, 2, 3)
tuple2=1, 2, 3
print(type(tuple1)) #tuple
print(type(tuple2)) #tuple

tuple3=tuple(list)
print(tuple3[0]) # 1
print(tuple3[1]) # 2


#packing, unpacking
#packing : 하나의 변수에 여러개의 값을 넣는 것
#unpacking : 패킹된 변수에서 여러개의 값을 꺼내오는 것
a, b= 1, 2
# tuple1=(a,b)  /  tuple2=(1,2)
# 서로 대입된 것
print(a) # 1 
print(b) # 2


#unpacking
c=(3,4)
d,e=c
print(c) # (3, 4)
print(d) # 3
print(e) # 4

#packing
f=d,e
print(f) # (3, 4)


x=5
y=10
# x와 y의 값을 교환하려면?
# 원래의 방법
'''
tmp=x
x=y
y=tmp
'''

x,y=y,x
print(x)
print(y)


def tuple_func():
    return 1,2
q,w=tuple_func()
print(q) # 1
print(w) # 2




