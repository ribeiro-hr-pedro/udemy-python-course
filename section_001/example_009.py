# Student: Pedro Henrique Resende Ribeiro
# Description: If, elif and else
# Date: 2024-01-10 - Time: 12:45

option = input('Do you want to continue? [y/n] ')

if option == 'y':
    print('Continue...')
elif option == 'n':
    print('Stop...')
else:
    print('Invalid option!')

age = 28

if age < 18:
    print('Minor')
elif age >= 18:
    print('Adult')
else:
    print('Invalid age!')

number_1 = int(input('Enter the 1st number: '))
number_2 = int(input('Enter the 2nd number: '))

if number_1 > number_2:
    print(f'{number_1} is greater than {number_2}')
elif number_1 < number_2:
    print(f'{number_2} is greater than {number_1}')
else:
    print('The numbers are equal')
