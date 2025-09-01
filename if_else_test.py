Alien_color = ["green", "yellow", "red"]
Alien = input("enter colour of alien from red,yellow,green : ").lower()
if Alien == "green":
    print("player earned 5 points")
elif Alien == "yellow":
    print("player earned 10 points")
elif Alien == "Red":
    print("player earned 15 points")


# Phrase of Life based on Age Calculator

age_of_person = int(input("Enter the age in number\t"))
if age_of_person < 2:
    print(f"Person is a baby of {age_of_person} age")
elif 2 <= age_of_person < 4:
    print(f"Person is a toddler")
elif 4 <= age_of_person < 13:
    print(f"Person is a kid of age {age_of_person}")
elif 13 <= age_of_person < 20:
    print(f"Person is a teenager of age {age_of_person}")
elif 20 <= age_of_person < 65:
    print(f"Person is a adult of age {age_of_person}")
else:
    print(f"Person is an old man of age {age_of_person}")
