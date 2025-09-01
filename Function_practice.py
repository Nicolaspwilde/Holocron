def full_name_creator(first_name, middle_name, last_name):
    """Doc_string to combine the functions"""
    if middle_name:
        full_name = f"{first_name}_{middle_name}_{last_name}"
    else:
        full_name = f"{first_name}_{last_name}"
    return full_name


First_name = input("Enter your First Name : ").replace(" ", "").strip().title()
Middle_name = input("Enter your Middle Name : ").replace(" ", "").strip().title()
Last_name = input("Enter your last Name : ").replace(" ", "").strip().title()
title = full_name_creator(First_name, Middle_name, Last_name)
print(title)
