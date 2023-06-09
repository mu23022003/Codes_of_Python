#import numpy as np
#1
'''
new_data = np.random.random((40,5))
np.savetxt("first.csv" , new_data , fmt="%.2f" , delimiter=",", header="H1,H2,H3,H4,H5")
#reading csv
reading_csv = np.loadtxt("first.csv" , delimiter=",")
reading_csv[:4,:]
print(reading_csv)
'''



#2
'''
filename = "first.csv"
try:
    data = np.loadtxt(filename,delimiter=",")
    print(data)
except PermissionError as e:
    print("Permission denied" , str(e))
    '''

#3
'''
import pickle

#write tp pickle file

ordering = {"first": 1,
            "second": 2,
            "third": 3}
pickle.dump(ordering , open("new.pkl", "wb"))

#reading data into pickle file

reading_pickle = pickle.load(open("new.pkl" , "rb"))
print(reading_pickle)
'''


#CSV Examples

#import csv

'''
with open('data.csv' , 'w') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
'''

'''
data = [
    ['Name' , 'Age' , 'Country'],
    ['John' , '25' , 'USA'],
    ['Aloce' , '30' , 'Canada'],
     ['Bob' , '35' , 'UK']
]

with open('output.csv' , 'w' , newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
'''



'''
with open('output.csv' , 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'] , row['Age'] , row['Country'])

'''


'''
with open('output.csv' , 'r') as file:
    reader = csv.reader(file)
    for row in reader:

        name = row[0]
        age = row[1]
        print(name, age)
        '''


'''
data = [
    {'Name' : 'John' , 'Age' : '24' , 'Country' : 'USA'},
    {'Name' : 'Alice' , 'Age' : '30' , 'Country' : 'Canada'},
    {'Name' : 'Bob' , 'Age' : '35' , 'Country' : ' UK'}

]

fieldnames = ['Name' , 'Age' , 'Country']

with open('output.csv' , 'w' , newline='') as file:
    writer = csv.DictWriter(file , fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(data)
'''
'''
with open('output.csv' , 'r') as file:
    reader = csv.DictReader(file , delimiter=';' , quotechar='"')
    for row in reader:
        print(row)
    '''

'''
#json

import json


college = {
    "college" : "Engineering College" ,
    "Objective" : "Masterring Electrical and Computer Engineering",
    "department" : {
        "dep1" : "Electrical",
        "dep2" : "Computer"
    },
    "years" : [
        "year 1",
        "year 2",
        "year 3",
        "year 4"
    ],
    "number" : [1 , 2, 3 , 4],
    "ID" : [ 10, 20 , 30 , 40]
}

json.dump(college , open("college.json" , "w"))

college_new = json.load(open("college.json" , "r"))
print(college_new)

'''
'''

import  PyPDF2

new_pdf = open('intro.pdf' , 'rb')
reading_pdf = PyPDF2.PdfFileReader(new_pdf)


print(reading_pdf.numPages)
pdf_page = reading_pdf.getPage(0) # get the page numbers
print(pdf_page.extractText())  #extration of any words
new_pdf.close() #close pdf
'''

'''
class Employee:
    count = 0
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.count += 1
    def displayCount(self):
        print ("There are %d employee"  % Employee.count)
    def displayDeatils(self):
        print("Name: " , self.name , "Position: " ,self.position , "Salary: " , self.salary)

emp1 = Employee("Employee1", "HR", 30000)
emp2 = Employee("Employee2", "Manager", 50000)
emp3 = Employee("Employee3", "Engineer" , 65000)
emp4 = Employee("Employee4", "Programmer", 70000)

emp2.displayCount()

print("Information about Employee")

emp1.displayDeatils()
emp2.displayDeatils()
emp3.displayDeatils()
emp4.displayDeatils()

'''


'''
from time import strftime
from tkinter import Label , Tk

# window configure

window = Tk()
window.title("")
window.geometry("200x80")
window.configure(bg = "black")
window.resizable(False , False)

# label_configure

clock_label = Label(window , bg="black" , fg="white" , font= ("Times" , 30 ,'bold') , relief='flat')
clock_label.place(x = 20 , y = 20)

def updating_label():
    current_time = strftime('%H: %M %S')
    clock_label.configure(text = current_time)
    clock_label.after(80,updating_label)

updating_label()
window.mainloop()
'''

'''
 https://pll.harvard.edu/catalog/free

import  tkinter as tk

window = tk.Tk()
window.title("Hello Tkinter")

label = tk.Label(window , text="Hello ,Tkinnter!")

label.pack()

button = tk.Button(window , text="Click me!" , command=lambda : print("Button Clicked!"))
button.pack()

window.mainloop()
'''



'''
 Gesssing game  
 
 
import random


def guesssing_game(guessLimit , number):
    random_number = random.random(1,number)
    try:
        while guessLimit() > 0:
            guess  = int(input("What is your guess?"))
            guessLimit -= 1
            if random_number == guess:
                print("Congrats , You got it right!")
                break
            elif guess > number:
                print("Your Guess is out of range:")
                print(f"You habe {guessLimit} guess(es) left")
            else:
                print("Sorry , That was wrrong!")
                print(f"Yo have {guessLimit} guess(es) left")
            print("game over")
            print(f"The random number was {random_number}")

    except ValueError:
        print("Only integer are allowd!")


def easy():
    print("You are to guess a number between 1 and 10 , and you have 6 guesss")
    guesssing_game(6,10)

def medium():
    print("You are to guess a number between 1 and 20 , and you have 4 guess")
    guesssing_game( 4, 20)

def hard():
    print("You are guess a number between 1 and 50 , and you have 3 guess")
    guesssing_game(3,50)

def try_again():
    again = input("do you want to play again Yes/No")
    if again.upper() == 'YES':
        welcome()
    elif again.upper() == 'NO':
        print("Thans for playing")
    else:
        print("Wrong input")
        try_again()

def welcome():
    print("Welcome to th guesssing game")
    difficulty = input("Choose your level between Easy Medium , Hard")
    if difficulty.upper() == 'Easy':
        easy()
        try_again()
    elif difficulty.upper() == 'Medium':
        medium()
        try_again()
    elif difficulty.upper() == "Hard":
        hard()
        try_again()
    else:
        print("This is wrong input")
        welcome()

    welcome()

'''



# Music loder
