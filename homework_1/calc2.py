def calculator(action):
    if action == '+' :
        return a+b
    if action == '-':
        return a-b
    if action == '/':
        return a/b
    if action == '*':
        return a*b
    return ('ERROR')
a=float(input('Введите первое число: '))
b=float(input('Введите второе число: '))
action=input('Введите символ (+-/*): ')
print(calculator(action))





