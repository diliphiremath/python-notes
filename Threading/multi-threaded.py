from time import sleep, perf_counter
from threading import Thread

def task():
    print("Start execution")
    sleep(1)
    print("Execution complete")

start_time = perf_counter()

t1 = Thread(target=task)
t2 = Thread(target=task)

# start the threads
t1.start()
t2.start()

# wait for threads to complete
t1.join()
t2.join()

end_time = perf_counter()

print(f"It took {end_time - start_time: 0.2f} seconds to execute the program")