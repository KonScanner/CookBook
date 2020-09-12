import random
import time
import threading
from threading import Thread


def simpLeWorker():
    print('I am a SimpLeWorker', flush=True)
    time.sleep(random.random()*5)
    val = random.randint(0, 100)
    print(f'Hello, my favourite number is {val}', flush=True)


def example1():
    t = Thread(target=simpLeWorker)
    threads = [Thread(target=simpLeWorker) for _ in range(5)]

    [t.start() for t in threads]
    print(t.is_alive())
    print(t.start())
    print(t.is_alive())
    print(t.join())

# example1()


def example2():
    # Thread identity

    t = Thread(target=simpLeWorker)

    print(f"ident == {t.ident}, until t.start()")
    t.start()
    print(f"Thread name: {t.name}, Thread identifier: {t.ident}")


# example2()

# Custom name threads


def workerExample():
    self_name = threading.current_thread().name
    ident = threading.get_ident()
    sleep_time = random.randint(1, 4)
    print(
        f"Thread name {self_name}, Thread identifier: {ident}, sleeping for {sleep_time} s")
    time.sleep(sleep_time)
    print(f"Thread name {self_name} exiting...")


def example3():
    ts = [Thread(target=workerExample, name=name) for name in [
        'Rick James', 'Fyodor Dostoevsky', 'J Robert Oppenheimer']]

    for t in ts:
        t.start()
        print('Waiting...')


# example3()

def workerExample2(sleep_time):
    self_name = threading.current_thread().name
    ident = threading.get_ident()
    print(
        f"Thread name {self_name}, Thread identifier: {ident}, sleeping for {sleep_time} s")
    time.sleep(sleep_time)
    print(f"Thread name {self_name} exiting...")


def example4():
    ts = [Thread(target=workerExample2, name=name, args=(time,)) for name, time in zip([
        'Rick James', 'Fyodor Dostoevsky', 'J Robert Oppenheimer'], [1, 1.5, 2])]

    for t in ts:
        t.start()
        print('Waiting...')


# example4()

class MyThread(Thread):
    # Using a class that inherits from Thread
    def __init__(self, time_to_sleep, name=None):
        super().__init__(name=name)
        self.time_to_sleep = time_to_sleep

    def run(self):
        # self_name = threading.current_thread().name
        ident = threading.get_ident()
        print(
            f"Thread name {self.name}, Thread identifier: {ident}, sleeping for {self.time_to_sleep} s")
        time.sleep(self.time_to_sleep)
        print(f"Thread name {self.name} exiting...")


def example5():
    t = MyThread(2)
    t.start()


# example5()

TIME_TO_SLEEP = 1.5
EXIT_THREAD = False


def workerExample3():
    self_name = threading.current_thread().name
    ident = threading.get_ident()
    print(
        f"Thread name {self_name}, Thread identifier: {ident}, sleeping for {TIME_TO_SLEEP} s")
    time.sleep(TIME_TO_SLEEP)
    print(f"Thread name {self_name} exiting...")


def example6():
    """Global variable inheritance."""
    ts = [Thread(target=workerExample3, name=name) for name in [
        'Rick James', 'Fyodor Dostoevsky', 'J Robert Oppenheimer']]

    for t in ts:
        t.start()
        print('Waiting...')


example6()
