import random
import time

def hola(name):
    print("Hello {name}!!".format(name=name))

def rolled_dice():
    print("You have rolled {}".format(random.randint(1,6)))

def programm_sleep(t):
    print("I will need to sleep ....")
    time.sleep(t)
    print("I have wake up!!")
    
def divisor_pattern(number):
    for i in range(1, number+1):
        for j in range(1, number+1):
            if ((i % j == 0) or (j % i == 0)):
                print("* ",end="")
            else:
                print("  ",end="")
        print((i+1))

def printing_format(name=None, height=None, age=None, weight=None, 
                    eyes=None, teeth=None, hair=None):
    print(f"Let's talk about {name}.")
    print(f"He's {height} inches tall")
    
def asking_questions():
    print("How old are you?: ", end="")
    age = input()
    print("How tall are you?: ", end="")
    height = input()
    print("How much do you weight?: ", end="")
    weight = input()
    print(f"So, you're {age} old, {height} tall and {weight} heavy.")
    
def prompting_people():
    age = input("How old are you?: ")
    height = input("How tall are you?: ")
    weight = input("How much do you weight?: ")
    print(f"So, you're {age} old, {height} tall and {weight} heavy.")
    
def regurgitator():
    age = int(input("Please enter your age: "))
    while age < 1 or age > 95:
        # Repeat this code while the age is invalid
        print("This age is not valid")
        age = int(input("Please enter your age: "))
    print("Thank you for entering your age!")
    
def catching_exception():
    while True:
        try:
            ride_number = int(input("Please enter the ride number you want: "))
            print(f"You have entered: {ride_number}")
            break
        except ValueError as ve:
            print("Invalid number")
            print(ve.__str__()) 
        

def counter_controlled_repetition():
    #pass