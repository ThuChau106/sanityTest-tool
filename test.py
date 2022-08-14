import time
import random
import threading

# Read dlt log from RIG
def readLog():
    while True:
        time
        a = random.randint(0, 2)
        print("Random value: " + str(a))
        
        
a = threading.Thread(target=readLog)
a.start()
a.join()