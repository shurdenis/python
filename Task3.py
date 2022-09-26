"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""
chart, author, name=input('Введите место в чарте, исполнителя и названия трека'), input(), input()
while chart != 'off':
    example_dict = {}
    example_dict['Место']=chart
    example_dict['Исполнитель']='author'
    example_dict['Название трека']='name'
    chart, author, name = input('Введите место в чарте, исполнителя и названия трека'), input(), input()
    example_dict[1] = chart
    example_dict[2] = author
    example_dict[3] = name
    if chart == 'off':
        print('(' + example_dict={} + ',' + example_dict={} + ')' + ': ' + example_dict{})
        break
else:print("Thank's!")
