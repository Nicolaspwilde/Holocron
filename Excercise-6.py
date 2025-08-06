My_information = {'First_name' : 'Abhimanyu','Middle_name': 'Singh','Last_name':'Negi','Age':'25','city':'Delhi'}
print(f"My name is {My_information['First_name']} {My_information['Middle_name']} {My_information['Last_name']}")

print("this is sample dictionary :")
for info in My_information.values():
    print(info.title())

my_dict = {
    'a': 1,
    'b': 2,
    'c': 1,  # duplicate value
    'd': 3,
    'e': 2   # duplicate value
}
print("unique values : ")
for value in sorted(set(my_dict.values())):
    print(value)

rivers = {
    "Nile": ["Egypt", "Sudan", "Uganda"],
    "Amazon": ["Brazil", "Peru", "Colombia"],
    "Ganga": ["India", "Bangladesh"],
    "Yangtze": ["China"],
    "Mississippi": ["United States"],
    "Danube": ["Germany", "Austria", "Hungary", "Romania", "Bulgaria", "Serbia"],
    "Volga": ["Russia"],
    "Mekong": ["China", "Laos", "Thailand", "Cambodia", "Vietnam"],
    "Thames": ["United Kingdom"],
    "Indus": ["Pakistan", "India", "China"]
}

for river in rivers.keys():
    if river == 'Indus':
        countries = ' , '.join(rivers[river])
        print(f"{river} is an important river which flows in these countries that are : {countries} ")
    if river == 'Nile':
        countries = ' , '.join(rivers[river])
        print(f"{river} is an important river which flows in middle east in countries like this : {countries}")

# Nested list
empty_list = []
for elements in range (30):
    new_elements = {'a':0,'b':1}
    empty_list.append(new_elements)
# show the first 5 aliens.

for element in empty_list:
    if element['a'] == 0 :
        element['a'] = -1

for element in empty_list[:5]:
    print(element)



