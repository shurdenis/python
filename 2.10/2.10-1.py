#Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров, но только в том случае если они не равны None.

def function(x, y, z):
    dict = locals()
    print('Аргументы: ', *(f'{k} = {v}' for k, v in dict.items() if v))

function(1, None, 'sirius')