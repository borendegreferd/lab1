'''
Дано четырехзначное число. Найти сумму его цифр.
'''

number = int(input())
print('{0}'.format(number%10+(number//100)%10+(number//10)%10+number//1000))