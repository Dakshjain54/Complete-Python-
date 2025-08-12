import threading
import time
from concurrent.futures import ThreadPoolExecutor

def fun(sec):
    print(f"sleeping for {sec} sec")
    time.sleep(sec)

def main():
    time1 = time.perf_counter()
    # fun(4)    
    # fun(3)    
    # fun(2)    


    t1 = threading.Thread(target=fun, args=[4])
    t2 = threading.Thread(target=fun, args=[3])
    t3 = threading.Thread(target=fun, args=[2])
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    time2 = time.perf_counter()
    print(time2 - time1)

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(fun, 2)
        future2 = executor.submit(fun, 3)
        future3 = executor.submit(fun, 5)
        print(future1.result())
        print(future2.result())
        print(future3.result())

poolingDemo()        
    