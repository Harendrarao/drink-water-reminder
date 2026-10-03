#💦 DRINK WATER REMINDER
import time
from win11toast import toast
import winsound
while True:
     winsound.Beep(800, 1500)
     toast(
        "Drink Water Reminder",
        "It's time to hydrate",
        duration="short"
     )
     time.sleep(2700)
  
