import datetime
while True:
     issue_date = input("Введите дату в формате дд/мм/гггг ")
     try:
         d = datetime.datetime.strptime(issue_date, '%d/%m/%Y')
         break
     except:
         print ("Формат не верный")
difference = d.date() - datetime.date.today()
if d.date() <= datetime.date.today():
    print("Дедлайн истёк ", difference)
else:
    print("До дедлайна осталось ", difference)

