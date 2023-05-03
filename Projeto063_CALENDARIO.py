# crie um projeto que mo

import calendar

print(calendar.calendar(2023))
print(calendar.month(2023, 12))

print(calendar.monthrange(2022, 12))
print(list(enumerate(calendar.day_name)))

for week in calendar.monthcalendar(2023, 12):
    for day in week:
        if day == 0:  # os dias q n sao do mes q qremos ficam '0', ate começar
            # o mes desejado
            continue
        print(day)
