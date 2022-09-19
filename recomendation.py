category1=input('Введите категорию товара: ')
if category1 == 'продукты':
    price1=int(input('Введите цену товара:'))
    if price1<100:
        print('Попробуйте нашу выпечку!')
    elif price1>=100 and price1 < 500:
        print('Как насчет орехов в шоколаде?')
    elif price1>=500:
        print('Попробуйте экзотические фрукты!')
else: print('Загляните в товары для дома!')