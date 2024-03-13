def sum_numbers_in_file(input_file):
    sum = 0
    with open(input_file, encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            sum+=float(line)
        return sum
    
def find_first_words(input_file):
    result = []
    with open(input_file,encoding='utf8') as f:
        for line in f.readlines():
            line = line.strip()
            if line == '':
                result.append(line)
            else:
                tmp = [word for word in line.split()]
                result.append(tmp[0])
        return result
    

# print(sum_numbers_in_file('test.txt'))
print(find_first_words('test.txt'))