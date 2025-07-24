# Cars_rating = {}
#
# while True :
#     cars_name = input("Enter the car Name: ")
#     if cars_name == 'stop':
#         break
#     Cars_rating[cars_name] = float(input("Enter rating out of 5 :"))
#
# print(f"{Cars_rating} \n")
# dictionary = {}
# i = 0
# key = input("Enter the key for dictionary").split(" ")
# value = input("Enter the valur for dictionary").split(" ")
# for i in range (len(key)):
#     if i < len(value):
#         dictionary[key[i]] = value[i]
#     else :
#         dictionary[key[i]] = None
# print("Final Dictionary")
# print(dictionary)
#
# #forking with different ideas
#
# while True:
#     key = input("key")
#     if key.lower() == 'stop' :
#         break
#     value = input("value")
#     dictionary[key] = value
# print(dictionary)
#
# my_value = dictionary.get('apple','No apple was found.')
# print(my_value)

#Why we need looping ?
Dictionary_sample = {'Red' :'45','green' : '67'}

for key,value in Dictionary_sample.items():
    print(f"key\n : {key}")
    print(f"value\n : {value}")

