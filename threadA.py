
import csv
import enum
from msilib.schema import Condition
import time
import common
        
# Parse to define columns
def parse(row):
    tc_no = row[0]
    step_no = row[1]
    type_data = int(row[2])
    action_data = row[3]
    timeout_no = int(row[4])
    log_ok = int(row[5])
    log_err = int(row [6])
    return tc_no, step_no, type_data, action_data, timeout_no, log_ok, log_err

# Process test case
def process_TC():
    print("Hello")
    # Open() method is used to open file and return a file object
    file = open('speech.csv')
    # Use csv.reader object to read the CSV file
    csvreader = csv.reader(file)
    next(csvreader)
    for row in csvreader:
        common.c.acquire()
        if common.flag == 0:
            if (row[2] != 'type'):
                tc_no, step_no, type_data, action_data, timeout_no, common.log_ok, common.log_err = parse(row)
                if (step_no != '1'): 
                    if (common.check == 1):
                        print("Ok, next step")
                    else:
                        print("failed. The end")
                        break
                if(type_data == 2):
                    print("threadA: " +str(action_data))
                    time.sleep(timeout_no)
            common.flag = 1
            common.c.notify_all()
        else:
            common.c.wait()
        common.c.release()
    # Close the file
    file.close()