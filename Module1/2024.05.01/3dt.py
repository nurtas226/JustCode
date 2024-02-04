from datetime import datetime, timezone, timedelta

str_datetime = '2023-10-01 01:22:45'

datetime_obj = datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')

print(f"{datetime_obj = }")

print(f"{timedelta(weeks=5, hours=3) = }")

