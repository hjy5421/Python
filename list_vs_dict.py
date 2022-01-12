#리스트와 딕셔너리의 비교

list=[1, 2, 3, 4, 5]
dict={'one' : 1, 'two' : 2}

print(list[0])
print(dict['one'])


del(list[0])
del(dict['one'])
print(list)
print(dict)


len(list)
len(dict)


print(2 in list) #True
print(7 in list) #False
print('two' in dict.keys()) #True
print('to' in dict.keys()) #False
print(2 in dict.values()) #True
print(32 in dict.values()) #False


dict.clear()
list.clear()


big_list=[1,2,3]+[4,5,6]
dict1={1:100,2:200}
dict2={1:1000,3:3000}
dict1.update(dict2) #{1: 1000, 2: 200, 3: 3000}

dict1={1:100,2:200}
dict2={1:1000,3:3000}
dict2.update(dict1) #{1: 100, 3: 3000, 2: 200}


'''
리스트와 비교

[공통점]
                List	                Dictionary
생성	    list = [ 1, 2 ,3 ]	    dict = { 'one':1, 'two':2 }
호출	    list[ 0 ]	            dict[ 'one' ]
삭제	    del( list[ 0 ] )	    del( dict[ 'one' ] )
개수 확인	len( list )	            len( dict )
값 확인	    2 in list	            'two' in dict.keys( )
전부 삭제	list.clear( )	        dict.clear( )

[차이점]
                    List	                                                    Dictionary
순서	삭제 시 순서가 바뀌기 때문에 인덱스에 대한 값이 바뀐다	    key로 값을 가져오기 때문에 삭제 여부와 상관없다
결합	         list1 + list2	                                              dict1.update( dict2 )
'''