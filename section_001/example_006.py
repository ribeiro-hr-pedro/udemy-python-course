# Student: Pedro Henrique Resende Ribeiro
# Description: Concatenation and repetition operators
# Date: 2024-01-10 - Time: 07:00

concatenation = 'Pedro' + ' ' + 'Henrique'
print(concatenation)

letter_a = 'a' * 10
print(letter_a)

# Precedence of operators
# 1. Parentheses
# 2. Exponentiation
# 3. Multiplication, division, integer division and modulo
# 4. Addition and subtraction

conta_1 = 1 + 1 ** 5 + 5
print(conta_1)

conta_2 = (1 + 1) ** 5 + 5
print(conta_2)

conta_3 = (1 + int(0.5 + 0.5) ** 5) + 5
print(conta_3)

conta_4 = (1 + (0.5 + 0.5) ** 5) + 5
print(conta_4)

name = 'Pedro Henrique'
height = 1.90
weight = 100
imc = weight / height ** 2

print(name, 'has', height, 'meters of height')
print('His weight is', weight, 'kg')
print('His IMC is', imc)

print(f'{name} has {height:,.2f} meters of height')
print(f'His weight is {weight:,.1f} kg')
print(f'His IMC is {imc:,.2f}')
