This script contains code associated with Lecture 3, Variables, Expressions and Operators. The indented blocks are code for you to input to the Python interpreter.

Python as a calculator

        6+5
        a = 6+5
        print(a) # Here, a is a variable that we have assigned the value 11 to
        print(‘a’) # Here, a is a string. Python knows this because of the single quotation marks

We ask the computer to work with values. What is a value?

A letter, a number
Technically, it is an expression that can not be further evaluated

For example, 3 is a value, a is a value

2+1 can be evaluated to 3

a*7 can be evaluated to 7a

Values are of different types

Common Python built-in types include
int - integers
0,1,2

float - floating point numbers
0.1, 1.356

complex - complex numbers
5j + 3 -x

str - strings
‘abracadabra’, ‘ABBA’

Boolean
True or False

These also evaluate to ‘0’ or ‘1’ as integers

        b = True
        int(b)

        b = False 
        int(b)
        b = true # What happens?
        
We assign values to variables
Therefore, variables can change

        a = 12
        print(a)
        a = ‘logistic’
        print(a)
 
A series of values, variables and operators gives you an expression

        a
        a*b
        a*b + 12
 
What is an operator? It's a symbol that represents a task 

Some are mathematical but not all
For example, = assignment

        a = 5*3
        print(a)
 
Arithmetic operators include * (multiplication), + (addition), - (subtraction), / (division), ** (exponentiation) and my favorite %, the lesser known modulus operator.
 
        5 % 3 # What happens?
       
How would you describe the modulus operation?
      
Comparison operators include == (equivalence), != (negative equivalence), > (greater than) and < (less than).

We also have membership operators like in, not in and identity operators like is, is not.

Boolean operators signify logical operations like and, or and not.

        a = True
        b = False
        print(a and b)
        print(a or b)
        print(a not b)

Our artificial neuron activates when all 3 inputs are true. Our pseudocode is:

        If I1 == I2 == I3 == True       # Testing for equivalence
        Then Neuron_activation = True   # assigning a value to Neuron_activation
  
Next, we will figure out how to translate our pseudocode to Python.
 
 
