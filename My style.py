set_of_numbers = [value for value in range(1, 1000001)]
print(sum(set_of_numbers))
print(max(set_of_numbers))
print(min(set_of_numbers))


odd_numbers = []
for value in range(1, 21, 2):
    odd_numbers.append(value)

print(odd_numbers)

# short_form
set_of_odd_integers = [value for value in range(1, 21, 2)]
print(set_of_odd_integers)

cubes_of_first_10 = [i**3 for i in range(1, 11)]

print(cubes_of_first_10)
i = 1
for values in cubes_of_first_10:
    print(f"cube root {i} is {values}")
    i += 1
