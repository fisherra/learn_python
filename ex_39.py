# dictionaries

# basically a look-up table in R 

# here's how a list works 

a_list = ['this', 'is', 1, 'list', True, False, None, 123.2]

print(a_list[0])
print(a_list[1])
print(a_list[-1])

# here's how a dictionary works

a_dictionary = {'first entry': 123.321, 'x': 'Walmart', 'name of entry 3': 'entry 3 content'}

print(a_dictionary['first entry'])

a_dictionary['fourth entry'] = 72
print(a_dictionary['fourth entry'])

del a_dictionary['x']
print(a_dictionary)

# creating and accessing a larger dictionary 

# create countries dict
countries = {
'Thailand': 'TH',
'Canada': 'CA',
'Brazil': 'BR',
'South Africa': 'SA',
'Unted States': 'US'
}

# create cities dict
cities = {
'TH': 'Bangkok', 
'Canada': 'Vancouver',
'Brazil': 'Rio De Janeiro'
}

# a different way to add to the dict
cities['South Africa'] = 'Cape Town'
cities['United States'] = 'New York City'

# access the dict
print('-' * 10)
print("The United States has", cities['United States'])
print("Brazil has", cities["Brazil"])

# dictionaries through dictionaries
print('-' * 10)
print("Thailand has", cities[countries['Thailand']])
# because countries['Thailand'] = 'TH', and cities['TH'] = 'Bangkok

