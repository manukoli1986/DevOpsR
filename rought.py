from datetime import datetime


def get_user_birthday():
    year = int(input('When is your birthday? [YY] '))
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))

    birthday = datetime(year,month,day)
    return birthday


def calculate_dates(birthyday):
    now = datetime.now()
    birthday = datetime(now.year, birthday.month, birthday.day)
    return (birthday - now.today()).days + 1


bd = get_user_birthday()
c = calculate_dates(bd)
print(c)