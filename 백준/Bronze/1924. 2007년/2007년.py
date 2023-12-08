from datetime import datetime, date


def what_day_is_it(date):
    days = ['MON', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    day = date.weekday()
    print(days[day].upper())


x, y = map(int, input().split())

what_day_is_it(date(2007, x, y))
