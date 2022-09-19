print('Добро пожаловать в магазин Долголетие!')
sum1=int(input('Введите сумму к оплате: '))
hours1=int(input('Введите текущий час оплаты: '))
if hours1>=10 and hours1<=12:
    print(sum1/2)
elif hours1>=20 and hours1<=22:
    print(sum1/4)
else:
    print(sum1)

