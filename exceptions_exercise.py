def sum_of_list(values):
    sum = 0
    for val in values:
        try:
            numeric_val = float(val)
        except Exception as e:
            print(e)
        sum+=numeric_val
    return sum

class TooLongString(Exception):
    pass

def verify_short_string(s):
    if len(s)>10:
        raise TooLongString(len(s))

try:
    verify_short_string('this i')
except TooLongString as e:
    print(e)
    pass
else:
    print("vi anh la ngoai le cua em")
    assert True
    

# list1 = [1, 2, 3]
# list2 = ['1', 2.5, '3.0']
# list3 = ['', '1']
# list4 = []
# list5 = ['John', 'Doe', 'was', 'here']
# nasty_list = [KeyError(), [], dict()]

# assert sum_of_list(list1) == 6
# assert sum_of_list(list2) == 6.5
# assert sum_of_list(list3) == 1
# assert sum_of_list(list4) == 0
# assert sum_of_list(list5) == 0
# assert sum_of_list(nasty_list) == 0