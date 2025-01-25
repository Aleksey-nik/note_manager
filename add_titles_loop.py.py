#username="Алексей"
#title="Программа 1"
#content="Вычисление"
#status="Начало"
#created_date_day="день"
#created_date_month="- месяц"
#created_date_year="- год"
#issue_date_day="день"
#issue_date_month="- месяц"
#issue_date_year="- год"


title = "\nВведите заголовок"
title += "\nОстанов по стоп.\n"
message = ""
while message != "стоп":
    message = input(title)
    if message != "стоп":
        print(message)
    else:
        print("Останов программы")
