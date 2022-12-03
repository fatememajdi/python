time = str(input('time : '))
seconds = 0
seconds += int(time[0:2]) * 3600
seconds += int(time[3:5]) * 60
seconds += int(time[6:])

print(seconds)
