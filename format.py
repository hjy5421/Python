number=20
greeting='안녕하세요'
welcome='환영합니다'

#old way
print(number,'손님 ', greeting)
base='{}번 손님, {}'
new_way=base.format(number, greeting)

print(base)
print(new_way)