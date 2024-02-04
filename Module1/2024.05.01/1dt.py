from datetime import datetime, timezone, timedelta

currennt_datetime = datetime.now()
# currennt_utc_datetime = datetime.utcnow()
currennt_utc_datetime = datetime.now(tz=timezone.utc)


print(f"{currennt_datetime}")
print(f"{currennt_datetime.tzinfo}")
print(f"{currennt_utc_datetime}  ")
print(f"{currennt_utc_datetime.tzinfo}  ")

