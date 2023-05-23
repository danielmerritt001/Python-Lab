
#---------- LAB BEGINS AT LINE 82 ----------#


#Python functions

# def first_function():
#     pass

# def add(a, b):
#   return a + b

# def subtract(a, b):
#   return a - b

# def compute(a, b, op):
#   return op(a, b)

# print(compute(1, 2, add))

# math_operations = {
#   '+': add,
#   '-': subtract
# }

# print(math_operations['+'](2, 4))

# ----------Lambda functions (Kinda like Arrow Functions)---------- #
# nums = [1, 3, 2, 6, 5]
# #                 lambda (elem): function, (list being filtered)
# odds = list( filter(lambda num: num % 2, nums) )
# print(odds)

# ----------Parameters and Arguments ---------- #
# def fn(*args):
#   print( type(args) )
#   for arg in args:
#     print(arg)

# fn(1, 2, 'SEI')

# EASY AND READABLE WAY!!!!
# def dev_skills(dev_name, *args):
#   dev = {'name': dev_name, 'skills': []}
#   for skill in args: 
#     dev['skills'].append(skill)
#   return dev

# SEXY WAY!!!!
# def dev_skills(dev_name, *args):
#   dev = {'name': dev_name, 'skills': list(args)}
#   return dev

# print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))

# def divide(a, b):
#   return f'{a} divided by {b} is {a / b}'

# NOT CONVENTION BUT FUNCTIONAL
# divide(b=25, a=100)

# def dev_skills(dev_name, **kwargs):
#   # kwargs will be a dictionary!
#   dev = {'name': dev_name, 'skills': kwargs}
#   return dev

# print(dev_skills('Jackie', HTML=5, CSS=3, JavaScript=4, Python=2))

# ---------- Arg Demo ---------- #
#Must be in this order to work!
# def arg_demo(pos1, pos2, *args, **kwargs):
#   print(f'Positional params: {pos1}, {pos2}')
#   print('*args:')
#   for arg in args:
#     print(' ', arg)
#   print('**kwargs:')
#   for keyword, value in kwargs.items():
#     print(f'  {keyword}: {value}')

# arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')

# ---------- Python Functions Lab ----------

# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.
def sum_to(n):
  answer = 0
  for num in range(n+1):
    answer += num
  return answer

print(sum_to(4))

# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
def largest(list):
  high_num=0
  for number in list:
    if number > high_num:
      high_num = number
  print(high_num)

largest([1, 2, 3, 4, 0])
largest([10, 4, 2, 231, 91, 54])

# Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.
def occurrences(str1, str2):
  occurrence = 0
  for num in range(len(str1)-len(str2)+1):
    if str1[num:num+len(str2)] == str2:
      occurrence += 1
  print(occurrence)

occurrences('fleep floop', 'e')   
occurrences('fleep floop', 'p')   
occurrences('fleep floop', 'ee')  
occurrences('fleep floop', 'fe')

#Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
#(HINT: Review your notes on *args).

def product(*args):
  product = 1
  for arg in args:
    product = product * arg
  print(product)

product(-1, 4) 
product(2, 5, 5) 
product(4, 0.5, 5)

# Write a function named steps_to_zero that accepts a non-negative integer as an argument, and returns the number of steps it took to reduce the integer to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
# INCORRECT!!!!!!!!
def steps_to_zero(num):
  steps = 0
  curr_num = num
  while curr_num != 0:
    if curr_num % 2 == 0:
      curr_num = curr_num // 2
      steps += 1
    else:
      curr_num = curr_num - 1
      steps +=1
  print(steps)

steps_to_zero(14)