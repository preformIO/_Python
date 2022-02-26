def main():
  # %%
    # %% [markdown]
  # # Python Basics
  #  * Data types
  #  * Operators
  #  

  # %%
  # %% [markdown]
  # ## Data types

  # %%
  # Interger
  i = 1
  print("int i = ", i)
  print("int(i / 1.5) = ", int(i / 1.5), '\n') #can cast any number as an integer, but watch for unexpected results

  # %%
  # Float
  f = 1.0
  print("f = ", f)
  print("f * 1.5 = ", f * 1.5, '\n')

  # %%
  # Strings
  ss = 'Hello World! Is the "default" message for a beginning application.' # basic string with single quotes
  print("ss = '" + ss + "'")
  sd = "Hello World!... \nIs the \"default\" message for a beginning application." # \escape character example
  print("sd = '" + sd + "'\n")
  
  # simplify output by using an f-string
  sf = f"Hello World! i = {i}; f = {f}\n"
  print(sf)

  # %%
  # Lists - 1D array
  l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] # a 1x15 array... also example of zero indexing item addresses

  print(f"l = {l}\n")

  # %%
  import random

  l = [i for i in range(15)] # example using list comprehension
  print(f"l = {l}")
  lrandom = [random.randint(0,14) for i in range(15)]
  print(f"lrandom = {lrandom}\n")

  # %%
  l = [0] * 15 # using list * operator
  print(f"l = {l}")
  print(f"l[14] = {l[14]}\n")

  # %%
  # 2d Lists
  # 15x3 list of 0's
  l2D = [[0]*15] *3 # using list * operator again
  print(f"l2D = {l2D}")
  print(f"l2D[2][14] = {l2D[2][14]}")
  print(f"l2D[-1][-1] = {l2D[-1][-1]}\n") # last elements in each dimension

  # 15x3 list of random numbers
  l2D_random = [[random.randint(0,14) for i in range(15)] for i in range(3)]
  print(f"l2D_random = \n{l2D_random}\n")

  # %%
  # Tuples
  t = ((("first", "second") *2) * 4) * 2 # can only ever be one-dimensional
  print(f"t = \n{t}\n")
  
  # %%
  # %% [markdown]
  # ## Operators

  # %%
  # * multiplicative
  print(f"1 * 2 = {1 * 2}\n")
  print(f"2Dlist * 2 = {l2D * 2}\n")
  print(f"(((('first', 'last')) * 2) *2) * 2) = {(((('first', 'last') * 2) *2) * 2)}\n")

  # %%
  # + additive
  print(f"1 + 2 = {1 + 2}")
  #print(f"2Dlist + 2 = {l2D + 2}") # cannot concat int into lists
  print(f"(((('first', 'last')) + (2,)) +(2,)) + (2,)) = \n")
  print(f"{(((('first', 'last') + (2,)) +(2,)) + (2,))}\n")

  # %%
  # / division (float)
  print(f"float division 2 / 3 = {2 / 3}")

  # // indiger division
  print(f"integer division 2 // 3 = {2 // 3}\n")

  # %%
  # integer modulo operator
  r = 12 % 5
  print(f"12 % 5 = {r}\n")

  # days and weeks example
  days = 30
  print(f"days = {days}")
  weeks_i = days // 7
  days_r = days % 7 # divides days by 7 and gives you the remainder
  print(f"using int math = {weeks_i} weeks, {days_r} days")
  weeks_f = days /7
  print(f"using float math = {weeks_f:.2f} weeks\n")

  # %%
  return

main()