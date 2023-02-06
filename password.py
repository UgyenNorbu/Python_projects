master_pwd = input('Enter the master password...')

def view_pwd():
    with open('pwd.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name, pwd = data.split('|')
            print('Username: ', name, '|', 'Password:', pwd)


def add_pwd():
    user_name = input('Enter username. \n')
    pwd = input('Enter password. \n')

    with open('pwd.txt', 'a') as f:
        f.write(user_name + '|' + pwd + '\n')


while True:
    mode = input('Select the mode: View or Add... or pres Q to quit. \n').lower()
    if mode == 'q':
        break

    if mode == 'view':
        view_pwd()
    elif mode == 'add':
        add_pwd()
    else:
        print('Invalid option....')