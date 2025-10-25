#My baby steps in PYTHON includes the following below:


"""(This is an example of a comment, I am using it to explain what I am doing here)
What I Learned
- print() statement
- variables
- Basic python operators
- Basic data types
- Input/output functions
- loops
- if statements
- functions 
- basic calculations
"""

#PRINT STATEMENT(first python word)

print("Welcome Reader, this is my first step in python")


#VARIABLES - Variables is a name given to a value.
x = "5" # x is a variable to the value '5'
y = "MARY"  # Y is a variable to the value 'Mary'
print(x, y)


# BASIC PYTHON OPERATORS
"""
a. Arithmetic operators are  addition(+), substraction(-), division(/), modulus(%),
Exponentiation(**), floor division(//), multiplication(*)

b. Comparison Operation - less than(<), greater than(>), equal to (=), 
Less than or equal to (<=), greater than or equals to(>=),not equal to(!=)

c. Logical Operations - And, or , Not

d. Assignment Operators
"""
x = 5
y = 3
d = x + y
e = x - y
f = x // y
g = x ** y
h = x % y

print(d, e, f, g , h)
 
#BASIC DATA TYPES 
"""
a. Integers(int) -  positive or negative whole numbers e.g -3, 30 et.c
b. Float - positive or negative decimal numbers e.g 0.03, 0.0056 et.c
c. Strings - sequences of character enclosed in single ' ' or double quotation " " e.g "Mary" or '5'
d. Booleans also called Bool are represented by True or False.
"""

#INPUT AND OUTPUT FUNCTIONS
"""
The input() function in Python is used to receive data from the user while the program is running.
It pauses the program, waits for the user to type something, 
and then stores that input as a string (by default).
"""
# User Input Example
name = input(str('Enter your name:')) #Input fxn
print(f"My name is {name}") #Output fxn


#LOOPS
"""
A loop is a programming structure that allows you
to repeat a block of code multiple times without writing it over and over again.
Why Do We Use Loops?
- To avoid repetition in your code.
- To automate repeated tasks.
- To process lists, strings, numbers, and more.

*Types of loops - For and while loop
"""
#FOR LOOP example
for i in range(5):        #This prints "Hello" 5 times.
    print("Hello")

#WHILE LOOP example
count = 1
while count <= 5:      #This also prints "Hello" 5 times.
    print("Hello")
    count += 1


#IF STATEMENT
"""
The if statement evaluates a condition (an expression that results in True or False).
If the condition is true, the code block inside the if statement is executed. 
If the condition is false, the code block is skipped.
"""
#IF statement example
number = 15
if number > 0:
  print("The number is positive")
  
  
#FUNCTIONS
"""
Python Functions
- A function is a block of code which only runs when it is called.
- A function can return data as a result.
- A function is a reusable block of code that helps avoid code repetition.

*TYPES OF FUNCTION
- Default Argument
- Positional Argument
- keyword Argument
- Keyword- only Argument
- Variable - length Argument
"""
#DEFAULT ARGUMENT
"""
A default argument is when you assign a default value to a parameter in a function.
So if the user doesn't provide a value, Python will use the default.

Short Note:
It prevents errors when arguments are missing and saves time.
"""
def greet(name="Guest"):
    print(f"Hello {name}")

greet()        # Uses default → "Guest"
greet("Mary")  # Uses provided value

#POSITIONAL ARGUMENT
"""
These are arguments passed to a function in order.
The position matters — the first argument goes to the first parameter, second to second, etc.

Short Note:
If you change the order, the meaning changes.
"""
def display(name, age):
    print(name, age)

display("Mary", 23)   # Correct
display(23, "Mary")   # Wrong meaning (order changed)

#KEYWORD ARGUMENT
"""
Here, you specify the parameter name when calling the function, so order no longer matters.

Short Note:
Makes your code clearer and avoids confusion.
"""
def bio(name, age):
    print(name, age)

bio(age=22, name="Mary")  # Order doesn’t matter now


#KEYWORD - ONLY ARGUMENT
"""
These are arguments that must be specified using keywords, not positional order.
You enforce them using * in the function definition.

Short Note:
Used when you want clarity and prevent wrong ordering.
"""
def student(name, *, grade):
    print(name, grade)

student("Mary", grade="A")   # Correct
# student("Mary", "A")       #  Not allowed

#VARIABLE LENGTH ARGUMENT
"""
Used when you don't know how many arguments will be passed.
There are two forms: **Kwargs and *args
"""
#*args
def add(*numbers):
    print(sum(numbers))

add(2, 3, 5, 10)   # Works with any number of inputs


#**Kwargs
def profile(**info):
    print(info)

profile(name="Mary", age=22, level="Tech sis")



print("\n Mary Week 1 Basics Completed Successfully!")
