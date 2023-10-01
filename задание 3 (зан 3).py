n=int(input())
chas=n//60
minut=n-(chas*60)
if n>1440:
    print('Ошибка')
else:
    print(chas,minut)
