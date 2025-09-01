def add_numbers(n):
    total = 0
    for i in range(n):
        num = float(input("Enter number {}: ".format(i + 1)))
        total += num
    return total


n = int(input("How many numbers do you want to add? "))
result = add_numbers(n)
print("The sum of the {} numbers is: {}".format(n, result))
