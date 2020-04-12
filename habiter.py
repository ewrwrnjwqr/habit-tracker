#!/usr/bin/python3
import random
from firebase import Firebase

config = {
  "apiKey": "AIzaSyDkkiDWhsRhnTVGzAP38UmVVd-lCZkJkZ8",
  "authDomain": "habit-tracking-dfbc2.firebaseapp.com",
  "databaseURL": "https://habit-tracking-dfbc2.firebaseio.com/",
  "storageBucket": "habit-tracking-dfbc2.appspot.com"
}

firebase = Firebase(config)

db = firebase.database()


#firebase = firebase.FirebaseApplication('') 

start = 1
args = []
data = []
un = 0
unt = 0
args_i = 0

print("Welcome to Class Habit Tracker!!!")
print("Enter your Name:")
x = input()
print('Hello',x,'!')

def start():
    global y
    if start == 1:
        print("What do you want to do today "+ x + "?\n Type 'register' if you want to create an account.\n Type 'login' if you want to login into an account.\n")
    else:
        print("What else do you want to do today "+ x + "?\n Type 'register' if you want to create an account.\n Type 'login' if you want to login into an account.\n")
    y= str(input())

start()

data = []

def creator():
    global user
    global data
    class stack():

        def __init__(self, username, name, password, email, role): 
            self.username = username
            self.name = name
            self.password = password
            self.email = email
            self.role = role

        @classmethod
        def from_input(cls):
            return cls(
                data.append(input('Username: ')),
                data.append(input('Name: ')), 
                data.append(input('Password: ')),
                data.append(input('Email: ')),
                data.append(input('Role: ')),
            )
    user = stack.from_input()
 
def getll():
    global un
    usernames = db.child("users").get()
    for user in usernames.each():
        if data[0] == user.val()[0]: 
            pas = input("Username in use, choose new username: ")
            for user in usernames.each():
                if pas != user.val()[0]:
                    data[0] = pas
                    un +=1
        else:
            un +=1
            #db.child("users").child(data[0]).child(1).update{1:pas} data isnt sent in this function     
    
def login():
    global unt
    inuser = input("what's your username: ")
    inpas = input("what's your password: ")
    usernames = db.child("users").get()
    for user in usernames.each():
        if inuser == user.val()[0] and inpas == user.val()[2]:
            if user.val()[4] == 1:
                    print("Welcome Teacher,",user.val()[1])
                    unt +=1 
            else:
                print("Welcome Student,",user.val()[1])
                unt +=1 
    if unt != 1:
        print("Wrong username or password was entered.") 
    
def create_class():
    global class_n
    global class_p
    global class_v
    global class_k
    global class_pw
    print("Create a new class:")
    print("What shall the class be called?")
    itemtd = input()
    print ("Created... ",itemtd)
    class_p = {}
    class_n =[]
    for _ in range(0,7):
        class_n.append(random.randint(0,9))n
    class_pw = ''.join(map(str, class_n)) 
    print("Your class code is: ",class_pw)
    class_p.update({itemtd:class_pw})
    class_v = class_p.values()
    class_k = class_p.keys()
    
def class_join():
    global itema
    class_nf = 0
    print("Join class:")
    print("Enter class name.")
    itemh = input()
    for class_k in class_p.items():
        if itemh == class_k:
            class_nf +=-1
        if itemh != class_k:
            class_nf += 1 
    if class_nf == 1:
            print("This class does not exist!")
            class_join()
    print("Enter class code.")
    itema = input()
    for class_v in class_p.items():
        if itema == class_v:
            print("Class joined!")      
            class_nf +=-1       
        if itemh != class_k:
            class_nf += 1
    if class_nf == 1:
        print("You typed the class in wrong!")
        class_join()
        
if y == 'register':
    args.append('create')
    creator()
    print(data)
    while un == 0:
        getll() 
    db.child("users").child(data[0]).set(data)
    print("account created!")
    start()
if y == 'login':
    args.append('login')
    while unt == 0:
        login()
        db.child("users").user.val()[0].set(data[0])
    if user.val()[4] != 1:
        print("creating class")
        create_class()
    else:
        print("joining class")
        class_join()
    
for i in range(0,len(args)): # smart code for adding args to y input and possible multi select html li or button?
    if y != args[i]:
        args_i +=1
if args_i > len(args):
    print("Error")
else:
    args_i = 0
    
