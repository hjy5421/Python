#리스트 더 알아보기
'''
list.index( value ) : 값을 이용하여 위치를 찾는 기능
list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가
list.insert( index, value ) : 원하는 위치에 값을 추가
list.sort( ) : 값을 순서대로 정렬
list.reverse( ) : 값을 역순으로 정렬
'''

list1=[135,462,27,2753,234]
list1.index(27) # 2
#list1.index(50) #Value Error
if 50 in list1:
    list1.index(50)

list2=[1,2,3]+[4,5,6]
list1.extend([9,10,11])
# [135,462,27,2753,234,9,10,11]

list1.insert(2,999)
# [135,462,999,27,2753,234,9,10,11]

list1.insert(-1,9999)
# [135,462,999,27,2753,234,9,10,9999,11]

list1.insert(10000,555)
# [135,462,999,27,2753,234,9,10,9999,11,555]
# 존재하지 않는 인덱스 넣으면 가장 끝에 insert

list1.sort()
#[9,10,11,27,135,234,462,555,999,2753,9999]

list1.reverse()
#[9999,2753,999,555,462,234,135,27,11,10,9]



'''
list = str.split( ) : 문자열에서 리스트로
" ".join( list ) : 리스트에서 문자열으로
'''
my_list=[1,2,3,4,5]
my_list[1] # 2

str="Hello World"
str[1] # e

3 in my_list # True
"H" in str #True
"z" in str #False

my_list.index(5) # 4
str.index("r") #8

characters=list("abcdef")
characters #['a','b','c','d','e','f']
words="Hello world는 프로그래밍을 배우기에 아주 좋은 사이트입니다."
words_list=words.split()
print(words_list) 
#['Hello', 'world는', '프로그래밍을', '배우기에', '아주', '좋은', '사이트입니다.']

time_str="10:35:27"
time_list=time_str.split(":")
print(time_list) # ['10', '35', '27']
":".join(time_list) # "10:35:27"
" ".join(words_list) # "Hello world는 프로그래밍을 배우기에 아주 좋은 사이트입니다."



'''
slicing : 리스트나 문자열에서 값을 여러개 가져오는 기능
- slice를 하면 해당하는 부분의 리스트나 문자열을 새로 만들어 준다.
- list[ 2: ] : 2번째부터 끝까지 반환
- list[ : 2 ] : 처음부터 2번째 까지 반환
- list[ : ] : 처음부터 끝까지 전부 반환
'''
list=[1,2,3,4,5]
text="hello world"
text[1:5] 
#ello #인덱스 1~4까지 가져옴
list[1:3]
#[2,3]
list[2:len(list)]
list[:2] #[1,2]
list[2:] #[3,4,5]
list[:] #[1,2,3,4,5]
#slice는 기존의 list를 복사해서 새로운 list 만듦

list1=[11,12,13,14,15]
list2=list[:] #[11,12,13,14,15] 



'''
step : slice한 값의 범위에서 step 값을 주어 그 값만큼 건너뛰어 가져오는 기능
list[ 시작값:끝값:step ]
'''
list1=list(range(20))
list1[5:15] #[5,6,7,8,9,10,11,12,13,14]
list1[5:15:2] #[5,7,9,11,13] #하나 건너서 가져옴
list1[5:15:3] #[5,8,11,14]
list1[5:15:-1] #5부터 -1해서는 15가 될 수 없음
list1[15:5:-1] #[15,14,13,12,11,10,9,8,7,6]
list1[14:4:-1] #[14,13,12,11,10,9,8,7,6,5]
list1[::3] #[0,3,6,9,12,15,18]
list1[::-3] #[19,16,13,10,7,4,1]


'''
slice 활용
- 삭제
del list[ :5 ] : 처음부터 5번째까지 삭제
- 수정
list[ 1:3 ] = [ 77, 88 ]
list[ 1:3 ] = [ 77, 88 ,99 ] : 더 많은 개수로 변환
list[ 1:4 ] = [ 8 ] : 더 적은 개수로 변환
'''
numbers=list(range(10))
del numbers[0]
#[1,2,3,4,5,6,7,8,9]
del numbers[:5]
#[6,7,8,9]
numbers[1:3] #[7,8]
numbers[1:3]=[77,88]
#[6,77,88,9]
numbers[1:3]=[77,88,99]
#[6,77,88,99,9]
numbers[1:4] #[77,88,99]
#numbers[1:4]=8 #TypeError
numbers[1:4]=[8]
#[6,8,9]