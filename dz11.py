import mmap
import multiprocessing
import time
import os

# Размер буфера для общей памяти
BUFFER_SIZE = 1024


def producer(shared_file_name):
    with open(shared_file_name, "r+b") as f:
        # Создаем отображение памяти
        shm = mmap.mmap(f.fileno(), BUFFER_SIZE, access=mmap.ACCESS_WRITE)
        message = "Привет от производителя!".encode('utf-8')
        shm.seek(0)
        shm.write(message)
        print("[ПРОИЗВОДИТЕЛЬ] Сообщение отправлено.")
        shm.close()


def consumer(shared_file_name):
    # Ждем немного, чтобы производитель успел записать
    time.sleep(1)
    with open(shared_file_name, "r+b") as f:
        shm = mmap.mmap(f.fileno(), BUFFER_SIZE, access=mmap.ACCESS_READ)
        shm.seek(0)
        message = shm.read(BUFFER_SIZE).rstrip(b'\x00').decode('utf-8')
        print(f"[ПОТРЕБИТЕЛЬ] Принято сообщение: {message}")
        shm.close()


if __name__ == "__main__":
    shared_file = "shared_memory_buffer"

    with open(shared_file, "wb") as f:
        f.write(b'\x00' * BUFFER_SIZE)

    p1 = multiprocessing.Process(target=producer, args=(shared_file,))
    p2 = multiprocessing.Process(target=consumer, args=(shared_file,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    os.remove(shared_file)
