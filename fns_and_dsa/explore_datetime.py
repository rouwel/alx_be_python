import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)

def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.date.today() + datetime.timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer.")
calculate_future_date()