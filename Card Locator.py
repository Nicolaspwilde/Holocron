def card_locator(cards, query):
    position = 0
    occurrence = 0
    first_match_pos = -1

    while position < len(cards):
        if cards[position] == query:
            occurrence += 1
            if first_match_pos == -1:
                first_match_pos = position + 1  # 1-based index
        position += 1

    if occurrence > 0:
        return first_match_pos, occurrence
    else:
        return -1, 0


cards_input = input("Enter cards separated by commas: ")
cards = cards_input.split(",")
query = input("Enter the card you want to find: ")

first_pos, count = card_locator(cards, query)

if first_pos != -1:
    print(f"The card '{query}' is at position {first_pos} and appeared {count} times.")
else:
    print("Card not found")
