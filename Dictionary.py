# Dictionary in python is a collection of key value pairs. Each key is connected to a value and
# you can use the key to access the value associated with it.

Dictionary_sample = {'Red' :'45','green' : '67'}

print(Dictionary_sample['Red'])

points = Dictionary_sample['green']
print(f"the points you earned is {points}")

Dictionary_sample['Blue'] =  input("Enter the dictionary value")
Dictionary_sample['yellow'] = 80
print(Dictionary_sample)
