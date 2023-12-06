""" 
@Program: 15_1
@Author: Donald Osgood
@Last Date: 2023-12-05 22:36:12
@Purpose: run multi processing
"""
import multiprocessing
import time
import random
import datetime


# process to run
def process_function():
    # random 0,1
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {current_time}")

def run_multiprocs():
    procs = []
    # process in parallel all 3
    for n in range(3):
        proc = multiprocessing.Process(target=process_function)
        procs.append(proc)
        proc.start()
    for p in procs:
        p.join()
        
if __name__ == "__main__":
    run_multiprocs()

