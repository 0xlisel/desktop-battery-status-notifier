# A Desktop Battery Notifier Program

from psutil import sensors_battery
from plyer import notification
import math

# print(math.floor(sensors_battery().percent))
# print(sensors_battery().power_plugged)

#title of notification
title = 'Battery Reminder'

# notification message
message = f'Battery remaining: {math.floor(sensors_battery().percent)}%' 

# timeout = 10 # duration to display the message, default = 10
notification.notify(title, message, 10)

# def notifier():
#     ... 

# if __name__ == '__main__':
#     notifier()


# if __name__ == "__main__":
#     if plugged:
#         percent = battery.percent
#         if percent <= 80:
#             notification.notify(
#                 #title of notification
#                 title="Plugged In",

#                 #message of notification
#                 message=" For better battery life, charge upto 80%",

#                 # displaying time
#                 timeout=2
#             )

#         elif percent == 100:
#             notification.notify(
#                 title="Plugged In",
#                 message=" Please plugged out the charger. Battery is charged",
#                 timeout=2
#             )

#         else:
#             notification.notify(
#                 title="Plugged In",
#                 message=" Remove the charger please. For better battery life charge up to 80%",
#                 timeout=2
#             )

#     else:
#         percent = battery.percent
#         if percent <= 20:
#             notification.notify(
#                 title="Battery Reminder",
#                 message="Your battery is running low. You might want to plug in your PC ",
#                 timeout=2
#             )

#         elif percent <= 50:
#             notification.notify(
#                 title="Battery Reminder",
#                 message=f" Battery is {percent}.",
#                 timeout=2
#             )

#         elif percent == 100:
#             notification.notify(
#                 title="Battery Reminder",
#                 message="Fully charged",
#                 timeout=2
#             )

#         else:
#             notification.notify(
#                 title="Battery Reminder",
#                 message=f"Battery is {percent}",
#                 timeout=2
#             )
