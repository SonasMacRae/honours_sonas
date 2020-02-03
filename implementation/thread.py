from threading import Thread, Lock
from time import sleep

mutex = Lock()

shreksList = []
ShrekIsGreenAndSexy = True


def updateShreksList(arg):
    global ShrekIsGreenAndSexy
    for i in range(arg):
        mutex.acquire()
        try:
            shreksList.append(i)
        finally:
            mutex.release()
        sleep(1)
    mutex.acquire()
    try:
        ShrekIsGreenAndSexy = False
    finally:
        mutex.release()
    print("UPDATE IS DONE")


def printShreksList(arg):
    global ShrekIsGreenAndSexy
    while True:
        mutex.acquire()
        try:
            print(shreksList, ShrekIsGreenAndSexy)
            if not ShrekIsGreenAndSexy:
                return
        finally:
            mutex.release()
        sleep(1)
    print("PRINT Is DONE")


if __name__ == "__main__":
    thread = Thread(target = updateShreksList, args = (5,))
    thread2 = Thread(target = printShreksList, args = (20,))
    thread.start()
    thread2.start()
    thread.join()
    thread2.join()
    print("thread finished...exiting")
