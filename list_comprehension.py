'''
List Comprehension
파이썬의 유용한 도구
예1 [ i*i for i in range(1,11) ] # [ 계산식 for문 ]
예2 [ i*i for i in range(1,11) if i % 2 == 0 ] # [ 계산식 for문 조건문 ]
예3 [ ( x, y ) for x in range(15) for y in range(15) ] # [ 계산식 for문 for문 ]
'''

areas=[]
for i in range(1,11):
    areas=areas+[i*i]
print(areas)
#[1,4,9,16,25,36,49,64,81,100]

areas2=[ i*i for i in range(1,11)]
print(areas2)
#[1,4,9,16,25,36,49,64,81,100]


areas=[]
for i in range(1,11):
    if i%2==0:
        areas=areas+[i*i]
print(areas)
#[4,16,36,64,100]

areas2=[ i*i for i in range(1,11) if i%2==0]
print(areas2)
#[4,16,36,64,100]


areas2=[(x,y) for x in range(15) for y in range(15)]
print(areas2)