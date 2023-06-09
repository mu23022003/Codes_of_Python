### class

'''
class Snake:
    # Snake main blueprint
    name = "Anaconda"

    # Mothod to chnge name
    def modifyName(self, new_name):
        self.name = new_name


# Objects based on Snake

snake01 = Snake()
# printing on screen
print(snake01.name)

#Modify the name using modifyName

snake01.modifyName("Python")
print(snake01.name)
'''

'''
class Snake:
    def __init__(self, name):
        self.name = name

    def modifyName(self, newName):
        self.name = newName


# Object

anaconda1 = Snake("Anaconda")
python1 = Snake("Python")

print(anaconda1.name)
print(python1.name)
'''

'''
class Person:
    def __init__(self, name, age, personID):
        self.name = name
        self.age = age
        self.personID = personID

person1 = Person("Mukesh", 12, 21)
person2 = Person("Messi", 35 , 10)
person3 = Person("Neymar", 29,11)
print(person1.name)
print(person1.age)
print(person1.personID)

print(person2.name)
print(person2.age)
print(person2.personID)

print(person3.name)
print(person3.age)
print(person3.personID)

'''

'''

class Person:
    def __init__(self , name , age , personID):
        self.name = name
        self.age = age
        self.personID = personID

    def display_data(self):
        print("Hi my name is " , self.name , "my age is " , self.age
              , "and my personId is " , self.personID)

person1 = Person("santosh", 13,21)
person2 = Person("Roshan" , 14,22)
person3 = Person("Abishek" , 15,52)

person1.display_data()
person2.display_data()
person3.display_data()

'''

'''
class Product:
    def __init__(self, product_name, brand_name, model_name, price):
        self.product_name = product_name
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = model_name


laptop = Product('Laptop', 'Dell', 'm4800', 54000)
mobile = Product('Mobile', 'Samsung', 'A7', 50000)

print(laptop.model_name())
'''

'''
class Product:
    def __init__(self, product_name, brand_name, model_name, price):
        self.product_name = product_name
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.productNameWithModel = product_name + ' ' + model_name



laptop = Product("Laptop", "Dell", "m4500", 54000)
mobile = Product("Mobile", "Samsung", "Akkm4", 50000)
print(mobile.price)
print(laptop.productNameWithModel)
print(laptop.model_name)
'''

# Methods

'''
class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def result(self):
        if self.marks > 500 :
            return 'Pass'
        else:
            return 'Fail'

s1 = Student('Mohail', 24, 500)
print(s1.name)
print(s1.result())
'''

# Method Example
'''
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def result(self):
        if self.marks >= 500:
            return 'Pass'
        else:
            return "Fail"


s1 = Student('Santosh', 21, 600)
s2 = Student('Roshan', 22, 570)
s3 = Student('Rajesh', 21, 500)
s4 = Student('Abishek', 23, 560)
s5 = Student('Rohit', 24, 400)

student_object = [s1, s2, s3, s4, s5]

passStudents = []
failStudents = []
student_result = {} # 
for x in student_object:
    if x.result() == 'Pass':
        passStudents.append(x.name)
        student_result['Pass student'] = passStudents
    else:
        failStudents.append(x.name)
        student_result['Fail student  '] = failStudents

print(student_result)
'''

'''
class Product:
    def __init__(self, productName, price):
        self.productName = productName
        self.price = price

    def discount(self, discountvalue):
        discountAmount = (self.price / 100) * discountvalue
        final_price = self.price - discountAmount
        return final_price


laptop = Product("Laptop", 45000)
print(laptop.discount(15))
'''

# Class Virable
'''
class Circle:
    pai = 3.14

    def __init__(self, radius):
        self.radius = radius

    def circle_circumference(self):
        value_of_circle_circumfernce = 2 * Circle.pai * self.radius
        return value_of_circle_circumfernce

    def area(self):
        area = Circle.pai * self.radius ** 2
        return area


c1 = Circle(23)


c2 = Circle(43)

c1.circle_circumference()
c2.area()
print(c2.area())
'''

