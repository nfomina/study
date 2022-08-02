from datetime import timedelta

hours, minutes, seconds = [int(i) for i in input().split(':')]
print(int(timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()))