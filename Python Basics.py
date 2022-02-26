def main():
  # %% [markdown]
  # # Python Basics
  #  * Data types
  #  * Operators
  #  

  # %% [markdown]
  # ## Data types

  # %%
  # Interger
  i = 1
  print(i)
  int(i / 1.5) #can cast any number as an integer, but watch for unexpected results

  # %%
  # Float
  f = 1.0
  f * 1.5

  # %%
  # Strings
  ss = 'Hello World! Is the "default" message for a beginning application.' # basic string with single quotes
  print(ss)
  sd = "Hello World!... \nIs the \"default\" message for a beginning application." # \escape character example
  print(sd)
  sf = f"Hello World! i = {i}; f = {f}" # f-string
  sf

  # %%
  # Lists - 1D array
  l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] # a 1x15 array... also example of zero indexing item addresses
  print(f"l = {l}")

  # %%
  import random

  l = [i for i in range(15)] # example using list comprehension
  print(f"l = {l}")
  lrandom = [random.randint(0,14) for i in range(15)]
  print(f"lrandom = {lrandom}")

  # %%
  l = [0] * 15 # using list * operator
  print(f"l = {l}")
  print(f"l[14] = {l[14]}")

  # %%
  # 2d Lists
  l2D = [[0]*15] *3 # using list * operator again
  print(f"l2D = {l2D}")
  l2D[2][14]
  l2D[-1][-1] # last elements in each dimension

  l2D_random = [[random.randint(0,14) for i in range(15)] for i in range(3)]
  print("l2D_random = ")
  l2D_random

  # %%
  # Tuples
  t = ((("first", "second") *2) * 4) * 2 # can only ever be one-dimensional
  t

  # %% [markdown]
  # ## Operators

  # %%
  # * multiplicative
  print(f"1 * 2 = {1 * 2}")
  print(f"2Dlist * 2 = {l2D * 2}")
  print(f"(((('first', 'last')) * 2) *2) * 2) = {(((('first', 'last') * 2) *2) * 2)}")

  # %%
  # + additive
  print(f"1 + 2 = {1 + 2}")
  #print(f"2Dlist + 2 = {l2D + 2}") # cannot concat int into lists
  print(f"(((('first', 'last')) + (2,)) +(2,)) + (2,)) = {(((('first', 'last') + (2,)) +(2,)) + (2,))}")

  # %%
  # / division (float)
  print(f"float division 1 / 3 = {1 / 3}")

  # // indiger division
  print(f"integer division 1 // 3 = {1 // 3}")
  days = 20
  weeks = 20 // 7
  print(f"days // 7  = {days // 7}")
  print(f"days / 7  = {days / 7}")

  # %%
  # integer modulo operator
  days_r = days % 7 # divides days by 7 and gives you the remainder
  print(f"20 days = {weeks} weeks and {days_r} days")

  return

main()