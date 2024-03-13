def read_file(path):
    data_file = open(path,'r')
    lines = data_file.readlines()
    line_count = len(lines)
    idx = 0
    empty_lines = 0
    words = []
    numbers = []
    while idx < line_count:
        line = lines[idx]
        line = line.strip()
        if line == '':
            empty_lines+=1
        else:
            is_number = False
            try:
                number = float(line)
                is_number = True
            except Exception:
                pass
                
            if is_number:
                numbers.append(number)
            else:
                words.append(line)
        idx+=1
    data_file.close()

    return empty_lines, numbers, words

def get_max_value(numbers):
    max_value = None
    if len(numbers)>0:
        max_value = numbers[0]
        for idx in range(len(numbers)):
            if numbers[idx]>max_value:
                max_value = numbers[idx]
    return max_value

def words_to_lowercase(words):
    lowercased = []
    for idx in range(len(words)):
        value = words[idx].lower()
        lowercased.append(value)
    return lowercased

def get_most_common_words(words):
    word_count = {}
    idx = 0
    while idx<len(words):
        value = words[idx]
        if value not in word_count.keys():
            word_count[value]=1
        else:
            word_count[value]+=1
        idx+=1
    max_count = 0
    for value in word_count.values():
        if value > max_count:
            max_count = value
    
    most_common_word = []

    for word in word_count.keys():
        count = word_count[word]
        if count == max_count:
            most_common_word.append(word)

    most_common_word = sorted(most_common_word)
    return most_common_word, max_count

def _make_report(missing_values, numbers, words):
    max_value = get_max_value(numbers)
    lower_case_words = words_to_lowercase(words)
    most_common_info = get_most_common_words(lower_case_words)
    most_common_words = most_common_info[0]
    most_common_count = most_common_info[1]

    most_common_str = ''
    for idx in range(len(most_common_words)):
        most_common_str += most_common_words[idx] + ', '
    # remove the last comma and space
    most_common_str = most_common_str[0:len(most_common_str) - 2]

    report = ('missing values: {}\n'
              'highest number: {}\n'
              'most common words: {}\n'
              'occurrences of most common: {}\n'
              '#####\n'
              'numbers: {}\n'
              'words: {}').format(missing_values, max_value, most_common_str,
                                  most_common_count, numbers, lower_case_words)

    return report

missing_values, numbers, words = read_file("test.txt")
print(_make_report(missing_values,numbers,words))