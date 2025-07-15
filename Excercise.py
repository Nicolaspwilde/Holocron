# From a list of names, remove all names that are exactly "nishtha"
# (case-insensitive) and print the updated list.

# list_of_names = ["Nishtha","Abhimanyu","Sanchit","Abhaash"]*10
# name_to_be_removed = 'Nishtha'
# updated_list = []
# for name in list_of_names:
#     if name.lower() != name_to_be_removed.lower():
#         updated_list.append(name)
#
# for name in updated_list:
#     print(name)

# index = 0
#
# for index in range(0, len(list_of_names),3):
#     for name in list_of_names:
#         print(f"name at {index} is {list_of_names[index]}")
#         break

guests = ['NISHTHA', 'sanchit', 'SANCHIT', 'abhaash', 'Abhaash', 'nishtha']
guestses =[]
standarised_guests = []
for name in guests:
    guestses.append(name.lower())
    # name = guest.lower()
    for name in guestses:
        if name not in standarised_guests:
            standarised_guests.append(name)
for name in standarised_guests:
    print(name)


# for guest in guests:
#     standarised_guests.append(guest.lower())
#
# not_duplicate_guest = []
# for guest in standarised_guests:
#     if guest not in not_duplicate_guest:
#         not_duplicate_guest.append(guest)
#
# for guest_final in not_duplicate_guest:
#     print(guest_final.upper())
#
