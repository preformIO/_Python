# %% [markdown]
# # Intermediate python
# 
#  * Conditionals
#     * If statements
#     * Else-if chains
#  * Loops
#     * Iterables like range() and list()
#     * List comprehension
#  * Functions
#  * Classes & Methods

# %% [markdown]
# ## Conditionals

# %%
# if statements
if True:
    # do something if condition is true
    pass
else:
    # do something else instead
    pass

# %%
# if statement based on a random or other calculation
import random
randBool = random.choice([True, False])
if randBool:
    print(f"randBool is true")
    pass
else:
    print(f"randBool is false")    
    pass

# %%
# if - else chain
randInt = random.choice([None, 0, 1, 2])
if randInt == 0:
    print("randInt is zero")
    pass
elif randInt == 1:
    print("randInt is one")
    pass
elif randInt == 2:
    print("randInt is two")
    pass
else: #default
    print(f"randInt = {randInt}")
    pass

# %%
# compound conditionals
import random
randBool = random.choice([True, False])
randInt = random.choice([None, 0, 1])
if (randInt == 0) or (randBool):
    print("randInt is zero OR randBool is true")
    pass
elif (randInt == 1) and (not randBool):
    print("randInt is one AND randBool is false")
    pass
else: #default
    print(f"randInt = {randInt}, randBool = {randBool}")
    pass

# %% [markdown]
# ## Loops
# 

# %%
# loops with indexes
print(f"range (12) = {range (12)}")

# example of what range(int) returns
for i in range(12):
    print(f"i = {i}")
    pass

# %%
import numpy as np
l = np.random.rand(12)
print(f"l = \n{l}")

# %%
# example using range(length(list))
for i in range(len(l)):
    print(f"l[{i}] = {l[i]}")
    pass

# %%
# loop through items in a iterable
for float_val in l: # comparable to C# foreach loops
    print(f"float_val = {float_val}")

# %%
# loop to create a 2D array
arr = []
for i in range(3):
    arrJ = []
    for j in range (3):
        arrJ.append(np.random.rand())
    arr.append(arrJ)
print(f"arr = \n{arr}")

# %%
# List comprehension 1D
arrListComp = [i for i in range(3)]
print(f"arrListComp = \n{arrListComp}")

# %%
# List comprehension 2D
arrListComp2D = [[j+i for j in range(3)] for i in range(3)]
print(f"arrListComp = \n{arrListComp2D}")

# %%
# List comprehension 2D with function
arrListComp2D = [[np.random.rand() for j in range(3)] for i in range(3)]
print(f"arrListComp2D = \n{arrListComp2D}")

# %% [markdown]
# ## Functions

# %% [markdown]
# ### Basic functions with one argument

# %%
# define funcName (args)
def sqrt(num):
    import math
    
    root = math.pow(num, 1/2)

    return root
    pass

print(f"sqrt(9) = {sqrt(9)}")

# %% [markdown]
# ### Handling unexpected types

# %%
sqrt("Hello World!") # this will throw an error

# %%
# handle unexpected data types
def sqrt(num):
    import math
    root = None
    
    try:
        root = math.pow(num, 1/2)
    except:
        print(f"'{num}' is not a real number -- data type = {type(num)}")
        pass

    return root
    pass

print(f"sqrt(9) = {sqrt(9)}")
sqrt("Hello World!") # this will no longer throw an error

# %%
import math

def percentAsString(num):
    assert (type(num) == int) or (type(num) == float)

    perc = num * 100
    
    perc_string = f"{perc:,.1f}%"
    
    return perc_string

[percentAsString(x) for x in range(1,11)]

# %%
# assert trigering example
[percentAsString(char) for char in "Hello World!"] # will throw an error

# %%
# define a fuction by name (parameters go in prentheses = "default values")
def fncName (parameter1 = "foo", parameter2 = "bar", etc = "baz"):
    print(f"parameter1 = {parameter1}")
    print(f"parameter2 = {parameter2}")
    print(f"etc = {etc}")
    
fncName(1, 2, 3)
fncName(1, 2)
fncName()

