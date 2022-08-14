import threading
global check, log_ok, log_error, flag
c = threading.Condition()
flag = 0
log_error  =0 
log_ok = 0
check = 0