# Object Techinques
'''
class Laptop:
    def __init__(self, name, price):
        self.name = name
        self.price = price


m3400 = Laptop('m3400', 45600)
m4500 = Laptop('m4500', 55000)

print(m3400.__dict__)
print(m4500.__dict__)

'''

'''
class Laptop:
    discount = 10

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def applydiscount(self):
        discount_amount = (self.price / 100) * Laptop.discount
        finalAmount = self.price - discount_amount
        return finalAmount


m4500 = Laptop('m4500', 54000)
m5400 = Laptop('m5400', 55000)

print(m4500.__dict__)

print(m5400.applydiscount())

m4500.discount = 5
print(m4500.applydiscount())
print(m4500.__dict__)

m5400.applydiscount()
print(m5400.applydiscount())
'''

# Sovling problem
'''
class Phone:
    def __int__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.completeSpacification = f"{self.brand} {self.model_name} and price is {self.price}"

        @staticmethod
        def make_a_call(phone_num):
            print(f"calling {phone_num}...")

        def full_name(self):
            return f"{self.brand} {self.model_name}"


phone1 = Phone('Nokia', '1100', 5000)

phone1.name
'''
'''
class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name

        #if price > 0:
         #   self.price = price
        #else:
         #   self.price = 0

        # second method of solving negetive price

        self.price = max(price,0)

       # self.completeSpecification = f"{self.brand} {self.model_name} and price is {self.price}"

    def completeSpacefication(self):    # create a funtion for continusly update our  price
        return f"{self.brand} {self.model_name} and price is {self.price}"

    @staticmethod
    def male_a_call(phone_num):
        print(f"calling {phone_num}...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


# phone1= Phone('Nokia' , '1100' , 5000)
phone1 = Phone('Nokia', '1100', 3000)

print(phone1.price)  # still showing price in #negative
print(phone1.model_name)
print(phone1.brand)
phone1.price = 2000
print(phone1.price)

phone1.completeSpacefication()  # it's solving problem of not update price at run time but doing this we can solve this problem
print(phone1.completeSpacefication())/
'''

'''
class Laptop:
    discount = 10  # class variable
    def __init__(self , name , price):
        self.name = name # class Attribute
        self.price = price

    #my laptop name is m6600 and price is 60000

    @classmethod
    def for_string(clr,string):
        import re
        item = re.findall('is \w' , string)
        name = item[0][3:]
        price = item[1][3:]
        return clr(name,int(price))

    def applydiscoun(self):
        discountAmount = (self.price/100)*self.discount
        final_amount = self.price - discountAmount
        return int(final_amount)


m6600 = Laptop('m6600' , 50000)

print(m6600.__dict__)

m6600.applydiscoun()
print(m6600.applydiscoun())

m6600 = Laptop.for_string("my laptop name is m6600 and price is 60000")

m6600.discount = 5
m6600.__dict__
print(m6600.__dict__)

print(m6600)


'''

'''
# Static Method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def printstatement():
        print("this is a static statemnt")


s1 = Student('Santosh', 22)
print(s1.name)
print(s1.__dict__)

print(s1.printstatement())

'''
'''
class Date:          #class 
    def __init__(self , years,month,day):    #constructor/init method
        self.years = years
        self.month = month
        self.day = day

    def arrange_value_into_Date(self):          # Why instance method ane how do we know
                                                # bcz its only passes self parameter  
        date = str(self.day) + '-' + str(self.month) + '-' + str(self.years)
        return date

date1 = Date(2023,6,18)

date1.__dict__
print(date1.__dict__)

date1.arrange_value_into_Date()
print(date1.arrange_value_into_Date())

'''

# Second method
'''
class Date:
    def __init__(self ,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def arrange_value_into_Date_patterrn(self):
        date = str(self.day)  + '-' + str(self.month) + '-' + str(self.year)
        return date

    @classmethod
    def getDatafromString(cls,string):
        import re
        data = re.findall('\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}')
        list_data = data.replace('/' , '-').split('-')
        date = list_data[0]
        date = list_data[1]
        date = list_data[2]
        return cls(year,month,date)


date1 = Date(2022,6,18)
#date1.__dict__
#print(date1.__dict__)

date2 = Date.getDataformString("today date is 17-05-20")

date2.__dict__
print(date2.__dict__)
# rregular expression
'''
'''
import re

pattern = r'apple'
text = 'I love eating apples.'

result = re.search(pattern, text)
if result:
    print('Pattern found!')
else:
    print('Pattern not found!')
'''

