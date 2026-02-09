import threading

class pyreadonce:
    def __init__(self, is_atomic=True, is_readonce=True, default_value=None, strict=False):
        self._lock = threading.Lock() if is_atomic else None
        self._upd = threading.Event() if is_readonce else None
        self._value = default_value
        self._upd.set()
        self._strict = strict

    def set(self, value):
        if self._lock is not None:
            with self._lock:
                self._value = value
        else:
            self._value = value
        if self._upd is not None:
            self._upd.set()

    def get(self, timeout=10.0):
        if self._upd is not None:
            if not self._upd.wait(timeout):
                if self._strict:
                    raise Exception("Timeout waiting for update")
                else:
                    return None
            self._upd.clear()
        if self._lock is not None:
            with self._lock:
                return self._value
        else:
            return self._value

