'''
Dictionary Comprehension
파이썬의 유용한 도구
{ "{}번".format(number):name for number, name in enumerate(students) } # [ 형식 for문 ]
{student:score for student, score in zip(students, scores)}
'''

students=["태연","진우","정현","하늘","성진"]
for number,name in enumerate(students):
    print("{}번의 이름은 {}입니다.".format(number,name))

students_dict={ "{}번".format(number+1) : name   for number,name in enumerate(students) }
print(students_dict)

scores=[85,92,78,90,100]
for x, y in zip(students,scores):
    print(x,y)
'''
태연 85
진우 92
정현 78
하늘 90
성진 100
'''

score_dic={student:score for student,score in zip(students,scores)}
print(score_dic)
#{'태연': 85, '진우': 92, '정현': 78, '하늘': 90, '성진': 100}