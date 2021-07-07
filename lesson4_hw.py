'''Сделать список задач программу которая принимает 2 инпута (как в шаблоне)
1 показать, 2 добавить задачу. Задача состоит из 2 обязательных полей
1 сама задача и 2 дэдлайн до какого числа нужно сделать'''
todo = []
for i in range(100):
    option = input('Write task and deadline ')
    todo.append(option)
    if option == 'end': #to see your todos write 'end'
        for i in todo:
            print(i)


