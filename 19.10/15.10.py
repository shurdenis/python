"""
Напишите программу создающую .txt файл и записывающую туда строку "Я гений и стараюсь учить питон".
Выведите первые 7 символов файла на экран.
"""
with open('sirius.txt', 'w') as f:
    writers1 = f.write("Я гений и стараюсь учить питон")

with open('sirius.txt', 'r') as f:
    reader = f.read(7)
    print(reader)