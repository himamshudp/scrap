from app2 import dmart
import schedule
import time
# Task scheduling After every 10mins geeks() is called.
print("calling dmart")
dmart()
print("calling scheduler")
schedule.every(5).minutes.do(dmart)
while True :
    # Checks whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)
