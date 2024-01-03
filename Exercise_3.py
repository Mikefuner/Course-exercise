from datetime import datetime, timedelta

def working_days():
    days = int(input('Insert the number of all days --> '))
    work_days = int(input('Insert the number of the working days --> '))
    rest_days = int(input('Insert the number of the rest days --> '))
    start_date = datetime.strptime(input('Insert the date of the start --> '), '%d/%m/%Y')
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

    if input('Do you want to insert other data? --> ').lower() == 'yes':
        working_days()

working_days()