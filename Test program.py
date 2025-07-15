players = ['Michael', 'Ralph', 'David', 'Scott', 'Pete', 'Joe', 'Chris', 'Andy']
print("Full team list:")
for member in players:
    print(member)

print("\nThe captains are:")
for member in players[0:2]:
    print(member)

print("\nThese are starting players:")
for member in players[2:5]:
    print(member)

print("\nThese are bench players:")
for member in players[5:]:
    print(member)

print(f"\nTotal players: {len(players)}")

# Middle 3 players
mid = len(players) // 2
print("\nMiddle 3 players:")
print(players[mid - 1])
print(players[mid])
print(players[mid + 1])
