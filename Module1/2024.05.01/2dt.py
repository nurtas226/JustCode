from datetime import datetime, timezone, timedelta

currennt_utc_datetime = datetime.now(tz=timezone.utc)

str_datetime = datetime.strftime(currennt_utc_datetime, '%d-%m-%Y %H:%M:%S %z')

print(f"{str_datetime = }")

