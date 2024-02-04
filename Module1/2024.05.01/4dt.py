from datetime import datetime, timezone, timedelta

str_datetime = '2023-10-01 01:25:45'

datetime_obj = datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')

result = datetime_obj + timedelta(minutes=20)

print(f"datetime_obj: {datetime.strftime(datetime_obj, '%Y-%m-%d %H:%M:%S') }")
print(f"result: {datetime.strftime(result, '%Y-%m-%d %H:%M:%S') }")
