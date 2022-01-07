list = [1, 2, 3, 4, 5]
for i,v in enumerate(list):
    print('{}번째 값 : {}'.format(i,v))

for a in enumerate(list): #a는 튜플
    print('{}번째 값 : {}'.format(a[0],a[1]))

#튜플 앞에 '*'는 튜플을 쪼개라는 의미
for a in enumerate(list): #a는 튜플
    print('{}번째 값 : {}'.format(*a))