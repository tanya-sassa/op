print('Возраст')
age=int(input())
ostalos_let=16-age
if age >=16and age<75:
    print('Имя')
    name=input()
    if name==('Иван'):
        print('Ошибка')
    elif age>=16:
        print('Поздравляем  вы поступили в ВГУИТ')
else:
    print('Сначала нужно закончить школу!')
    print('Вам осталось учиться в школе',ostalos_let)
