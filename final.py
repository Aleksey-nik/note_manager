listing=[input("Введите имя пользователя"),
         input("Введите описание заметки"),
         input("Введите статус заметки"),
         input("Введите дату создания,дд.мм.гг"),
         input("Введите дату истечения,дд.мм.гг"),
         [
          input("Введите заголовок заметки1"),
          input("Введите заголовок заметки2"),
          input("Введите заголовок заметки3")
         ]
]
print("Имя пользователя:", listing[0])
print("Заголовок заметки 1:", listing[5] [0])
print("Заголовок заметки 2:", listing[5] [1])
print("Заголовок заметки 3:", listing[5] [2])
print("Описание заметки:", listing[1])
print("Статус заметки:", listing[2])
print("Дата создания заметки:", listing[3])
print("Дата истечения заметки:", listing[4])
