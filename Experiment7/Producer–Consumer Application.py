import threading
import multiprocessing
import time


def producer(q):
    for i in range(5):
        q.put(i)
        print("Produced:", i)
        time.sleep(0.2)


def consumer(q):
    for _ in range(5):
        item = q.get()
        print("Consumed:", item)
        q.task_done()


# Threading
print("Threading:")
q = __import__("queue").Queue()

t1 = threading.Thread(target=producer, args=(q,))
t2 = threading.Thread(target=consumer, args=(q,))

t1.start()
t2.start()
t1.join()
t2.join()


# Multiprocessing
print("\nMultiprocessing:")
q = multiprocessing.Queue()

p1 = multiprocessing.Process(target=producer, args=(q,))
p2 = multiprocessing.Process(target=consumer, args=(q,))

p1.start()
p2.start()
p1.join()
p2.join()
