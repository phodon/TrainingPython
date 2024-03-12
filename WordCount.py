from collections import Counter

Text="""
bands which have connected them with another, and to assume among the
powers of the earth, the separate and equal station to which the Laws
of Nature and of Nature's God entitle them, a decent respect to the
opinions of mankind requires that they should declare the causes which
impel them to the separation.  We hold these truths to be
self-evident, that all men are created equal, that they are endowed by
their Creator with certain unalienable Rights, that among these are
Life, Liberty and the pursuit of Happiness.--That to secure these
rights, Governments are instituted among Men, deriving their just
powers from the consent of the governed, --That whenever any Form of
Government becomes destructive of these ends, it is the Right of the
People to alter or to abolish it, and to institute new Government,
laying its foundation on such principles and organizing its powers in
such form, as to them shall seem most likely to effect their Safety
and Happiness. """

for char in '.-,\n':
    Text = Text.replace(char, " ")
Text = Text.lower()

word_list = Text.split()
#print(word_list)

def word_count_using_for_loops(a): 
    #dictionary
    d = {}

    for word in word_list:
        d[word] = d.get(word, 0)+1
    
    tuple_list = [(key,value) for key,value in d.items()]
    tuple_list.sort(reverse=True)
    return tuple_list

# print(word_count_using_for_loops(word_list))

def word_count_not_using_get_method(a):
    d = {}

    for word in a:
        if word not in d:
            d[word] = 0
        d[word]+=1

    word_freq = []
    for key,value in d.items():
        word_freq.append((value,key))

    word_freq.sort(reverse=True)

    return word_freq

# print(word_count_not_using_get_method(word_list))

def word_count_using_inbuilt_method(a):
    d = {}

    for key in a:
        d[key] = d.get(key,0)+1
    
    sorted_list=sorted(d.items(), key=lambda x: x[0], reverse=True) # key=lambda x: x[0] sort by key, x: x[1] sort by value

    return sorted_list

# print(word_count_using_inbuilt_method(word_list))

def word_count_using_collections_counter(a):
    d = Counter(a).most_common()
    return d

print(word_count_using_collections_counter(word_list))




