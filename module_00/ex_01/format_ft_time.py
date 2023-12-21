import time as time
from datetime import datetime


def __fromat_math(n):
    return "{:.2e}".format(n)


try:
    # get current time in seconds
    current_time = time.time()

    # convert seconds to scientific notation
    time_scientific = __fromat_math(current_time)

    print(f"Seconds since January 1, 1970: {current_time} or \
          {time_scientific} in scientific notation")

    # get the current time
    current_datetime = datetime.now()

    # get the current month
    month_string = current_datetime.strftime("%b")

    # get time
    current_time_n = time.localtime()

    # get the current day
    current_day = current_time_n.tm_mday

    # get the current year
    current_year = current_time_n.tm_year

    print(f"{month_string} {current_day} {current_year}")

except Exception as e:
    print(f"Error: \n{e}")
