import _thread
import os
import time

res = 100000000
x = 51224000
y = 30204000
quality = 100
speed = 0.95

n=100000
os.system("gcc mandelbrot.c -o mandelbrot")
start = res
while res>=100:
    command = f"./mandelbrot {res} {x-quality} {x+quality} {y-quality} {y+quality} > {n}.ppm && magick {n}.ppm {n}mandelbrotframe.jpeg && rm {n}.ppm";
    _thread.start_new_thread(os.system, (command,))
#    time.sleep(.1)

    res=res*speed
    x=x*speed
    y=y*speed
    n=n-1

processes = 1

while True:
    if os.system('pgrep magick') == 256:
        if os.system('pgrep mandelbrot') == 256:
            break
    time.sleep(1)
print("done")
os.system("magick -delay 10 -loop 0 *jpeg mandelbrot.gif &&rm *mandelbrotframe.jpeg")
