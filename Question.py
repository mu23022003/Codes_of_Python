#1

name = "John Dow"
print(name)

#2

pi = 3.15
print(type(pi))
#3
name = "Johan Doe"
print(type(name))
#4
num1 = 10
num2 = 5
sum = num1 + num2
print("result: " , sum)
#5

is_raining = True
print(type(is_raining))

#6
my_list = [ 1 ,3 ,2]
print(my_list)
print(type(my_list))

#8
my_tuple = (1,2,3,4)
print(tuple)

print(type(my_tuple))

#9
result = None
print(result)
print(type(result))

#10
is_even = 6
print(is_even)
print(type(is_even))

if is_even/2:
    print("its even")
else:
    print("Odd")



#11

my_dict = {
    "John" : 25,
    "Jane" : 22,
    "Jonny" : 30
}
print(my_dict)
print(type(my_dict))


#12

#Name = str(input("Enter Your Name :"))

#Age = int(input("Enter Your Age :"))

#Color = str(input("Enter your color:"))

#print(Name , Age , Color)


#13

Length_of_Rectangle = int(input("Enter the length of the rectangle: \n"))
Width_of_Rectangle = int(input("Enter the Width of the rectangle: \n"))

Area_of_Rectangle = (Length_of_Rectangle * Width_of_Rectangle)
print("Area of Rectangle : " , Area_of_Rectangle)


pi = 3.14
radius = int(input("Enter a Circle of Radius : "))
Area_of_Circle = pi * radius **10

print("Area of Circle : " , Area_of_Circle)

Circumference_of_Circle = 2 * pi * radius
print("Circumference of Circle: " , Circumference_of_Circle)



#14

Celsius = int(input("Enter the temperature in Celsius: \n"))

Fahrenheit = Celsius * 9/5 + 32

print("Temperature of Fahreheit : "  , Fahrenheit)


#15


num1 = int(input("Enter your number1 : "))
num2 = int(input("Enter your number2 : "))
num3 = int(input("Enter your number3 : "))

average_of_numbers = (num1 + num2 + num3)/3
print("Average of numbers:  " , average_of_numbers)



#16

Price_of_item1 = int(input("Enter the price of item1: "))
Quantity_of_item1 = int(input("Enter the quantity of item1 : "))

Price_of_item2 = int(input("Enter the price of item2: "))
Quantity_of_item2 = int(input("Enter the price of item2: "))

Price_of_item3 = int(input("Enter the price of item3 :"))
Quantity_of_item3 = int(input("Enter the price of item3: "))

Price_of_item4 = int(input("Enter the price of item4:"))
Quantity_of_item4 = int(input("Enter the price of item4 :"))


Subtotal = (Price_of_item4 * Quantity_of_item4) + ( Price_of_item3 * Quantity_of_item3) +  (Price_of_item2 * Quantity_of_item2 ) + ( Price_of_item1 * Quantity_of_item1)


Taxes_of_sales = (Subtotal*8)/100

Total = Subtotal - Taxes_of_sales
print("Total cost of items: " , Total)


#17

no_list = int(input( "Enter the numbers : "))

new_list = no_list.split()

print("Maximum : " , new_list.max())
print("Minimum : " , new_list.min())

