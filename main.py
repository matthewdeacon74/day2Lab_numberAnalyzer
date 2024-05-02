# get user name
user_name = input('What is your name? ')

# set initial loop condition
is_continue=True
is_valid=False

while is_continue == True:
    # get number input
    user_number = int(input('enter an integer from 1 to 100: '))
    if user_number > 0 and user_number < 101:
        is_valid=True
    print(f'{user_name} picked ', user_number)
    # determine odd or even for each condition later
    is_even = user_number % 2 == 0

    # print different messages based on input number
    if is_valid and user_number <60 and not is_even:
        print(f'{user_number} is Odd and less than 60')
    if is_valid and 2 <= user_number <= 24 and is_even:
        print(f'{user_number} is Even and less than 25')
    if is_valid and is_even and 26 <= user_number <= 60:
        print(f'{user_number} is Even and between 26 and 60 inclusive')
    if is_valid and is_even and user_number > 60:
        print(f'{user_number} is even and greater than 60')
    if is_valid and not is_even and user_number > 60:
        print(f'{user_number} is odd and greater than 60')
    elif not is_valid:
        print(f'{user_number} is not a valid choice, number must be from 1 to 100.')

    user_continue = input(f'Try another number, {user_name}? (y/n): ')
    if user_continue == 'n':
        print(f'See you next time, {user_name}!')
        is_continue = False
    else:
        is_valid = False