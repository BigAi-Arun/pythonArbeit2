# #how to create lambda function
# lambda_new_function = lambda x:x+5
# y=10
# print(lambda_new_function(y))

# #multiple argument by lambda function
# add_two_number = lambda x,y : x*y

# a=2
# b=5
# print(add_two_number(a,b))

# #write a program to concant two strings

# concat_string= lambda str1, str2 : str1 +str2

# string1=input('write your first name:')
# string2=input('write your second name:')
# print(concat_string(string1,string2))

#calculate maximun of 2 numbers

# max_num = lambda x, y :  x if x>y else y
# a=10
# b=2
# print(max_num(a,b))

# #implememnt map function
# list1=[1,2,3,4,5,6,7,8,9]

# square_num = lambda x:x*x

# square_list=list(map(square_num,list1))
# print(square_list)


#Add sequential respective elements in two given list 
# list1 =[1,2,3,4,5]
# list2=[5,4,3,2,1]

# #result 

# sum_of_2_list= lambda x,y:x+y

# result_list=list(map(sum_of_2_list, list1,list2))
# print(result_list)


#reduce function, we need to use functools library
import functools

# list1=[1,2,3,4,5]
# add_two_number = lambda x,y:x+y
# result= functools.reduce(add_two_number, list1)

# print(result)

# multily_two_num = lambda x,y :x*y
# result1=functools.reduce(multily_two_num,list1)
# print(result1)


#how to use filter()

seq=[1,2,5,6,9,7,10]

filter_odd = lambda x:x% 2 != 0
result2= list(filter(filter_odd, seq))
print(result2)