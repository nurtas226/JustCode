from datetime import datetime, timedelta

def find_next_day_of_week(target_day):
    week_days = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6,
    }

    today = datetime.today()
    target_day_value = week_days.get(target_day)

    if target_day_value is not None:
        if target_day_value < 6:
            days_until_target = (target_day_value - today.weekday() + 7) % 7
            next_day = today + timedelta(days=days_until_target)
            print(f"Today is {today.strftime('%Y-%m-%d')}. Days left until next {target_day}: {days_until_target} days.")
            print(f"Next {target_day} will be on {next_day.strftime('%Y-%m-%d')}.")
        elif target_day_value == 6:
            next_day = today + timedelta(days=7)
            print("Days left until next Sunday: 7 days.")
            print(f"Next {target_day} will be on {next_day.strftime('%Y-%m-%d')}.")
    else:
        print("Invalid day of the week provided.")

target_day = input("Enter weekday that you want to check: ")

find_next_day_of_week(target_day)

