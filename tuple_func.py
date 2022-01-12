list = [1, 2, 3, 4, 5]
for i,v in enumerate(list):
    print('{}번째 값 : {}'.format(i,v))

for a in enumerate(list): #a는 튜플
    print('{}번째 값 : {}'.format(a[0],a[1]))

#튜플 앞에 '*'는 튜플을 쪼개라는 의미
for a in enumerate(list): #a는 튜플
    print('{}번째 값 : {}'.format(*a))



ages={'Tod':35,'Jane':38,'Paul':50}
for key,val in ages.items():
    print('{}의 나이는 {}'.format(key, val))

for a in ages.items():
    print('{}의 나이는 {}'.format(a[0], a[1]))

for a in ages.items():
    print('{}의 나이는 {}'.format(*a))