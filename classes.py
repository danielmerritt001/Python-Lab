# create a list
# nums = [1, 2, 3]
# print the attributes & methods nums has
# print( dir(nums) )

class Dog():
  next_id = 1
  # init adds attributes on the new object 
  def __init__(self, name, age=0):
    self.name = name
    self.age = age
    self.id = Dog.next_id
    Dog.next_id += 1
  def bark(self):
    print(f'{self.name} says woof!')
  def __str__(self):
    return f'Dog ({self.id}) named {self.name} is {self.age} years old'
  @classmethod
  def get_total_dogs(cls):
    # cls represents the Dog class
    return cls.next_id - 1


Mr_Bojangles = Dog('Mr. Bojangles', 1)

# Mr_Bojangles.bark()

dog = Dog('Lassie')
print(Mr_Bojangles)
print(dog)

class ShowDog(Dog):
  def __init__(self, name, age=0, total_earnings = 0):
    # Add additional parameters AFTER those in the superclass
    Dog.__init__(self, name, age)
    # Now add any new attributes
    self.total_earnings = total_earnings
  def add_prize_money(self, amount):
    self.total_earnings += amount
    print(f'{self.name}\'s new total earnings are {self.total_earnings}')

show_dog = ShowDog('Test Dog')
winky = ShowDog('Winky', 3, 1000)
print(winky) # Yay, inherited the overridden __str__
winky.bark() # Yay, inherited the bark method
print(winky.total_earnings) # -> 1000
winky.add_prize_money(500) # New method that 'Dogs' don't have
print(winky.total_earnings)

# ---------- Vehicle Class Practice ---------- #
# class Vehicle():
#   def __init__(self, make, model, running = False,):
#     self.make = make
#     self.model = model
#     self.running = running
#   def start(self):
#     self.running = True
#     print('running...')
#   def stop(self):
#     self.running = False
#     print('stopped...')
#   def __str__(self):
#     return f'Vehicle is a {self.make} model {self.model} '

# car = Vehicle('Tesla', 'Model S')
# print(car)
# print(car.running)
# car.start()
# print(car.running)
# car.stop()