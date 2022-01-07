'''
리스트
'''
list1=['가위','바위','보']
list2=[37,23,10,33]

print(list1)
print(list2)

list2[0]=0
print(list2[0])
print(list2)


'''
리스트 인덱스 keypoint : 음수 인덱스 가능
'''
#print(list2[4]) -> 오류
print(list2[-1])
print(list2[-3])
print(list2[3])

list2=[1,2,3,4,5,6]
list2.append(7)
print(list2)

list3 = list2 + [8]
print(list3)


'''
리스트 원소 포함여부 : in
'''
n=12
ownership = n in list3
print(ownership)

n=10
if n in list3:
    print('{}은 있어'.format(n))


'''
리스트 원소 삭제
'''
list4=list2+list3
del(list4[12])
print(list4)

list4.remove(3) #같은 값이 여러개 존재하면 제일 첫번째 값이 삭제됨
print(list4)

list4.pop(0) #0은 인덱스
print(list4)