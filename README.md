# pyreadonce
A utility class when you only want a variable to be read once before next update, useful for multithreading.

## Example
```python
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
```
You will get output like following:
```text
1770660107.9304247
1770660108.9397464
1770660109.9539416
1770660110.9688287
1770660111.9839122
1770660112.9992635
1770660113.9994962
1770660115.0038087
1770660116.0087395
1770660117.0234022
```