def find_number_in_list(numbers, target):
    """
    Find the number of occurrences of a target number in a list and return the total positions checked and first occurrence position.
    :param numbers: List of numbers (as strings) to search in."""
    position = 0
    occurrences = 0
    first_occurrence = -1
    # Iterate through the list using a while loop
    while position < len(numbers):
        if numbers[position] == target:
            occurrences += 1
            if first_occurrence == -1:
                first_occurrence = position + 1
        position += 1  # always increment

    return occurrences, position,first_occurrence  # position will be len(numbers)

# Example usage
number_list = input("Enter a list of numbers separated by commas: ").split(",")
target_number = input("Enter a number to find in the list: ")
occurrences, total_positions,first_occurrence = find_number_in_list(number_list, target_number)
if occurrences == 0:
    first_occurrence = -1  
    print(f"{target_number} is not present in the list.")
else:
    print(f"{target_number} occurred {occurrences} time(s) in the list. and it took {total_positions} positions to check.with first occurrence at position {first_occurrence}.")
