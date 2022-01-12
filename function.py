def function():
    print('안녕 함수')

function()

def print_round(number):
    rounded=round(number)
    print(rounded)

print_round(4.6)
print_round(2.2)

def add_10(value):
    result=value+10
    return result

n=add_10(10)
print(n)


def print_sum_diff(a,b):
    sum=a+b
    diff=a-b
    return sum,diff

sum,diff=print_sum_diff(20,10)
