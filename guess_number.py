import random

rand_num = random.randint(0, 50)

count = 0

while True:
    user_input = int(input('Enter a number between 0 and 50 \n'))
    count += 1

    if rand_num == user_input:
        print('You\'ve got it')
        break
    elif rand_num > user_input:
        print('Input a larger number. \n')
        continue
    else:
        print('Input a smaller number. \n')

print('You\'ve made it in', count, 'attempts... \n')