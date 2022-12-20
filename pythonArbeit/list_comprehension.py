#program to create list 

# result=[]
# for num in range(1,11):
#     result.append(num)

# print(result)

# #same lsit by list comprehension
# result = [x for x in range(1,11)]
# print(result)

# #geta lsit of all even number
# list_a=[1,2,3,4,5,6,7,8,9,10,11,12]
# result =[x for x in range(1,11) if x%2==0]
# print(result)

#covert all alsit upper case
list=['hi','hello','bye','nice']
result=[x.upper() for x in list]
print(result)

#convert all +ve number after -ve number
list_a=[1,-1,2,-5,9,10,-6]
result_a=[x for x in list_a if x>=0 ] + [x for x in list_a if x<0]

print(result_a)