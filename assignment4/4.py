seconds = int(input('Seconds :'))

seconds = seconds % (24 * 3600)
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print("%02d:%02d:%02d" % (hours, minutes, seconds))
