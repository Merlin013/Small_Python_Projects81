"""Calendar Maker, by Al Sweigart al@inventwithpython.com
Create monthly calendars, saved to a text file and fit for printing."""

import datetime

# Set up the constants:

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print("Calendar Maker, by Al Sweigart al@inventwithpython.com")

while True: # Loop to get a year from the user.
    print("Enter the year for the calendar.")
    response = input(">> ")

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print("Please enter a numeric year, like 2021.")
    continue

while True: # Loop to get a month from the user.
    print("Enter the month for the calendar, 1 - 12:")
    response = input(">> ")

    if not response.isdecimal():
        print("Please enter a numeric month, like 10 for October.")
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print("Please enter a number from 1 to 12.")

def getCalendarFor(year, month):
    calText = '' # caltext will contain the string of our calendar

    # Put the month and year at the top of the calendar:
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # Add the days of the week labels to the calendar:

    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # The horizontal line string that separate weeks:
    weekSeparator = ('+----------'*7) + '+\n'

    # The blank rows have 10 spaces in between