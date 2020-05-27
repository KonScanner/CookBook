from multiprocessing import Process, Queue


def f(queue):
    return queue.put([None, '13/02/1915', 13])


if __name__ == "__main__":
    queue = Queue()  # create queue
    p = Process(target=f, args=(queue,))  # Process
    p.start()
    print(queue.get())  # Grab result off queue
    p.join()