'''
import re

pattern = r'\d+'
text = 'I have 5 apples and 3 bananas.'

matches = re.findall(pattern, text)
print(matches)
'''
'''
import re

pattern = r'apple'
replacement = 'orange'
text = 'I love eating apples.'

new_text = re.sub(pattern, replacement, text)
print(new_text)
'''

'''
import re

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def arrange_value_into_Date_pattern(self):
        date = f"{self.day}-{self.month}-{self.year}"
        return date

    @classmethod
    def getDatafromString(cls, string):
        data = re.findall(r'\d{2}-\d{2}-\d{2}|\d{2}/\d{2}/\d{2}', string)
        list_data = data[0].replace('/', '-').split('-')
        day, month, year = list_data[0], list_data[1], list_data[2]
        return cls(year, month, day)


date2 = Date.getDatafromString("today is 18-02-22")
arranged_date = date2.arrange_value_into_Date_pattern()
print(arranged_date)
print(date2.__dict__)
'''

# Static  Method Excerise
'''

import re

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def arrange_value_into_Date_pattern(self):
        date = f"{self.day}-{self.month}-{self.year}"
        return date

    @classmethod
    def getDatafromString(cls, string):
        data = re.findall(r'\d{2}-\d{2}-\d{2}|\d{2}/\d{2}/\d{2}', string)
        list_data = data[0].replace('/', '-').split('-')
        day, month, year = list_data[0], list_data[1], list_data[2]
        return cls(year, month, day)

    @staticmethod
    def setDatePattern(string):
        list1 = string.replace('/' , '-').split('-')
        date_update = list1[2] + '-' + list1[1] + '-' + list1[0]
        return date_update

date2 = Date.getDatafromString("today is 18-02-22")
arranged_date = date2.arrange_value_into_Date_pattern()
print(arranged_date)
print(date2.__dict__)

date3 = Date.setDatePattern("today date is 12-02-22")
print(date3)
'''


# Inheritance
# Example of Inheritance

# Parent Class

class Vechile:
    def Vechile_data(self):
        print("Hello from the vechile class")


# Child Class

class Car(Vechile):
    def Car_data(self):
        print("Hello from the Car class ")


# Objects based of car
car01 = Car()

# Get vechile data

car01.Vechile_data()
car01.Car_data()

# Two child class example of inheritance


'''
class Vechile:
    def Vechile_data(self):
        print("Hello from the Vechile class")


#Car Child class

class Car(Vechile):
    def Car_data(self):
        print("Hello from the Car Class")

#Bike child class


class Bike(Vechile):
    def Bike_data(self):
        print("Hello from bike class")

#object based on Car
car01 = Car()
bike01 = Bike()

#GEt Vechile data

car01.Vechile_data()
car01.Car_data()
#

print("===================")


#
bike01.Vechile_data()
bike01.Bike_data()
'''

'''


# Multiple inheritanc elike Two Parents

class Person:
    def Person_data(self ,name,age):
        print("Hello from the Person class")
        print("the name is:" , name,"and the age is:" , age)

#Comanpy parent class

class Company:
    def company_data(self,comp_name , location):
        print("Welcome to the company")
        print("the company name is:" , comp_name , "and location is:" , location)

#Employee child class

class Employee(Person , Company):
    def employee_data(self,salary,skill):
        print("welcom to the employee class")
        print("Salary is:" , salary,"skill is:",skill)


#object for employee
emp01 = Employee()


#Get data on screen
emp01.Person_data("Messi" , 35)

emp01.company_data("ANSC" , "Location343")
emp01.employee_data("100000" , "programmer")

'''

# Encapsulation
# a) Public method
# b) Private Method
# c) Protected Method

