from time import sleep, perf_counter

def task():
    print("Task execution starts..")
    sleep(1)
    print("Task execuation completed.")

start_time = perf_counter()

task()
task()

end_time = perf_counter()

print(f"it took {end_time - start_time:0.2f} seconds to execute a program")
