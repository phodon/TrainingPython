import random

def list_of_hexa_colors():
    tmp = "0123456789abcdef"
    result = "#"
    for i in range(6):
        result+= random.choice(tmp)
    return result

def list_of_rgb_colors():
    arr = [x for x in range(0,256)]
    result = []
    for i in range(3):
        result.append(random.choice(arr))
    return result

def generate_colors(key,value):
    result = []
    if key == "hexa":
        for i in range(value):
            result.append(list_of_hexa_colors())
    if key == "rgb":
        for i in range(value):
            result.append(list_of_rgb_colors())

    print(result)

generate_colors('rgb', 3)
