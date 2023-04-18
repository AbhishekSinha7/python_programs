import calendar
year = 2021
month=abs(int(input("enter the month:")))
if month<=12:
    print(calendar.month(year, month))
else:
    print("invalid month!")
