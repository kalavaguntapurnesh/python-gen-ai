import threading
import time

def task():
     print("Child Thread Started")
     time.sleep(5)
     print("Child Thread Completed")

t = threading.Thread(target=task)
t.daemon = True
t.start()
print("Main Thread Completed")