#!/usr/bin/python3
# encoding: utf-8

import time
#import threading
from queue import Queue
from threading import Thread

# A thread that produces data
def producer(out_q):
    i = 0
    while True:
        # Produce some data
        i = i + 1
        data = i
        print("Create data: " + str(data) + ", sending it...")
        out_q.put(data)
        print("Data sent!")
        time.sleep(2)

# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data
        print("Data received: " + str(data))

def start_thread():
    # Create the shared queue and launch both threads
    q = Queue()
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()

def main():
    start_thread();
    # 调用 join 等待线程结束
    #one_thr.join()
    #two_thr.join()
    #three_thr.join()

if __name__ == '__main__':
    main()
