import time
import random
import common

# Read dlt log from RIG
def readLog():
    while True:
        common.c.acquire()
        if common.flag == 1:
            a = random.randint(0, 1)
            print("Random value: " + str(a))
            if (common.log_ok == a):
                print("That is oke\n")
                common.check = a
            else:
                if (common.log_error == a): 
                    print("That is not oke\n")
                    common.check = a 
            common.flag = 0
            common.c.notify_all()
        else:
            common.c.wait()
            common.c.release()
