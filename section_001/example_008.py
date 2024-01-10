# Student: Pedro Henrique Resende Ribeiro
# Description: Input function and casting
# Date: 2024-01-10 - Time: 07:50

number = input('Enter a number: ')
print('Number:', number)
print('Type:', type(number))

number = int(input('Enter a number: '))
print('Number:', number)
print('Type:', type(number))

name = input('Enter your name: ')
print('Name:', name)

age = int(input('Enter your age: '))
print('Age:', age)

height = float(input('Enter your height: '))
print('Height', height)

weight = float(input('Enter your weight: '))
print('Weight', weight)

imc = weight / height ** 2
print('IMC:', imc)
