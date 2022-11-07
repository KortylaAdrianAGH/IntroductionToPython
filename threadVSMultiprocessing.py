from threading import Thread
import time
import multiprocessing


def ComparisionPrint(threadResult, multiprocessingResult):
    print("Task takes threads: {}".format(threadResult))
    print("Task takes Multiprocess.Process: {}".format(multiprocessingResult))

def CountToMilion():
    for i in range(10000):
        for i in range(50000):
            i*i



if __name__ == '__main__':
    threads = []
    processes = []
    startTimeThread = time.perf_counter()
    threads.append(Thread(target=CountToMilion()))
    threads.append(Thread(target=CountToMilion()))
    threads.append(Thread(target=CountToMilion()))
    durationTimeThreads = time.perf_counter() - startTimeThread

    startTimeProcess = time.perf_counter()
    processes.append(multiprocessing.Process(target=CountToMilion))
    processes.append(multiprocessing.Process(target=CountToMilion))
    processes.append(multiprocessing.Process(target=CountToMilion))
    for i in processes:
        i.start()

    for process in processes:
        process.join()

    durationTimeProcess = time.perf_counter() - startTimeProcess

    ComparisionPrint(durationTimeThreads, durationTimeProcess)