name = 'john Doe'
l = len(name)

if l>20:
    print('Name "{}" is more than 20 chars long'.format(name))
    length_description = 'long'
elif l>15 and l<=20:
    print('Name "{}" is more than 15 chars long'.format(name))
    length_description = 'semi long'
elif l>10 and l<=15:
    print('Name "{}" is more than 10 chars long'.format(name))
    length_description = 'semi long'
elif l>7 and l<=10:
    print('Name "{}" is 8, 9 or 10 chars long'.format(name))
    length_description = 'semi short'
else:
    print('Name "{}" is a short name'.format(name))
    length_description = 'short'

assert length_description == 'semi short'