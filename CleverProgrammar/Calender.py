import calendar

# headers of the week. mon, tue, wed... numbers show the number of characters
# 1 : M, 2 : Mo, 3 : Mon. Stops at 3
print(calendar.weekheader(3))
print()

# print the first month of the year 2020
print(calendar.month(2020, 1))


# print the entire given year
def year(i):
    month = 1
    while month < 13:
        print(calendar.month(i, month))
        month += 1


year(2020)


# print the entire year
def entireYear(i):
    print(calendar.calendar(i))


entireYear(2020)

# print the day of the week
print(calendar.weekday(2020,1,12))

print(calendar.isleap(2022))