'''
class Employee:
    # class Constructor
    def __init__(self, name, salary, project):
        self.name = name
        self.project = project
        self.salary = salary

        # shoe the employee data
        def show_details(self):
            print("the name is:", self.name, "and salary is: ", self.salary)

        # working project
        def work(self):
            print(self.name, "is working on", self.project)


# object for employee

employee01 = Employee("Messi", 90000000, "Video Game")


# call the public method for details

employee01.work()
employee01.show_details()
'''

# using Private Member

'''
class Employee:
    def __init__(self, name, salary, project):
        self.__name = name
        self.salary = salary
        self.project = project

    def show_details(self):
        print("The name is :", self.__name, "and Salary is", self.salary)

    def work(self):
        print(self.__name, " is working on", self.project)


employee01 = Employee("Marcelo", 90000, "Video Game")

#print("The Value of name is" , employee01.__name)  # u can't just call private method like this
employee01.show_details()   # doing this u can call it
employee01.work()

'''


# Protected data using getter and setters

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private memberr

    # getting age
    def get_age(self):
        return self.__age

    # setting age
    def set_age(self, age=None):
        self.__age = age


person01 = Person("Messi", 35)

# print("Name: ", person01.name, "age: ", person01.get_age())


# Modify age
person01.set_age(36)
print("Name: ", person01.name, "age: ", person01.get_age())

# Polymorphism

# Apply Polymorphism using differne tpolymorphic function


# Using Polymorphic build-in function

print(len("Anaconda"))
print(len([5, 15, 20, 25]))


# Using Polymorphic User_deffined Functions

def add(x, y, z=0):
    return x + y + z


print(add(5, 7))  # 12 there is z value is 0
print(add(5, 7, 9))  # 21  there z value is 9

# Polymorphism with Inheritance and Method Overriding in action

'''
class Bird:
    def intro(self):
        print("Hi , there are many types of birds!")

    def flight(self):
        print("Most of birds can fly but some cannot!")

    # Sparrow child class
class Sparrow(Bird):
    def flight(self):
        print("Sparrow can fly in the sky")

    #Ostrich child class

class Ostrich(Bird):
    def flight(self):
        print("Orstrich cannot fly ")

#objects

bird01 =  Bird()
sparrow01 = Sparrow()
ostrich1 = Ostrich()

#call intro and flight

bird01.intro()
bird01.flight()

sparrow01.intro()
sparrow01.flight()

ostrich1.intro()
ostrich1.flight()
'''

# Abstraction & Encapsulation


'''
class Phone:
    def __init__(self , brand , model_name , price):
        self.brand = brand
        self.model_name =  model_name
        self.price = price
    @staticmethod
    def make_a_call(phone_num):
        print(f"calling  {phone_num}.....")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


phone01 = Phone('Nokia' , 'Nh45' , 23000)

print(phone01.__dict__)
phone01.make_a_call('954938593')
print(phone01.make_a_call())
'''

# Inheritance

'''
class Phone:
    def __init__(self , brand , model_name , price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    @staticmethod
    def make_a_call(phone_num):
        print(f"calling {phone_num}")

    def full_name(self):
        print(f"{self.brand} {self.model_name}")

phone01 = Phone('Nokia' , 'Nh23', 45000)



class SmartPhone(Phone):
    def __init__(self , brand,model_name,price,ram,interanl_memory,rare_camera):
        phone01.__init__(self,brand , model_name , price)
        self.ram = ram
        self.internal_memory = interanl_memory
        self.rare_camera = rare_camera



Phone01 = Phone("Nokia" , '1000' , 56000)

Phone01.price
print(Phone01.price)

Phone01.full_name()
print(Phone01.full_name)

SmartPhone01 = SmartPhone('Samsumg' , 'A7' , 60000 , '4000' , '128GB' , '25MP')

SmartPhone01.rare_camera
print(SmartPhone01.rare_camera)

'''

