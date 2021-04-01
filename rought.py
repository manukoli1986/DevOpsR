# # from datetime import datetime


# # def get_user_birthday():
# #     year = int(input('When is your birthday? [YY] '))
# #     month = int(input('When is your birthday? [MM] '))
# #     day = int(input('When is your birthday? [DD] '))

# #     birthday = datetime(year,month,day)
# #     return birthday


# # def calculate_dates(birthyday):
# #     now = datetime.now()
# #     birthday = datetime(now.year, birthday.month, birthday.day)
# #     return (birthday - now.today()).days + 1


# # bd = get_user_birthday()
# # c = calculate_dates(bd)
# # print(c)

# # from datetime import date as dt
# # f_date = dt(2014, 5, 11)
# # l_date = dt(2014, 7, 11)
# # delta = l_date - f_date
# # print(delta.days)


# # from datetime import date
# import datetime
# myDate = "2020-02-20"
# # def convert(dt):
# #     newDate = datetime.datetime.strptime(dt, '%Y-%m-%d')
# #     print(newDate.date())


# def convert(dt):
#     newDate = datetime.datetime.strptime(dt, '%Y-%m-%d')
#     print(newDate.date())

# convert(myDate)


# newDate = "2020-02-20"
# dob = datetime.datetime.strptime(newDate, '%Y-%m-%d')
# nowDate = datetime.datetime.now().date()
# print(dob.date())
# print(nowDate)




# import datetime

# date_time_str = '2018-06-29 08:15:27.243860'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

# print('Date:', date_time_obj.date())
# print('Time:', date_time_obj.time())
# print('Date-time:', date_time_obj)


# import requests 
