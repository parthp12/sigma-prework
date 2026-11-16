from datetime import date as dt

# Fnd todays date and then split, day, month and year into seperate variables
today = dt.today()
current_year = today.year
current_month = today.month
current_day = today.day


def age_difference(previous_day, previous_month, previous_year):
    '''
    Calculates age between date and given date. Accounting for the day of the year
    INPUTS: Given date split into variables. Each variable given as a string 
    OUTPUTS: Age. Given as an integer
    '''
    age = current_year - int(previous_year)

    if int(previous_month) > current_month:
        age -= 1
    elif int(previous_month) == current_month:
        if int(previous_day) < current_day:
            age -= 1

    return age


def user_interface():
    '''
    Requests input from user. Only takes dd-mm-yyyy format
    Returns user output. 
    '''

    input_date = input("Please input the given date in the form dd-mm-yyyy")

    # Split given date into variables
    date_list = input_date.split('-')
    previous_day = date_list[0]
    previous_month = date_list[1]
    previous_year = date_list[2]

    # Call age calculation function
    age = age_difference(previous_day, previous_month, previous_year)

    return f"The age is {age} years"


print(user_interface())
