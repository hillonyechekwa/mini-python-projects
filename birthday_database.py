from datetime import datetime


# birthdays database
birthdays = {
    'Kiki': 'Jan 1',
    'Sarah': 'Sep 29',
    'Deedee': 'Aug 15',
    'AJ': 'Jan 27'
}

# ltuple of acceptable month names
mnths = (
    'Jan', 'Feb', 'Mar', 'Apr',
    'May', 'Jun', 'Jul', 'Aug',
    'Sep', 'Oct', 'Nov', 'Dec',
)

# tuple of months with 30 days
mnths30 = ('Apr', 'Jun', 'Sep', 'Nov')
# tuple of months with 31 days
mnths31 = ('Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec',)

# check if year is leap year
def isleap():
    current_year = datetime.today().year
    
    if current_year % 4 == 0:
        if current_year % 100 == 0:
            if current_year % 400 == 0:
                return  "it's a leap year"
            else:
                return "it's not a leap year"
        else:
            return "it's a leap year"
    else:
        return "it's not a leap year"
                
                
def is_in_months() -> str:
    month = input_month()
    
    if month not in mnths:
        print("You entered the month wrong")
        print("type the first three letters of the month in title case i.e 'Jan'")
        input_month()
    else:
        return month


def input_month() -> str:
    birth_month = input('Add the person\'s birthday month')
    return birth_month.capitalize()

# check if date entered is in line with the months dates
def is_in_dts(name):
    mnt = is_in_months()
    dte = input_date()
    yr = isleap()
    
    if dte in range(1, 31) and mnt in mnths30:
        assign_to_database(dte, mnt, name)
    elif dte in range (1, 32) and mnt in mnths31:
        assign_to_database(dte, mnt, name)
    elif mnt == 'Feb' and yr == "it's a leap year" and dte in range(1, 30):
        assign_to_database(dte, mnt, name)
    elif mnt == 'Feb' and yr == "it's not a leap year" and dte in range(1, 29):
        assign_to_database(dte, mnt, name)
    else:
        print("your date and month doesn't correlate")
        return is_in_months
        return input_date
    

def input_date():
    birth_date = input('Add the date')
    return int(birth_date)


def assign_to_database(date: int, month: str, name: str):
    birthdays[name] == month + ' ' + str(date)
    print(f"{name}'s birthday is on {birthdays[name]}")
    


# tuple of acceptable month dates
# dates = (
#     '1', '2', '3', '4', '5',
#     '6', '7', '8', '9', '10',
#     '11', '12', '13', '14',
#     '15', '16', '17', '18', 
#     ''
# )


#TODO: write a function to check if month is a 30 day month or a 31 day month
#TODO: write function if year is a leap year



name = input(' (enter blank(press enter) to quit) ').capitalize()

while True:
    if name == '' or name == ' ':
        break
       
    if name in birthdays:
        bday = birthdays.get(name, 0)
        print(f"{name}'s birthday is on {bday}'")
    else:
        print("we don't have that name in the database, why don't we change that")
        is_in_dts()