# %%
# example of passing a named parameter
fncName(etc = 3)

# %% [markdown]
# ### *args

# %%
# positional arguments (*args) example
def fncNameWithArgs(*args):
    for arg in args:
        if type(arg) == str:
            print(f"arg = '{arg}'")
            pass
        elif type(arg) == int:
            print(f"arg = {arg}")
            pass
        else:
            print(f"arg of unkown type = {type(arg)}, value = {arg}")
            pass
        pass
    
    return args
    pass

fncNameWithArgs("1", [2, 4, 6], 3)
# %%
# *args does not catch keword arguments
fncNameWithArgs(etc = 5)

# %% [markdown]
# ### **kwargs

# %%
# keword arguments (**kwargs) example
def fncNameWithKwargs(**kwargs):
    for key, value in kwargs.items():
        if type(value) == str:
            print(f"{key} = '{value}'")
            pass
        elif type(value) == int:
            print(f"{key} = {value}")
            pass
        else:
            print(f"kwarg of unkown type: {key} = {value}")
            pass
        pass
    
    return kwargs
    pass

fncNameWithKwargs(kwarg1 = "1", kwarg2 = 2, kwarg3 = [1,3,5])

# %%
# **kwargs does NOT capture positional arguments, however
fncNameWithKwargs(3, kwarg1 = "1", kwarg2 = 2, kwarg3 = [1,3,5])

# %%
# In order to make fully robust functions, 
# you have to capture *args AND **kwargs
def fncNameWithArgsAndKwargs(*args, **kwargs):
    for arg in args:
        if type(arg) == str:
            print(f"arg = '{arg}'")
            pass
        elif type(arg) == int:
            print(f"arg = {arg}")
            pass
        else:
            print(f"arg of unkown type = {arg}")
            pass
        pass
    

    for key, value in kwargs.items():
        if type(value) == str:
            print(f"{key} = '{value}'")
            pass
        elif type(value) == int:
            print(f"{key} = {value}")
            pass
        else:
            print(f"kwarg of unkown type: {key} = {value}")
            pass
        pass
    
    return (args, kwargs)
    pass

fncNameWithArgsAndKwargs(3, kwarg1 = "1", kwarg2 = 2, kwarg3 = [1,3,5])

# %%
# Floor division (Integer division) review
print(f"1/4 = {1/4}")
print(f"1//4 = {1//4}")

print(f"5/4 = {5/4}")
print(f"5//4 = {5//4}")

print(f"11/4 = {11/4}")
print(f"11//4 = {11//4}")

# %%
def Q1(L): # def defines a function, Q1 is the name of the fnc, () accepts arguments
    
    q1_i = len(L)//4
    list_sorted = np.sort(L)
    q1 = list_sorted[q1_i]
    
    print(f"list = {L}")
    print(f"list_sorted = {list_sorted}")
    print(f"Q1 of list = {q1}")
    
    return q1

data = np.random.rand(12)
Q1(data)

# %% [markdown]
# ## Classes & Methods

# %%
# 'class' declares a class, 'FinancialPortfolio' is its name
class FinancialPortfolio: 
    def __init__(self, name = "", cash = 0, bonds = 0, stocks = 0, alternatives = 0):
        print(f"FinancialPortfolio class instance created = {self}")
        self.name   = name
        self.cash   = cash
        self.bonds  = bonds
        self.stocks = stocks
        self.alts   = alternatives
        
        return
    
    def Print(self):
        print(f'{self.name}\'s Portfolio :: printing.')
        print(f'        cash = ${self.cash:,.2f}')
        print(f'       bonds = ${self.bonds:,.2f}')
        print(f'      stocks = ${self.stocks:,.2f}')
        print(f'        alts = ${self.alts:,.2f}')
        
    def PrintNetWorth(self):
        net = self.cash + self.bonds + self.stocks + self.alts
        print(f'{self.name}\'s Portfolio net worth = ${net:,.2f}')    

    pass

# create an instance of the class
portfolio = FinancialPortfolio("Anisha", -10, 1000, 3000000, 15)

# call some of its functions
portfolio.Print()
portfolio.PrintNetWorth()
