#bool
#숫자 0을 제외한 모든 수 - true
#빈 딕셔너리, 빈 리스트를 제외한 모든 딕셔너리, 리스트 - true
#아무 값도 없다는 의미인 None - false
#빈문자열을 제외한 모든 문자열 - true

bool(0) # False
bool(1) # True
bool(-1) # True
bool(-1234 ) # True

bool([]) # False
bool([3]) # True
bool(None) # False

bool('') # False
bool('hi') # True


if 'Hi':
    print('Hello') #Hello

if '':
    print('Hello')