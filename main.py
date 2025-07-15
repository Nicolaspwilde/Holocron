import time
list_of_guest = ['Nishtha','Sanchit','Abhishek','Abhaash','Nishtha']*300

start_time = time.time()

guest = 'Nishtha'.lower()
counter = 0
non_interest_count = 0

for friend in list_of_guest:
    if guest == friend.lower():
        counter += 1
    else:
        non_interest_count += 1

print(counter)
print(non_interest_count)
unique_guest = set(friends.lower() for friends in list_of_guest)
for allies in unique_guest:
    if guest == allies.lower():
        print(f"Welcome my love {allies}")
    else:
        print(f"Enter my good friend {allies}")
