#function may or may not except input parameter
#function may or may return any output

# def welcome_message():
#     print('welcome to Big-ai')
#     return

# welcome_message()

# def bot_reply():
#     return 'hi , I am BOT'

# print(bot_reply())

# def avg_of_two_nums(a,b):
#     avg_result=(a+b)//2
#     return avg_result

# num1=2
# num2=3
# output=avg_of_two_nums(num1,num2)
# print(output)    

# #writr a function to calculate the factorial of a num
# def factorial_of_num(n):
#     if n==0 or n==1:
#         return 1
#     result=1    
#     for num in range(1, n+1):
#         result=result*num
#     return result

# x=2
# ans=factorial_of_num(x)
# print("factorial of number,",x,"=",ans)

# #how to return multiple values from function
# a, b, c = 2,3,5

# print("value of a is ", a)
# print("value of b is ", b)
# print("value of c is ", c)


# def sqr_and_cube(n):
#     sqr=n*n
#     cube=n*n*n

#     return sqr,cube

# num =3
# sqr_num, cube_num = sqr_and_cube(num)
# print("square of ",num,"is:",sqr_num)    
# print("square of ",num,"is:",cube_num)    

#how to create optional argument in python

# def multiply(a, b=3):
#     result=a*b
#     return result

# num1=5
# num2=10
# print(multiply(num2))

# #optinal argument should be end of function

# def example_nonkeyed_argv(*argv):
#     for param in argv:
#         print(param)

# example_nonkeyed_argv('hello','welcome','to','iNeuron')        

#key valued argument act as dictonary
def example_of_key_value(**kwargs):
    print("Value of host : ", kwargs['host'])
    print("Value of port : ", kwargs['port'])
    print("Value of password : ", kwargs['pswd'])

    for k,v in kwargs.items():
        print("Key is ",k,' and Value is ',v)

example_of_key_value(host='170.80.80.80', port=9021, pswd='XXCG')