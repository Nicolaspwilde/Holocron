name = input("Enter the name of the person :").title()
# Exercise 2.3
print(f"Hello\t{name} would you like to learn some Python today ?")
# Exercise 2.4
print(name.upper(), name.lower(), name.title())
# Excercise 2.5,2.6,2.7
Famous_person = input("Name of the famouse person :").removeprefix("Mr.").rstrip()
print(Famous_person)
message = (
    f'{Famous_person} once said, "You were my brother Anakin,\n you were the chosen one you were supposed\t'
    f'destroy the sith not join them"'
)
print(message)

print(Famous_person.rstrip(), Famous_person.lstrip(), Famous_person.strip())
