from functools import wraps
import timeit

DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


# def count_sundays(start_year, stop_year):
#     count = 1
#     sundays = 0
#     for year in range(start_year, stop_year + 1):
#         for month in range(12):
#             days = DAYS_IN_MONTH[month]
#             if month == 1 and is_leap(year):  # There are 29 days in February of each leap yar.
#                 days += 1
#             count += days
#             if count % 7 == 0:
#                 sundays += 1
#     return sundays


def is_leap(year):
    """Check if year is a leap year.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400:
                return True
            else:
                return False
        else:
            return True
    return False


def execution_time(f):
    """Decorator for measuring execution time of a function

    Examples:
        @timing
        def f(a):
            pass
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = f(*args, **kwargs)
        end = timeit.default_timer()
        print("'{}' execution time: {:.3f}s".format(f.__name__, end - start))
        return result

    return wrapper


if __name__ == "__main__":
    @execution_time
    def custom_sum(a, b):
        return a + b


    print(custom_sum(2, 3))
    print(custom_sum(3, 4))

    # print(count_sundays(2019, 2020))
