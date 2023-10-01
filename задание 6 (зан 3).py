per=int(input())
vtor=int(input())
tret=int(input())
chetv=int(input())
if ((per%2==0 and vtor%2==0) and (tret%2!=0 and chetv%2!=0))or((per%2!=0 and vtor%2!=0) and (tret%2==0 and chetv%2==0)):
    print('Да')
else:
    print('Нет')
