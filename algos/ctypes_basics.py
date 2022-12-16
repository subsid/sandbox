import ctypes
import threading
import time

def py_loop(i, j):
    s = 0
    for i in range(i, j):
        if (i % 3 == 0):
            s += 1
    return s

# Compile library
# gcc -fPIC -shared -o clibrary.so clibrary.c

clibrary = ctypes.CDLL("./clibrary.so")

# clibrary.display(b"Sid", 18)

# func = clibrary.display

# func.argtypes = [ctypes.c_char_p, ctypes.c_int]
# func.restype = ctypes.c_char_p

# func(b"Sid", 18)

c_loop = clibrary.loop
c_loop.argtypes = [ctypes.c_int, ctypes.c_int]
c_loop.restype = ctypes.c_int
end = 1 * 10**9
fmt = lambda t: f"{t:.2f}"

tic = time.perf_counter()
py_loop(0, end)
py_loop(0, end)
py_loop(0, end)
py_loop(0, end)
print(f"Sequential runtime py_loop {fmt(time.perf_counter() - tic)} Seconds")

tic = time.perf_counter()
t1 = threading.Thread(target=py_loop, args=[0, end])
t2 = threading.Thread(target=py_loop, args=[0, end])
t3 = threading.Thread(target=py_loop, args=[0, end])
t4 = threading.Thread(target=py_loop, args=[0, end])
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print(f"Parallet runtime py_loop {fmt(time.perf_counter() - tic)} Seconds")

tic = time.perf_counter()
c_loop(0, end)
c_loop(0, end)
c_loop(0, end)
c_loop(0, end)
print(f"Sequential runtime c_loop {fmt(time.perf_counter() - tic)} Seconds")

tic = time.perf_counter()
t1 = threading.Thread(target=c_loop, args=[0, end])
t2 = threading.Thread(target=c_loop, args=[0, end])
t3 = threading.Thread(target=c_loop, args=[0, end])
t4 = threading.Thread(target=c_loop, args=[0, end])
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print(f"Parallet runtime c_loop {fmt(time.perf_counter() - tic)} Seconds")
