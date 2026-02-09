import threading
from pyreadonce import pyreadonce

def set_worker(r:pyreadonce):
    import time
    while True:
        r.set(time.time())
        time.sleep(1)

def get_worker(r:pyreadonce):
    import time
    while True:
        print(r.get())
        time.sleep(0.1)

if __name__== "__main__":
    r = pyreadonce()
    t1 = threading.Thread(target=set_worker, args=(r,))
    t2 = threading.Thread(target=get_worker, args=(r,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()