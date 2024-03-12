import json

def count_line_and_word():
    with open("speech_barack_obama.txt", encoding='utf-8') as f:
        line_count = 0
        word_count = 0
        for line in f:
            line_count+=1
            Text = line.replace(".,-:\n"," ")
            Text = Text.split()
            arr = [word for word in Text]
            word_count+=len(arr)
        print(line_count,word_count)

def most_spoken_languages(filename, number):
    with open(filename,encoding='utf8') as f:
        data = json.load(f)
        rank_language = {}
        for x in data:
            arr = [language for language in x["languages"]]
            for language in arr:
                rank_language[language] = rank_language.get(language,0)+1

        sorted_list = sorted(rank_language.items(),key = lambda x:(x[1],x[0]))
        for i in range(number+1):
            tmp = sorted_list.pop()
            print(tmp)

# most_spoken_languages('./countries_data.json',10)

def most_populated_countries(filename,number):
    with open(filename,encoding='utf-8') as f:
        data = json.load(f)
        return [{'country': item['name'], 'population': item['population']} for item in sorted(data, key=lambda item: item['population'], reverse=True)][:number]
            

print(most_populated_countries('./countries_data.json',10))


