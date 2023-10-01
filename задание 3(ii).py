print('Возраст')
age=int(input())
if age >0 and age<75:
    print('Имя')
    name=input()
    if name==('Иван'):
        print('Ошибка')
    elif age>=16:
        print('Поздравляем  вы поступили в ВГУИТ')
else:
    print('Сначала нужно закончить школу!')
    
