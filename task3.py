from datetime import datetime, timedelta

def generate_schedule(days, work_days, rest_days, start_date):
    schedule = []
    current_date = start_date
    total_days = 0

    while total_days < days:
        for i in range(work_days):
            if total_days >= days:
                break
            schedule.append(current_date)
            current_date += timedelta(days=1)
            total_days += 1

        for n in range(rest_days):
            if total_days >= days:
                break
            current_date += timedelta(days=1)
            total_days += 1

    return schedule

print(generate_schedule(5, 2, 1, datetime(2020, 1, 30)))