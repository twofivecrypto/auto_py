import pprint

cats = [
    {'name': 'Zophie',
    'desc': 'chubby'},
    {'name': 'Pooka',
    'desc': 'fluffy'}
    ]
print(pprint.pformat(cats))#[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
fileObj = open('myCats.py', 'w')
print(fileObj.write('cats = ' + pprint.pformat(cats) + '\n'))#83



