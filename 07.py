import json
import csv

def write_file():
    with open("test.txt",'a', encoding = 'utf-8') as f:
        f.write("dong chi my len do\n")

def read_file():
    f = open("test.txt",encoding='utf-8')


def saving_json_file():
    person = {
    "name":"Milaan",
    "country":"England",
    "city":"London",
    "skills":["Python", "MATLAB","R"]
    }
    with open('json_example.json', 'w', encoding='utf-8') as f:
        json.dump(person, f, ensure_ascii=False, indent=4)

def saving_csv_file():
    with open('csv_example.csv') as f:
        csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are :{", ".join(row)}')
                line_count += 1
            else:
                print(
                    f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
                line_count += 1
        print(f'Number of lines:  {line_count}')

