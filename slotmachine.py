import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROW = 3
COL = 3

symbol_count = {
    'A': 3,
    'B': 2,
    'C': 5,
    'D': 6
}

symbol_value = {
    'A': 5,
    'B': 6,
    'C': 3,
    'D': 2
}

def deposit():
    while True:
        amount = input('Enter deposit amount: Nu. ')
        # isdigit( returns True if all the characters are digits, otherwise False
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Enter an amount greater than zero. \n')
        else:
            print('Please enter numbers only. \n')
    return amount

def get_no_of_lines():
    while True:
        lines = input('Enter the number of lines you want to bet on (1-' + str(MAX_LINES) + (') '))
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines. ')
        else:
            print('Enter a NUMBER of lines. ')
    return lines

def get_bet():
    while True:
        amount = input(f'How much would you like to bet on each line?  ')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print('Enter a valid bet amount. \n')
        else:
            print('Please enter numbers only. \n')
    return amount


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for key, val in symbols.items():
        for _ in range(val):
            all_symbols.append(key)
    
    slot = [['#' for x in range(ROW)] for x in range(COL)]

    for i in range(ROW):
        copy_sym = all_symbols[:]
    
        for j in range(COL):
            slot[j][i] = random.choice(copy_sym)
            copy_sym.remove(slot[j][i])
    
    return slot

def print_slot(slot):
    print()
    for i in range(ROW):
        for j in range(COL):
            if j == (COL -1):
                print(slot[i][j])
            else:
                print(slot[i][j], end = ' | ')
    print()

def check_winnings(slot, no_of_lines, value, bet):
    win = 0
    for i in range(no_of_lines):
        base_symbol = slot[i][0]
        for j in range(1, COL):
            if base_symbol != slot[i][j]:
                break
        else:
            win = value[base_symbol] * bet
    return win

def main():
    balance = deposit()
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You do not have enough balance for the bet. Your balance is Nu. {balance}.')
        else:
            break

    slot = get_slot_machine_spin(ROW, COL, symbol_count)
    print_slot(slot)
    tot_wins = check_winnings(slot, lines, symbol_value, bet)
    print(f'You have won Nu. {tot_wins}')

main()