import threading

shared_variable = 0
lock = threading.Lock()

def adder():
    global shared_variable
    for i in range(1000000):
        lock.acquire()
        shared_variable += 1
        lock.release()

def subtractor():
    global shared_variable
    for i in range(1000000):
        lock.acquire()
        shared_variable -= 1
        lock.release()


thread1 = threading.Thread(target=adder)
thread2 = threading.Thread(target=subtractor)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(shared_variable)