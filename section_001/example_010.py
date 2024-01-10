# Student: Pedro Henrique Resende Ribeiro
# Description: Logical and relational operators
# Date: 2024-01-10 - Time: 13:20

number = 10

if number > 10:
    print('>')

if number >= 10:
    print('>=')

if number < 10:
    print('<')

if number <= 10:
    print('<=')

if number == 10:
    print('==')

if number != 10:
    print('!=')

if number > 10 and number < 20:
    print('and')

if number > 10 or number < 20:
    print('or')

if not number > 10:
    print('not')

option = input('Do you want to continue? [y/n] ')

if option == 'y' or option == 'n':
    print('Valid option...')
else:
    print('Invalid option...')
