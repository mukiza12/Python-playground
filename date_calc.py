from datetime import datetime, timedelta

start_date = datetime(2026, 2, 16)
duration_weeks = 9

end_date = start_date + timedelta(weeks = duration_weeks)

print(f"{start_date = }")
print(f"{end_date}")

