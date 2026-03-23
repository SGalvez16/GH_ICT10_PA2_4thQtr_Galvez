# Object-Oriented Programming
from pyscript import display
from js import document

'''
class car:
    def __init__(self, brand, color, model, type):
        self.brand = brand
        self.color = color
        self.model = model
        self.type = type

    def honk(self):
        display('Beep'*3, target='output')


# Instantiating an object
car1 = car('Mitsubishi', 'blue', 'lancer', 'sedan') # Mergal's
car1.honk()
car2 =  car('Tesla', 'pink', 'model y', 'EV') # Ainah's

display(f'Mergal\'s car is a {car1.brand}. The color is {car1.color}.', target = 'output')
display(f'Ainah\'s car is a {car2.brand}. The color is {car2.color}.', target = 'output')

class Lexus(car): # creatign a child class
    pass

car1 = Lexus('Lexus', 'grey', 'LM', 'Van')
car1.honk()

display(f'Law\'s car is a {car1.brand}. The color is {car1.color}', target = 'output')

class Dog:
    def __init__(self, name, age, color, breed):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed

dog1 = Dog('Luna', 1, 'black', 'German Shepered')
dog2 = Dog('Ollie', 7, 'white', 'Maltese Shit Tzu')

    # Create a method
'''

# Create a method
# create a child class
# Instantiate 3 objects
# get the value from a form
# repository link: GH_ICT10_PA2_4thQtr_Galvez
# submit the repository link in the VN

def dog(e):

    name = document.getElementById('name').value
    age = int(document.getElementById('age').value)
    color = document.getElementById('color').value
    breed = document.getElementById('breed').value

    display(f'Your dog is named {name}. The age is {age}. Color {color}. {breed} is the breed')


    class Dog:
        def __init__(self, name, age, color, breed):
            self.name = name
            self.age = age
            self.color = color
            self.breed = breed

        def describe(self):
            display(f'Dog is named {self.name}. The color is {self.color}.')

    class Puppy(Dog):
        pass

    dog1 = Puppy('Snoopy', 4, 'white', 'Bulldog')

    dog2 = Dog('Cupcake', 1, 'white', 'Bulldog')
    dog3 = Dog('Spotty', 3, 'brown', 'Corgi')
    dog4 =  Dog('Whitey', 2, 'golden brown', 'Poodle')
    dog5 =  Dog('Ollie', 5, 'beige', 'Shit Tzu')

    display(f'Gary\'s dog is named {dog1.name}. The color is {dog1.color}.', target = 'output')
    display(f'Alex\'s dog is named {dog2.name}. The color is {dog2.color}.', target = 'output')
    display(f'Kristine\'s dog is named {dog3.name}. The color is {dog3.color}.', target = 'output')
    display(f'Oliver\'s dog is named {dog4.name}. The color is {dog4.color}.', target = 'output')
    display(f'Oliver\'s dog is named {dog5.name}. The color is {dog5.color}.', target = 'output')