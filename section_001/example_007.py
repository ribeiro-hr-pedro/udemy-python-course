# Student: Pedro Henrique Resende Ribeiro
# Description: f-string anf format method
# Date: 2024-01-10 - Time: 07:30

a = 'A'
b = 'B'
c = 1.1
d = True

test_1 = 'a = {}, b = {}, c = {:,.2f} and d = {}'.format(a, b, c, d)
print(test_1)

string = 'a = {}, b = {}, c = {:,.2f} and d = {}'
test_2 = string.format(a, b, c, d)
print(test_2)

test_3 = 'a = {0}, b = {1}, c = {2:,.2f} and d = {3}'.format(a, b, c, d)
print(test_3)

test_4 = 'a = {param_1}, b = {param_2}, c = {param_3:,.2f} and d = {param_4}'.format(
    param_1=a, param_2=b, param_3=c, param_4=d)
print(test_4)

print(f'a = {a}, b = {b}, c = {c:,.2f} and d = {d}')
