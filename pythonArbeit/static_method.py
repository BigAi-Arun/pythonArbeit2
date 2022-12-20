#what is static Method in Python
class Car:
    def __init__(self, name, color):
        self.car_name = name
        self.car_color = color


    def displayCarDetails(self):
         print("car name is", self.car_name, "and Car color is",self.car_color)

    @staticmethod
    def initialMessage():
        print("Nice Car...!!!!")


# Car.initialMessage()
# car1= Car('XUV','white')
# car1.displayCarDetails()
# print(car1.car_name)
# Car.displayCarDetails()

#I neuron
class employee:
    @staticmethod
    def isEmployeeof():
        print("I am an Employee of iNeuron")

employee.isEmployeeof()        


#class with static function with argument variable
class calculation:
    @staticmethod
    def addTwonums(num1,num2):
        print("sum of two numbers=",num1 +num2)

calculation.addTwonums(2,3)        