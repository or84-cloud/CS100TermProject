from datetime import datetime, timedelta

def study_time_distribute(tota_minutes, due_date, study_days_per_week=5):
    """Distributing total study time across all available days before deadline"""
    today = datetime.today().date()
    days_left = (due_date - today).days

    if days_left <= 0:
        return {"error": "Deadline has passed, or it is today."}

    #Counting days the user is actually studying
    available_days = 0
    for i in range(days_left):
        if (today + timedelta(days=i)).weekday() < study_days_per_week:
            available_days += 1

    if available_days == 0:
        return {"error": "No study days before deadline!"}

    per_day = round(total_minutes / available_days, 1)

    #Building a schedule:
    schedule = {}
    for i in range(days_left):
        day =  today + timedelta(days=i)
        if day.weekday() < study_days_per_week:
            schedule[day.strftime("%a %m %m")] = per_day
    return schedule


#Existing calculation
total_minutes = calculate_total_time(assignments, exams, difficulty)

#Function call(s)
schedule = study_time_distribute(total_minutes, due_date)

#Returning results
for day, minutes, in schedule.items():
    print(f"{day}: {minutes} minutes")