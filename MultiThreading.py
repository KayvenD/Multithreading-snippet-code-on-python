import threading

import time

start = time.time()

def thread_1():
    for i in range(4):
        time.sleep(10)
        print("Hello")


def thread_2():
    for i in range(4):
        ##time.sleep(0.7)
        print("Hi")

##create the list of thread:
t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

## start the threads:
t1.start()
t2.start()

##If you want waiting until a thread stops its task, just write this :
t1.join()
t2.join()

##The below code will execute until all thread is done.
end = time.time()
print("Time taken in seconds : ", (end-start))