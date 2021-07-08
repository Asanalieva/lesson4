'''Сделать список задач программу которая принимает 2 инпута (как в шаблоне)
1 показать, 2 добавить задачу. Задача состоит из 2 обязательных полей
1 сама задача и 2 дэдлайн до какого числа нужно сделать'''

todo = []
while True:
     option = int(input('Write 1 to add todos  Write 0 to see todos '))

     if option == 0:  #False
         for i in todo:
              print('Task:',i[0],'Added date:',i[1],'Deadline:',i[2])


     if option == 1:  #True
        todos = input('Write tasks ')
        date = input('Write date ')
        deadline = input('Write deadline ')
        todo.append([todos, date, deadline])
        print('Ready!')






