import multiprocessing


def worker_function(lock, shared_value):
    with lock:
        print(f"Process {multiprocessing.current_process().name} is updating shared value")
        shared_value.value += 1


if __name__ == "__main__":
    shared_value = multiprocessing.Value('i', 0)  # Shared integer value
    lock = multiprocessing.Lock()  # Lock for synchronization

    processes = []
    for _ in range(5):
        process = multiprocessing.Process(target=worker_function, args=(lock, shared_value))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Final shared value: {shared_value.value}")