'''
class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    @staticmethod
    def make_a_call(phone_num):
        print(f"Calling {phone_num}")

    def full_name(self):
        print(f"{self.brand} {self.model_name}")


phone01 = Phone('Nokia', 'Nh23', 45000)
Phone.make_a_call("1234567890")  # calling 1234567890
phone01.full_name()  # Nokia Nh23


class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model_name, price)  # this is a common way to do it  
        
        #Phone.__init__(self,brand,model_name,price)   We can do this way but this way is very uncommon   
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera


Phone01 = Phone("Nokia", '1000', 56000)

print(Phone01.price)  # 56000

Phone01.full_name()  # Nokia 1000


SmartPhone01 = SmartPhone('Samsung', 'A7', 60000, '4000', '128GB', '25MP')

print(SmartPhone01.rear_camera)  # 25MP

'''

'''
class Phone:
    def __int__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    def make_a_call(phone_num):
        print(f" calling {phone_num}")

    def full_name(self):
        return  f"{self.brand} {self.model_name}"



class SmartPhone(Phone):
    def __init__(self, brand,price,model_name , ram,rear_camera , interanl_memory):
        super.__init__(self,brand,model_name,price)
        self.ram = ram
        self.rear_camera = rear_camera
        self.interanl_memory = interanl_memory



class FlagShip(SmartPhone):
    def __int__(self , brand, price,model_name,ram,rear_camera,front_camera):
        super.__init__(brand,price,model_name,ram,rear_camera)
        self.front_camera = front_camera


SmartPhone2 = SmartPhone('Samsung', 60000,'ak54' , '4GB' '45MP' ,   '25MP' , '125GB')

SmartPhone2.full_name()
print(SmartPhone2.full_name())

'''


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    def make_a_call(self, phone_num):
        print(f"Calling {phone_num}")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


'''
class SmartPhone(Phone):
    def __init__(self, brand, price, model_name, ram, rear_camera, internal_memory):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.rear_camera = rear_camera
        self.internal_memory = internal_memory


class FlagShip(SmartPhone):
    def __init__(self, brand, price, model_name, ram, rear_camera, front_camera):
        super().__init__(brand, price, model_name, ram, rear_camera)
        self.front_camera = front_camera


smartphone2 = SmartPhone('Samsung', 60000, 'ak54', '4GB', '45MP', '125GB')
print(smartphone2.full_name())

flagship1 = FlagShip('Samsung', 60000, 'ak54', '4GB', '45MP', '125GB' , '34MP')

print(flagship1.full_name())
print(flagship1.ram())
'''

'''

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    def make_a_call(self, phone_num):
        print(f"Calling {phone_num}")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


class SmartPhone(Phone):
    def __init__(self, brand, price, model_name, ram, rear_camera, internal_memory):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.rear_camera = rear_camera
        self.internal_memory = internal_memory

    def full_name(self):
        return f"{self.brand} {self.model_name}"


class FlagShip(SmartPhone):
    def __init__(self, brand, price, model_name, ram, rear_camera, front_camera):
        super().__init__(brand, price, model_name, ram, rear_camera, None)
        self.front_camera = front_camera

    def full_name(self):
        return f"{self.brand} {self.model_name}"


smartphone2 = SmartPhone('Samsung', 60000, 'ak54', '4GB', '45MP', '125GB')
print(smartphone2.full_name())

flagship1 = FlagShip('Samsung', 60000, 'ak54', '4GB', '45MP', '34MP')
print(flagship1.full_name())
print(flagship1.ram)

'''


# Multiple Inhertance part2


class A:
    def class_a_method(self):
        return 'I am just a class A method'

    def helo(self):
        return 'helo from class A'


class B:
    def class_b_method(self):
        return 'I am just a class B method'

    def helo(self):
        return 'Helo from Class B'


class C(A, B):
    pass


intanceA = A()
intanceA.class_a_method()
print(intanceA.class_a_method())

intanceB = B()
intanceB.class_b_method()
print(intanceB.class_b_method())

intanceC = C()
intanceC.helo()
print(intanceC.helo())

help(intanceC)

# Method resolution order:
# |      C
# |      A
# |      B
# |      builtins.object
# in order to change that resoultion order we need to do

