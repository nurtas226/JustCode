from datetime import datetime, timezone, timedelta

str_datetime = '2024-01-01 01:25:45'

datetime_obj = datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')

print(f"Week day: {datetime_obj.weekday()}")