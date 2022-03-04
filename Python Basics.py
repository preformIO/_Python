# %% [markdown]
# # Python Basics
#  * Variables
#  * Data types
#  * Operators
# 

# %% [markdown]
# ## Variables
#  * are placeholders for values in computer's memory
#  * calling a variable by name returns its value in memory

# %%
# set variable to a string value of "Hello World!"
message = "Hello World!"
print(message)

# set variable a to a value of 1 (integer)
an_integer = 1

# print the value of the vaiable to the console by callin the variable by name
print(an_integer)

# set another variable to int value of 2
another_integer = 2

# set yet another integer to the value of the sum of our first two integer
integer_sum = an_integer + another_integer

# print the sum of the first two integers
print(integer_sum)

# set variable to a float value of 1.3
a_float = 1.3

print(a_float)

# %% [markdown]
# ## Data types
#  * strings = ""
#  * integers = 1
#  * floats = 1.0


# %%
# Integer
i = 1
i2 = int(2.5) # ingores all decimal point information
print("i =", i)
print("i2 =", i2, '\n') #can cast any number as an integer, but watch for unexpected results

# %%
# Float
print("float(i) =", float(i))
f = 1.5
print("f =", f)
print("f + i =", f + i)
print("f * 2 =", f * 2, '\n')

# %%
# String
# -------------------
# basic string with single quotes
ss = 'Hello World! Is the "default" message for a beginning application.'
print(ss)
print()

# double quotes and \escape character examples
sd = "Hello World!... \nIs the \"default\" message for a beginning application."
print(sd)

# %%
# String concatenation
# -------------
# concatenation supported by print function
# (joins each element with ' ' in between each)
print(sd, "\n") 

# concat using '+' operator
# (no space characters added for more precise control)
sd_msg = "sd = '" + sd + "'\n"
print(sd_msg)

# f-strings (formatted strings) make concatenation 
# much easier for programers to read and write, IMHO.
print(f"Hello World! i = {i}; f = {f}\n")
# they also make it easier to format numbers.
print(f"Fraction '1/3' rounded to 2 decimal places = {1/3:.2f}")
ratio = 35/3
print(f"Ratio '{ratio}' converts to '{ratio *100:,.2f}%'")

# %%
# Lists
# ----------------
# 1D array -- a 1x15 array explicitly defined... 
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 

print(f"List 'l' = \n{l}\n")

# %%
# example of building a list by appending items to an empty list
l = []
for i in range(15):
  l.append(i)
print(f"List 'l' built with traditional for i in range(15) = \n{l}")

# example of building a list using list comprehension
l = [i for i in range(15)] 
print(f"List 'l' built with range(15) = \n{l}")

# using list comprehension and random
import random
lrandom = [
  random.randint(1,5) for i in range(15)
]
print(f"List 'lrandom' = \n{lrandom}\n")

# %%
# using list * operator
l = [0] * 15 
print(f"List 'l' = \n{l}")
print(f"List element 'l[14]' = {l[14]}\n")

# %%
# 2d Lists
# 15x3 list of 0's
l_2d = [[0]*15] *3 # using list * operator again
print(f"l_2d = \n{l_2d}\n")
print(f"l_2d[2][14] = {l_2d[2][14]}") # 2D indexing
print(f"l_2d[-1][-1] = {l_2d[-1][-1]}") # last elements in each dimension
print(f"l_2d[1:] = {l_2d[1:]}\n") # last elements in each dimension

# 15x3 list of random numbers
l_2d_random = [
  [
    random.randint(0,14) for i in range(15)
  ] 
  for i in range(3)
]
print(f"l_2d_random = \n{l_2d_random}\n")

# %%
# Tuples
# can only ever be one-dimensional
t = ((("first", "second") *2) * 4) * 2 
print(f"Tuple 't' = \n{t}\n")

# tuples are immutable (code below generates 
# "TypeError: 'tuple' object does 
# not support item assignment")
t[0] = 'new string'

# %% [markdown]
# ## Operators

# %%
# * multiplicative
print(f"1 * 2 = {1 * 2}\n")
print(f"l_2d * 2 = {l_2d * 2}\n")
print(f"(((('first', 'last')) * 2) *2) * 2) = {(((('first', 'last') * 2) *2) * 2)}\n")

# %%
# + additive
print(f"2 + 2 = {2 + 2}")
#print(f"2Dlist + 2 = {l_2d + 2}") # cannot concat int into lists
print(f"(((('first', 'last')) + (2,)) +(2,)) + (2,)) = \n")
print(f"{(((('first', 'last') + (2,)) +(2,)) + (2,))}\n")

# %%
# / division (float)
print(f"float division 2 / 3 = {2 / 3}")

# // indiger division
print(f"integer division 2 // 3 = {2 // 3}\n")

# %%
# integer modulo operator
r = 12 % 5 # divides 12 by 5 and gives you the remainder
print(f"Remainder of 12 % 5 = {r}\n")

# %%
# days and weeks example
days = 30
weeks_i = days // 7
days_r = days % 7 
print(f"Using int math, {days} days = {weeks_i} weeks, {days_r} days")
weeks_f = days /7
print(f"Using float math, {days} days = {weeks_f:.2f} weeks\n")