import threading
import time
import logging

logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
        )

def worker():
       print threading.currentThread().getName(), 'Starting'
       time.sleep(2)
       print threading.currentThread().getName(), 'Exiting'

def my_service():
       print threading.currentThread().getName(), 'Starting'
       time.sleep(3)
       print threading.currentThread().getName(), 'Exiting'

t = threading.Thread(name='my_service', target=my_service)
t.setDaemon(True)

w = threading.Thread(name='worker', target=worker)
# w2 = threading.Thread(target=worker) # will use a default name

w.start()
