unsure_list = ['Nishtha','Abhimanyu']
names_to_add = input("Enter the name : ").split(",")
for new_name in names_to_add:
    unsure_list.append(new_name.strip())
confirmed_list  = []

while unsure_list:
    confirmed_list = unsure_list.pop()
    print(f"behold the confirmed relationship : {confirmed_list.title()}")
    
    
# other approach
unsure_list = []
confirmed_list  = []
unconfirmed_list = []
names_to_add =input("Enter the names for the list : ").split(',')
for names in names_to_add :
    unsure_list.append(names.strip())

for names in unsure_list:
    decision = input(f"Do you want to confirm this name {names}  say yes or no:").lower()
    if decision == 'yes' :
        confirmed_list.append(names)
    else :
        unconfirmed_list.append(names)


print(f"List of confirmed names : {confirmed_list}")
print(f"list of names unconfirmed : {unconfirmed_list}")