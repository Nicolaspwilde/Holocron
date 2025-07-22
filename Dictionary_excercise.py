Cars_rating = {}

while True :
    cars_name = input("Enter the car Name: ")
    if cars_name == 'stop':
        break
    Cars_rating[cars_name] = input("Enter rating out of 5 :")

print(f"{Cars_rating} \n")
dictionary = {}
i = 0
key = input("Enter the key for dictionary").split(" ")
value = input("Enter the valur for dictionary").split(" ")
for i in range (len(key)):
    if i < len(value):
        dictionary[key[i]] = value[i]
    else :
        dictionary[key[i]] = None
print("Final Dictionary")
print(dictionary)