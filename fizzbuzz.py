# Fizz Buzz function
# def fizz_buzz(max_num):
#     for num in range(1, max_num):
#         if num % 3 == 0 and num % 5 == 0:
#             print('{} is FizzBuzz'.format(num))
#         elif num % 3 == 0:
#             print(f'{num} is Fizz')
#         elif num % 5 == 0:
#             print(f'{num} is Buzz')
#         else:
#             print(num)

# fizz_buzz(31)

#----------Control Flow Lesson----------

# floor = "sticky"
# walls = "clean"
# if floor == "sticky":
#     print("Clean the floor! It's sticky!")

# if walls =="sticky":
#     print("Clean the walls! They're sticky")
# else: 
#     print("The walls are clean!")
# color = ""
# while color != quit:
#     color = input('Enter "green", "yellow", "red": ').lower()
#     if color == "green":
#         print("Go!")
#     elif color == "yellow":
#         print("Go faster!")
#     elif color == "red":
#         print("Stop!")
#     elif color == "quit":
#         break
#     else:
#         print("Bogus!")

# names = ["Tom", "Deborah", "Murray", "Axel"]
# for name in names:
#     print(name)

# for num in range(5):
#     print(num)

# for even in range(2, 10, 2):
#     print(even)

# for descent in range(10, 0, -1):
#     print(descent)

#---------- Python Containers ----------
student = {
    'name' : 'Maria',
    'course' : 'SEI',
    'current_week' : '7'
}

name = student['name']
student['name'] = 'Tina'

# print(student.get('skills', {'HTML': 5, 'JAVASCRIPT': 4}))
# del student['course']

# if 'course' in student:
#   print( f"{student['name']} is enrolled in {student['course']}")
# else:
#   print( f"{student['name']} is not enrolled in a course")

# student['age'] = 21

# for item_tuple in student.items():
#     print( f'key = {item_tuple[0]} / value = {item_tuple[1]}')
# print(len(student))
# print(student.items())

GQs_5_things_daniel_merritt_cannot_live_without = {
    'saxophone' : 'in my office',
    'brewzilla' : 'in the basement',
    'fresh keg of hombrewed beer' : 'chilled in the kegerator',
    'toothbrush' : 'outside, so the rain can clean it',
    'lucky ring' : "on the mantle. I never wear it. Can't risk losing that luck",
}

# for thing in GQs_5_things_daniel_merritt_cannot_live_without.items():
#     print(f"My {thing[0]} is kept {thing[1]}")

# colors = ["red", "green", "blue"]
# print(len(colors))
# for idx, color in enumerate(colors):
#     print(idx, color)

# scores = [
#     {
#         'name': 'name of the player',
#         'points': 25
#     }
# ]

# scores.append({'name' : 'Dikembe Mmtumbo', 'points': 16})

# for score in scores:
#     print( f"{score['name']} scored {score['points']} points")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [n * n for n in nums]
even_squares = [n * n for n in nums if (n * n) % 2 == 0]

#above is a shortening of the below
# even_squares = []
# for n in nums:
#   square = n * n 
#   if square % 2 == 0:
    # even_squares.append(square)
