#dict act like a map data structure
#they have key value pair
#list, tuple, set etc can't be used as key
#value could be anything
dict={}
print(type(dict))
dict['name']='Big-AI'
dict['age']=1
dict[45]='forty five'
dict['skills']=['Python', 'java','c++',47]
dict['other_details']={'color': 'black', 'city':'rostock', 'country': 'germany'}
# print(len(dict))# length of a dic is number of keys
# print(dict['name'])
# dict['age']=2
# print(dict)

# temp=dict[45]

# print(dict['other_details']['country'])
# print(dict['skills'][3])
# print(dict['other_details'])
dict['45']='fifty'
dict['other_details']['country']='Norway'
dict['other_details']['city']='Oslo'
dict['other_details']['color']='green'
dict['skills'][3]='C sharp'
# print(dict)

# total_keys=dict.keys()
# print(total_keys)
#print(dict.items())


#How to iterate on dict
# for k, v in dict.items():
#      print('key is', k , 'value is', v)

# 'comparision of dictionary'
# dict1={'a':1,'b':2,'c':3}
# dict2={'b':2,'a':1,'c':3}
# print(dict1==dict2)

#deletion of key value pair in dict
del dict['45']
del dict['other_details']
print(dict)
list_of_keys=list(dict.keys())
print(list_of_keys)
if 'name' in list_of_keys:
    print(True)
else:
    print(False)    