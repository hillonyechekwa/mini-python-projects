from datetime import datetime


birthdays = {
    'Kiki': 'Jan 1',
    'Sarah': 'Sep 29',
    'Deedee': 'Aug 15',
    'AJ': 'Jan 27'
}

mnths = (
    'Jan', 'Feb', 'Mar', 'Apr',
    'May', 'Jun', 'Jul', 'Aug',
    'Sep', 'Oct', 'Nov', 'Dec',
)

mnths30 = ('Apr', 'Jun', 'Sep', 'Nov')
# tuple of months with 31 days
mnths31 = ('Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec',)


def get_birthday(person):
    m = input_month()
    chk_mnt = is_in_months(m)
    d = input_date()
    leap = isleap()
    return compare_month_and_date(chk_mnt, d, leap, person)


def compare_month_and_date(mnt: str, dte: int, yr: str, nm: str) -> int:

    if dte in range(1, 31) and mnt in mnths30:
        assign_to_database(dte, mnt, nm)
    elif dte in range(1, 32) and mnt in mnths31:
        assign_to_database(dte, mnt, nm)
    elif mnt == 'Feb' and yr == "it's a leap year" and dte in range(1, 30):
        assign_to_database(dte, mnt, nm)
    elif mnt == 'Feb' and yr == "it's not a leap year" and dte in range(1, 29):
        assign_to_database(dte, mnt, nm)
    else:
        print("your date and month doesn't correlate")
        return dte


def isleap():
    current_year = datetime.today().year

    if current_year % 4 == 0:
        if current_year % 100 == 0:
            if current_year % 400 == 0:
                return "it's a leap year"
            else:
                return "it's not a leap year"
        else:
            return "it's a leap year"
    else:
        return "it's not a leap year"


def is_in_months(month: str) -> str:

    if month not in mnths:
        print("You entered the month wrong")
        print("type the first three letters of the month in title case i.e 'Jan'")
        input_month()
    else:
        return month


def input_month() -> str:
    birth_month = input('Add the person\'s birthday month')
    return birth_month.capitalize()


def input_date() -> int:
    birth_date = input('Add the date')
    return int(birth_date)


def assign_to_database(date: int, month: str, name: str):
    birthdays[name] = month + ' ' + str(date)
    print(f"{name}'s birthday is on {birthdays[name]}")
    print("database has been updated!")
    

name = input(' (enter blank(press enter) to quit) ').capitalize()


while True:
    if name == '' or name == ' ':
        break

    if name in birthdays:
        bday = birthdays.get(name, 0)
        print(f"{name}'s birthday is on {bday}'")
        break
    else:
        print("we don't have that name in the database, why don't we change that")
        data = get_birthday(name)
        if isinstance(data, int):
            rerun_data = get_birthday(name)
        else:
            break
