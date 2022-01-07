#딕셔너리
#딕셔너리 key : 문자열, 숫자형, 튜플 가능
#딕셔너리 value : 어떤 자료형이든 가능 / 문자열, 숫자형, 튜플, 리스트 등등

wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
}

print(wintable['가위'])

def rsp(mine, yours):
    if mine==yours:
        return 'draw'
    elif wintable[mine]==yours:
        return 'win'
    else:
        return 'lose'

result=rsp('가위','바위')
print(result)

messages={
    'win':'이겼다',
    'lose':'졌다',
    'draw':'비겼다'
}
print(messages[rsp('가위','바위')])
print(messages[result])


dict={
    'one':1,
    'two':2
}

'''
딕셔너리 수정
'''
dict['one']=11
print(dict)


'''
딕셔너리 추가
'''
dict['three']=3
print(dict)


'''
딕셔너리 삭제
'''
del(dict['one'])
print(dict)
dict.pop('two')
print(dict)


ages={'Tod':35,'Jane':38,'Paul':50}
print(ages)

for key in ages.keys():
    print(key)

for value in ages.values():
    print(value)

for key in ages.keys():
    print('{}의 나이는 {}'.format(key, ages[key]))

for key in ages:
    print('{}의 나이는 {}'.format(key, ages[key]))

#list의 enumerate와 같은 함수
for key, value in ages.items():
    print('{}의 나이는 {}'.format(key, value))
