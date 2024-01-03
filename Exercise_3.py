from datetime import datetime, timedelta

days = int(input())
work_days = int(input())
rest_days = int(input())
start_date = datetime.strptime(input(), '%d/%m/%Y')
days_of_work = []
i, wd = 0, 0

while i < days:
    wd += 1
    if wd <= work_days:
        days_of_work.append(start_date)
        start_date += timedelta(days=1)
        i += 1
    else:
        wd = 0
        start_date += timedelta(days=rest_days)
        i += rest_days
print(days_of_work)