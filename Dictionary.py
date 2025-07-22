# Dictionary in python is a collection of key value pairs. Each key is connected to a value and
# you can use the key to access the value associated with it.

Dictionary_sample = {'Red' :'45','green' : '67'}

print(Dictionary_sample['Red'])

points = Dictionary_sample['green']
print(f"the points you earned is {points}")

Dictionary_sample['Blue'] =  input("Enter the dictionary value")
Dictionary_sample['yellow'] = 80
print(Dictionary_sample)

empty_dictionary = {}

while True:
    key = input("Enter the key (or type 'stop' to finish): ")
    if key.lower() == "stop":
        break
    value = input(f"Enter the value for '{key}': ")
    empty_dictionary[key] = value  # add to dictionary

print("Your final dictionary:")
print(empty_dictionary)

empty_dictionary = {}

# Enter all keys
keys = input("Enter all keys separated by spaces: ").split(',')

# Enter all values
values = input("Enter all values separated by spaces: ").split(',')

# Combine them into the dictionary
for i in range(len(keys)):
    if i < len(values):
        empty_dictionary[keys[i]] = values[i]
    else:
        empty_dictionary[keys[i]] = None  # if there are fewer values

print("Your final dictionary:")
print(empty_dictionary)
