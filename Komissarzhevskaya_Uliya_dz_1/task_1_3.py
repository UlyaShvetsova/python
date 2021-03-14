user_numb = int(input('Please, enter the number from 0 to 20: '))  # Склонение числа процентов пользователя
if 5 <= user_numb <= 20 or user_numb == 0:
    print(f'({user_numb} процентов)')
elif user_numb == 1:
    print(f'({user_numb} процент)')
elif 1 < user_numb < 5:
    print(f'({user_numb} процента)')
else:
    print(f'Noooooo! From 0 to 20!')

for numb in range(0, 21):  # Вывод всех склонений
    if numb >= 5 or numb == 0:
        print(f'{numb} процентов')
    elif numb == 1:
        print(f'{numb} процент')
    elif 1 < numb < 5:
        print(f'{numb} процента')
