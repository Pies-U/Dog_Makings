from threading import Thread
import time

#Uwaga nie jest to synchonizowane ale pokazuje roznice miedzy watkami

time_limited = True

try:
    threads = int(input("How many threads? > "))
    if threads > 16:
        print("Chcesz komputer zabić?")
    else:
        run_limit = int(input("Time Limit? (sec) > "))
        if run_limit == "":
            time_limited = False
        if run_limit > 1000:
            print("Debilu to za długo")
        else:
            pass
except TypeError:
    print("")
    print("Podaj NUMERKI debilu")


run = True
x = 0 

def task():
    global x
    while run:
        x += 1
        print(x) 


for i in range(1, threads + 1):
    Thread(target=task).start()

#Test part
if time_limited:
    time.sleep(run_limit)
    run = False
    print("")
    print(f"In {run_limit} sec printed {x} numbers using {threads} threads")