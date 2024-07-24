from win10toast import ToastNotifier
import time 

toaster = ToastNotifier()

title = input("Title of the Reminder:  ")
message = input("Message: ")
minutes = float(input("How many minutes: "))


totalTime = minutes * 60 

print("Reminder set Successfully")
time.sleep(totalTime)
toaster.show_toast(title, message, duration=10, threaded=True)

while toaster.notification_active:
    time.sleep(0.1)
    