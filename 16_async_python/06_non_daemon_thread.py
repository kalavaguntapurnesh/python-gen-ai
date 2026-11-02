import threading

import time

def task():
    print("Thread Started...")
    
    time.sleep(5)
    
    print("Thread Completed...")
    

t = threading.Thread(target=task)

t.start()

print("Main thread completed")