"""Birthday Paradox Simulation, by Al Sweigart al@investwithpython.com"""

import datetime, random


def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation as long as all birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more that once in the birthday list"""
    if len(birthdays) == len(set(birthdays)):
        return None  # all birthdays are unique so return none

    # Compare each birthday ti ever other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA


# Display the intro:
print('''Birthday Paradox, by Al Sweigart 

The Birthday Paradox shows us that in a group of N people, the odds that
2 of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (i.e., repeated random simulations)
to explore this concept.

(It's not actually a paradox, its just a surprising result.)
''')

# Set up a tuple of month names in order:

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: # Keep asking untel the user enters a valid amount.
    print("How many birthdays shall I generate?(Max = 100)")
    response = input(">> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # User has entered a valid amount.