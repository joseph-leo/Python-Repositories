birthdays = {}

birthdays['Luke Skywalker'] = '5/24/19'
birthdays['Obi-Wan Kenobi'] = '3/11/57'
birthdays['Darth Vader'] = '4/1/41'

if 'Yoda' not in birthdays:
    birthdays['Yoda'] = 'Unknown'
if 'Darth Vader' not in birthdays:
    birthdays['Darth Vader'] = 'Unknown'

for name in birthdays:
    print(name, birthdays[name])

del(birthdays['Darth Vader'])

for name in birthdays:
    print(name, birthdays[name])

new_dict = dict([('Luke Skywalker', '5/24/19'), ('Obi-Wan Kenobi', '3/11/57'),
      ('Darth Vader', '4/1/41')])
print(new_dict)
