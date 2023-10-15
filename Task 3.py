names = ['Александр', 'Максим', 'Яна']
print(F"Текущий список имён {names}")


def add(names1):
    x = input('Введите новое имя: ')
    names1 += [x]
    print(names1)


add(names)
add(names)
