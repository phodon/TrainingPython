import csv

def extract_email():
    with open('email_exchanges_big.txt', encoding='utf-8') as f:
        Text = f.read()
        char = '><)(=?/,;}{:-[]\n'
        Text = Text.replace(char, " ")
        word_list = { word for word in Text.split() if '@' in word}
        print(word_list)

def read_csv():
    with open('hacker_news.csv') as f:
        csv_reader = csv.reader(f,delimiter=',')
        line_count_python = 0
        line_count_java = 0
        line_count_javascrip = 0
        for row in csv_reader:
            tmp = ""
            for x in row:
                tmp+=str(row)+" "
            if "python" in tmp or "Python" in tmp:
                line_count_python+=1
            if "Java" in tmp and "Javascript" not in tmp:
                line_count_java+=1 
            if "javascript" in tmp or "Javascript" in tmp or "JavaScript" in tmp:
                line_count_javascrip+=1  
        print(f'Number of lines has python:  {line_count_python}')
        print(f'Number of lines has Java:  {line_count_java}')
        print(f'Number of lines has JavaScript:  {line_count_javascrip}')

read_csv()
        

# extract_email()