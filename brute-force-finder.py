from PIL import Image

# constants
height = 17
width = 17

def formula(x, y):
    return 0.5 < ((y//17) >> (17*x+(y%17))) % 2

def is_equal(bitmap, start, size, flipx=False, flipy=False):
    startx = start[0]
    starty = start[1]
    width = size[0]
    height = size[1]
    for x in range(width):
        for y in range(height):
            y_hat = y if flipy else height-y-1
            x_hat = x if flipx else width-x-1
            if bitmap[x_hat, y_hat] != ((255, 255, 255) if formula(x + startx, y + starty) else (0, 0, 0)):
                return False
    return True

def thread_function(thread_index, thread_count):
    with Image.open("babi.png") as img:
        bitmap = img.load()
        y = height*thread_index
        while True:
            y += height*thread_count
            if is_equal(bitmap, (0, y), (width, height)):
                print(y)
            if y % (1000000*height*thread_count) == 0:
                print(f"Thread {thread_index} is @ {y}")

from multiprocessing import Process, Manager, Value, Array
import math
thread_count = 16

with Manager() as manager:
    thread_index = 0
    threads = []
    for i in range(thread_count):
        th = Process(target=thread_function, args=(thread_index, thread_count), daemon=True)
        th.start()
        threads.append(th)
        thread_index += 1
    for th in threads:
        th.join()

print("UwU aww my thweads awe done ଘ(੭ ˘ ᵕ˘)━☆ﾟ.*･｡ﾟᵕ꒳ᵕ~") # will not happen
