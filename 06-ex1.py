import string, random

def randum_user_id():
    result=""
    anpha = string.ascii_letters
    number = string.digits
    full = anpha + number
    for i in range(6):
        result+=random.choice(full)
    return result

def user_id_gen_by_user(dd):
    result=""
    anpha = string.ascii_letters
    number = string.digits
    charaters = anpha + number
    for i in range(dd):
        result+=random.choice(charaters)
    return result


def rgb_color_gen():
    arr = [x for x in range(0,256)]
    result = []
    for i in range(3):
        result.append(random.choice(arr))
    return result

# print(randum_user_id())
# arr = input().split()
# for i in range(int(arr[1])):
    print(user_id_gen_by_user(int(arr[0])))

print(rgb_color_gen())
