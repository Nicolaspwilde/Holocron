car = 'bmw'
car == 'subaru'
print(car == 'subaru')
# we can use it to compare the values of different sections.
list_of_cars = ['subaru','lamborigini','bugati','beetel']

car = 'subaru'

if car not in list_of_cars:
    print(f"this is not a vintage or sports car")
else:
    print(f"this is the car : {car}")