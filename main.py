
def menu():
    print('Доступные команды:'
    '\n1. Добавить задачу.'
    '\n2. Показать задачу.'
    '\n3. Удалить задачу.'
    '\n4. Пометить задачу как выполненную.'
    '\n5. Выйти.')


def index(save):
   a = input('Введите задачу:')
   b = input('Выбери метку для задачи(красный, желтый, зеленый): ')
   save.append({'a': a, 'b': b, 'done': False})
   print('Задача добавлена.')


def show(save):
    if not save:
        print('У вас нет активных задач')
        return
    for i, save in enumerate(save, start = 1):
        status = '(Выполненa)' if save['done'] else ''
        print(f'{i}. {save["a"]} (Метка: {save["b"]}) {status}')


def delete(save):
    show(save)
    try:
        index = int(input('Введите номер задачи которую хотите удалить:'))-1
        if 0 <= index < len(save):
            save.pop(index)
            print('Задача была успешно удалена')
        else:
            print('Такой задачи нет')
    except ValueError:
        print('Напишите пожалуйста номер задачи')


def completed(save):
    show(save)
    try:
        f = int(input('Введите номер задачи которую хотите пометить выполненной:'))-1
        if 0 <= f < len(save):
            save[f]['done'] = True
            print('Задача помечена как выполненная')
        else:
            print('Такого номера нет.')
    except ValueError:
        print('Напишите пожалуйста номер задачи')



def main():
    save = []
    while True:
        menu()
        d = input('Выберите команду(1-5):')
        if d == '1':
            index(save)
        elif d == '2':
            show(save)
        elif d == '3':
            delete(save)
        elif d == '4':
            completed(save)
        elif d == '5':
            print('Выход из программы.')
            break
        else:
            print('Такой команды нет.')
if __name__ == '__main__':
    main()


