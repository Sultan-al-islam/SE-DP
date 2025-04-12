class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

s = Singleton()
s1 = Singleton()
print(s)
print(s1)


import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()  # Lock for thread safety
    def __new__(cls):
        with cls._lock:  # Ensures only one thread enters at a time
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance
# Testing
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True, same instance
