from pynotifier import Notification
import psutil

battery = psutil.sensors_battery()
percent = battery.percent

Notification("Battery Percentage" , str(percent) + "% percentage remaining" , duration=10).send()