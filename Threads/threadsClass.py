import concurrent.futures
import os
import time
import threading

def helloWorld(t):
    time.sleep(t)
    print(f"Hello World from {threading.current_thread().name}")
    return t

if __name__ == '__main__':
    time1 = time.perf_counter()

    t1 = threading.Thread(target=helloWorld, args=[4], name='t1')
    t2 = threading.Thread(target=helloWorld, args=[3], name='t2')
    t3 = threading.Thread(target=helloWorld, args=[2], name='t3')

    for i in range(10):
        t = threading.Thread(target=helloWorld, args=[4], name='t1')
        t.start()

    t1.start()
    t2.start()
    t3.start()

    t1.join()  # JOIN: wait for execution
    t2.join()
    t3.join()

    time2 = time.perf_counter()

    print(time2 - time1)

    time1 = time.perf_counter()

    print("cpu"+str(os.cpu_count()))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        f1 = executor.submit(helloWorld, 4) #T1 - 1 2 3 4
        f2 = executor.submit(helloWorld, 3) #T2 - 1 2 3
        f3 = executor.submit(helloWorld, 2) #T2 - W W W 4 5
        result1 = f1.result()
        print(result1)
        result2 = f2.result()
        print(result2)
        result3 = f3.result()
        print(result3)
    
    # IMPLICIT JOIN OUTSIDE BLOCK...
    time2 = time.perf_counter()
    print(time2 - time1)