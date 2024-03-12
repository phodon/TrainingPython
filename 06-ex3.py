from random import randint, random

def shuffle_list(arr):
    random.shuffle(arr)
    return arr

# arr = [1,2,3,4,5,6,7,8,9]
# print(shuffle_list(a))

def func():
    arr = set()
    while len(arr)<7:
        arr.add(randint(0,9))
    print(arr)

func()


