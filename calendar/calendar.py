months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def count_sundays(start_year, stop_year):
    count = 1
    sundays = 0
    for year in range(start_year, stop_year + 1):
        for month in  range(12):
            days = months[month]
            if month == 1 and is_leap(year):
                days += 1
            count += days
            if count % 7 == 0:
                sundays +=1
    return sundays



def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400:
                return True
            else:
                return False
        else:
            return True
    return False