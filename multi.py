import threadA
import threadB
import threading

a = threading.Thread(target=threadA.process_TC)
b = threading.Thread(target=threadB.readLog)


a.start()
b.start()

a.join()
b.join()