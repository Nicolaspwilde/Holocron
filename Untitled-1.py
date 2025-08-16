# while

Number = int(input("Enter the number you want to double "))

flag = True
while flag :
    Number += Number
    print(f" the double number {Number}")
    chance_to_stop = input("do you want to st gvbop ? ").lower().strip()
    if chance_to_stop == 'yes':
        flag = False
    
#WRITE a program to repeat the 

repeater = "I will repeat everything you say till you say stop: "
repeater += "Enter the word "

flag = True
while flag: 
    message = input(repeater).lower()
    if message == 'stop':
        flag = False
        break
    else :
        print(message)