# class(B,A) like this

# c.mro()  # with the help of that u find the order just like help()


# isinstance() method

# it is used for to know the class is inherit or not

# Example

# isinstance(flagship , Smartphone)
# isinstance(phone01, Phone)


# issubclass() method is used to know the is sub class or not

# example

# issubclass(Flagship,Smartphone)


# Private
# Public

# in Python Everthing is public

'''
class Phone:
    def __init__(self , brand ,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self._discount = 5

    def apply_discount(self):
        discounted = (self.price/100)*self._discount
        final_price = self.price - self._discount
        return final_price

phone1 = Phone('Nokia' , '1600' , 3000)

phone1.__dict__
print(phone1.__dict__)

phone1.apply_discount()
print(phone1.apply_discount())

phone1.apply_discount = 2
phone1.__dict__
print(phone1.__dict__)

# why we using _discount like this
#it's not like that python rules or something its just use by professional developer for convetion


'''

# Name Mangling
'''
class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.__price = price  #NAme Mangling
        self._discount = 5

    def apply_discount(self):
        discounted = {self.price/100}*self._discount
        final_price = self.price - discounted
        return final_price

Phone01 = Phone('Nokia' , '1100' , 4000)

Phone01.__dict__
print(Phone01.__dict__)

Phone01._Phone__price
print(Phone01._Phone__price)
'''


# Dunder or Magic method
'''
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.model} , {self.price} , {self.brand}"

   # def __repr__(self):
    #    return f"{self.price} {self.brand}"

    def __repr__(self):
        return f"Phone(\'{self.model}\',\'{self.price})"

# print(phone01) # by using the print command its show us a  memory location <__main__.Phone object at 0x0000017C66E146D0>

# if u want to create a dunder method then create this way


# __name__   # dunder Method / Magic Method
# _Name private variable


phone01 = Phone('Nokia', 'A3400', 4000)
#print(str(phone01))


#print(phone01)  #Now using dunder method its print by using this method


#str and repr showing same result then why we using both different different?

# bcz str is use to show some result ot our user in a well formatted manner when we use str method
# when we use repr method we want to show the developer


#print(phone01.__str__())
'''

'''
# Method Overloading

class Phone:
    def __int__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def __add__(self, other):
         return self.price + other.price

    def __sub__(self, other):
         return  self.price - other.price

     def __mul__(self, other):
         return self.price * other.price

phone01 = Phone('Nokia' , 'Akef345' , 5000)

phone02 = Phone('Nokia' , 'Ad4500' , 7000)


phone01.__dict__
print(phone01.__dict__)
phone02.__dict__
print(phone02.__dict__)

phone02 * phone01
print(phone02 * phone01)
'''


# Polymorphism

class Phone:
    def __int__(self , brand ,model_name , price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price , 0)

    def full_name(self):
        return f"{self.price} {self.model_name}"

    def __add__(self, other):
        return f"{self.brand} {self.model_name} " + f"{other.brand} {other.model_name}"


class SmartPhone(Phone):
    def __int__(self,brand,model_name,price,ram,internal_memory , rare_camera):
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rare_camera = rare_camera

    def __add__(self, other):
        return self.price + other.price

class FlagShip(SmartPhone):
    def __init__(self , brand ,model_name,price,ram,internal_memory,rare_camera,front_camera):
        super().__init__( brand,model_name,price,ram,internal_memory,rare_camera)
        self.front_camera = front_camera

    def __add__(self, other):
        return self.rare_camera + other.rare_camera

Phone1 = Phone('Nokia' , 'sk100' , 4500)

SmartPhone1 = SmartPhone('Samsung' , 'A6' ,5600,'4GB' , '139GB' , '34MP')

FlagShip1 = FlagShip('Samsung', 'A4' , 7000 , '4GB' , '123GB' , '34MP' , '12MP')
FlagShip2 = FlagShip('Samsung' 'A7' , 4600 , '6GB' , '128GB' , '45MP', '23MP')

FlagShip1 + FlagShip1
print(FlagShip1 + FlagShip2)