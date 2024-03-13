first_name = 'John'
last_name = 'Doe'
favorite_hobby = 'Python'
sports_hobby = 'gym'
age = 82

fullname = first_name+" "+last_name
hobbies = []
hobbies.append(favorite_hobby)
hobbies.append(sports_hobby)
my_dict = {
    'name': fullname,
    'age': age,
    'hobbies': hobbies
}

assert my_dict == {
        'name': 'John Doe',
        'age': 82,
        'hobbies': ['Python', 'gym']
    }

dict1 = dict(key1='This is not that hard', key2='Python is still cool')
dict2 = {'key1': 123, 'special_key': 'secret'}
# This is also a away to initialize a dict (list of tuples) 
dict3 = dict([('key2', 456), ('keyX', 'X')])

my_dict ={}
my_dict.update(dict1)
my_dict.update(dict2)
my_dict.update(dict3)

special_value = my_dict.pop('special_key')

assert my_dict == {'key1': 123, 'key2': 456, 'keyX': 'X'}
assert special_value == 'secret'

# Let's check that the originals are untouched
assert dict1 == {
        'key1': 'This is not that hard',
        'key2': 'Python is still cool'
    }
assert dict2 == {'key1': 123, 'special_key': 'secret'}
assert dict3 == {'key2': 456, 'keyX': 'X'}

# print(my_dict)