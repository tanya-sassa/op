a=int(input())
if a%4==0 and a%100!=0 and a%400==0:
    print('Да')
else:
    print('Нет')
