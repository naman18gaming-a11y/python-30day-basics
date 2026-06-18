import time
alarm_time = input("Enter alarm time (HH:MM): ")
while True:
    current_time = time.strftime("%H:%M")
    if current_time == alarm_time:
        print(" Alarm! Wake up!")
        break
    time.sleep(30)
