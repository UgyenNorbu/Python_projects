import random
OPTIONS = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0
9
while True:
    user_pick = input('Enter rock/paper/scissors or Q to quit. \n').lower()

    if user_pick == 'q':
        break
    if user_pick not in OPTIONS:
        print('Enter a volid input...')
        continue

    rand_num = random.randrange(0, 3)
    computer_pick = OPTIONS[rand_num]
    print('Computer picked :', computer_pick)

    if user_pick == computer_pick:
        print('Draw...')
    elif user_pick == 'rock' and computer_pick == 'scissors':
        print('You won!!!')
        user_score += 1
    elif user_pick == 'paper' and computer_pick == 'rock':
        print('You won!!!')
        user_score += 1
    elif user_pick == 'scissors' and computer_pick == 'paper':
        print('You won!!!')
        user_score += 1
    else:
        print('Computer won!!!')
        computer_score += 1

print('User vs. Computer')
print('   ', user_score, 'vs', computer_score)
print('\n')

if user_score == computer_score:
    print("RESULT : DRAW")
elif user_score > computer_score:
    print('RESULT: YOU WIN')
else:
    print('RESULT: COMPUTER WIN')
print('\n')