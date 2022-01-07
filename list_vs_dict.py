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
dict2.update(dict1)
print(dict2)

