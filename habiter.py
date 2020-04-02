#from firebase import firebas
import random

#firebase = firebase.FirebaseApplication('') 


start = 1
args = []
args_i = 0
yo momma

print("Welcome to Class Habit Tracker!!!")
print("Enter your Name:")
x = input()
print('Hello',x,'!')

def start():
    global y
    if start == 1:
        
        print("What do you want to do today "+ x + "?\n Type 'register' if you want to create an account.\n Type 'login' if you want to login into an account.\n Type 'create' if you want to create a class. \n Type 'join' if you want ot join a class.")
    else:
        print("What else do you want to do today "+ x + "?\n Type 'register' if you want to create an account.\n Type 'login' if you want to login into an account.\n Type 'create' if you want to create a class. \n Type 'join' if you want ot join a class.")
    y= str(input()) #if already done

start()

def create_account():
    class creator():
        def __init__(self, name, username,  password, email): #make inputs
            self.name = name
            self.username = username
            self.password = password
            self.email = email
            self.role = role

            dictionary = []
            dictionary.append(self.name)
            dictionary.append(self.username)
            dictionary.append(self.password) #encrypting password?
            dictionary.append(self.email)
            dictionary.append(self.role)
            #firebase.post(location,dictionary) 
    print("account created!")

def login():
    print("logging in...")
    
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
        class_n.append(random.randint(0,9))
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
    args.append('register')
    create_account()
if y == 'login':
    args.append('login')
    login()
if y == 'create':
    args.append('create')
    #if user == self.teacher:
    create_class() # only if teacher ASSIGN ROLES AND LOG FIRST
    start()
    #else:
        #print("You are not a teacher")
        #start()
    
if y == 'join':
    args.append('join')
    class_join()
    
for i in range(0,len(args)): # smart code for adding args to y input and possible multi select html li or button?
    if y != args[i]:
        args_i +=1
if args_i > len(args):
    print("Error")
else:
    args_i = 0
    
