names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

try:
    first_five_name = names[:4]
    es = names[5]
    ru = names[7]
    print(first_five_name)
    print(es)
    print(ru)
except Exception as e:
    print(e.args)
