#조건문

if 3<5:
    print("조건식이 True이므로 실행됩니다.")
if 3>5:
    print("조건식이 False이므로 실행되지 않습니다.")


if True:
    print("조건식이 True이므로 실행됩니다.")
if False:
    print("조건식이 False이므로 실행되지 않습니다.")

#현재시간이 오전인지 확인합니다.
from datetime import datetime 
hour = datetime.now().hour
if hour<12:
    print('오전입니다.')

#number가 3의 배수인지 확인합니다.
number = 15
if number % 3 == 0: 
    print("{}는 3의 배수입니다.".format(number))


