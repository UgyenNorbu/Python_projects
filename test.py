import random

symbol_count = {
    'A': 3,
    'B': 2,
    'C': 3,
    'D': 1
}

all_symbols = []
for key, val in symbol_count.items():
        for _ in range(val):
            all_symbols.append(key)

slot = [['#' for x in range(3)] for x in range(3)]
for i in range(3):
    for j in range(3):
        slot[i][j] = random.choice(all_symbols)
        all_symbols.remove(slot[i][j])

print(slot)
print(all_symbols)
