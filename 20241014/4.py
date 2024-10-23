from collections import defaultdict

dict_deck = defaultdict(set)
dict_players = defaultdict(set)
max_size = 0

s = input()
while s:
    a, b = s.split(' / ')
    if a.isnumeric():
        dict_deck[a].add(b)
    else:
        dict_players[a].add(b)
    s = input()

dict_player_sizes = {}
for player, decks in dict_players.items():
    total_cards = set()
    for deck in decks:
        total_cards.update(dict_deck[deck])
    size = len(total_cards)
    dict_player_sizes[player] = size
    max_size = max(max_size, size)

result = [player for player, size in dict_player_sizes.items() if size == max_size]

print(*sorted(result), sep="\n")