from datetime import datetime, timedelta

start_time = datetime.strptime(input(), '%H:%M')
end_time = datetime.strptime(input(), '%H:%M')

while start_time <= end_time:
    lesson_start = start_time
    lesson_end = lesson_start + timedelta(minutes=45)
    if lesson_end <= end_time:
        print(f"{lesson_start.strftime('%H:%M')} - {lesson_end.strftime('%H:%M')}")
    start_time = lesson_end + timedelta(minutes=10)