status = "\nВведите новый статус заметки(цифру)"
status += "\n1.Выполнено.\n2.В процессе\n3.Отложено\n"
message = ""
message1 = "Ваш выбор1.\nСтатус заметки успешно обновлён на: выполнено"
message2 = "Ваш выбор2.\nСтатус заметки успешно обновлён на: в процессе"
message3 = "Ваш выбор3.\nСтатус заметки успешно обновлён на: отложено"
message = input(status)
if message == "1":
    print(message1)
elif message == "2":
    print(message2)
elif message == "3":
    print(message3)
else:
    print("Неверный символ")
