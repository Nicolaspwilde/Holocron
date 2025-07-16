#pizza toppings program.

print("welcome to domino's pizza\nwe have many toppings available\nyou can also add multiple toppings")
list_of_toppings = ['paneer','corn','chicken','mushroom']

customer_input = input(f"pls enter your toppings choice these are available toppings{list_of_toppings}").split(' ')
list_by_customer = [preference.strip().lower() for preference in customer_input]

for toppings in list_by_customer:
    if toppings in list_of_toppings:
        print(f"adding custom toppings {toppings}")
    else:
        print(f"Sorry this option not available {toppings}") 
        suggestion = input("Do you want to make suggestion to add this toppings to list y or n ?").lower()
        if suggestion == 'y':
            suggestion_for_list = input("enter the topping name with spaces").split(' ')
            new_toppings = [suggested_toppings.strip().lower() for suggested_toppings in suggestion_for_list]
            print(', '.join(new_toppings))
            for new in new_toppings:
                list_of_toppings.append(new)
                print(f"your suggestion {new_toppings} was added")
        elif suggestion == 'n':
            print("sorry we couldn't serve you")
            