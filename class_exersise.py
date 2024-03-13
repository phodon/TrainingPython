class Calculate:
    def __init__(self,var1, var2):
        self.var1 = var1
        self.var2 = var2
    
    def calculate_power(self):
        return self.var1**self.var2
    
    def calculate_sum(self,var3):
        return self.var1+self.var2+var3
    
class StringManipulator:
    """Docstring of StringManipulator"""

    category = "Manipulator"

    def __init__(self, original):
        self.string = original

    def reverse_words(self):
        words = self.string.split()
        self.string = ' '.join(reversed(words))

    def make_title(self):
        words = self.string.split()
        result = ""
        for word in words:
            result+=word.capitalize()+" "
        self.string = result[:-1]


    def get_manipulated(self):
        return self.string
    
class Dog:

    def __init__(self):
        self.energy = 10
    
    def get_energy(self):
        return self.energy

    def bark(self):
        self.energy-=1
    
    def sleep(self):
        self.energy+=2

doge = Dog()
assert doge.get_energy() == 10

doge.bark()
doge.bark()
doge.bark()
assert doge.get_energy() == 7

doge.sleep()
assert doge.get_energy() == 9

another_doge = Dog()
assert another_doge.get_energy() == 10
    
# assert StringManipulator.__doc__ == "Docstring of StringManipulator"
# assert StringManipulator.category == "Manipulator"

# str_manip = StringManipulator('cOOL pyThON')

# str_manip.reverse_words()
# assert str_manip.get_manipulated() == 'pyThON cOOL'

# str_manip.make_title()
# assert str_manip.get_manipulated() == 'Python Cool'
    
# calc = Calculate(2,3)
# print(calc.calculate_power())
# print(calc.calculate_sum(4))