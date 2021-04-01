import datetime

birth = datetime.date(1988,12,1)
print("Birth: ", birth)

today = datetime.date.today()
print("Today: ", today)

# If a) current month is equal to my birthday, 
# b) AND day already passed., 
# c) OR if current momth is after my born date.
if ( today.month == birth.month and today.day >= birth.day or today.month > birth.month ):
    nextBirthYear = today.year + 1
else: 
    nextBirthYear = today.year

# 1) Get current date 
# 2) Get date of next birthday.
# Next Birthday date is at: 
# a) Same Born Month 
# b) Same born day 
# c) Calculated next birthday year
nextBirthday = datetime.date(nextBirthYear, birth.month, birth.day)
print ("Next Birthday: ", nextBirthday)

# 4) Date of next Birthday - current Date
diff = nextBirthday - today
print("Days left for net birthday:", diff.days)