import _thread
import os
from time import sleep
from threading import Semaphore

res = 1080
x = -0.5581939960512976
y = -0.63693935931071
maxZoom = 10000000000
speed = 1.02

n=1000000
os.system("gcc mandelbrot.c -o mandelbrot")
zoom = 0.2
n=1000000
batch = 1000000
batchSize=25
maxBatches = -1

testZoom=zoom
while (testZoom<maxZoom):
    maxBatches=maxBatches+1
    renderBatch=batchSize
    while renderBatch>0:
        renderBatch=renderBatch-1
        testZoom=testZoom*speed


while (zoom<maxZoom):
    renderBatch = batchSize
    while renderBatch>0:
        renderBatch=renderBatch-1
        command = f"./mandelbrot  {zoom} {res} {x} {y} > {n}mandelbrotframe.ppm && magick {n}mandelbrotframe.ppm {n}mandelbrotframe.gif && rm {n}mandelbrotframe.ppm" #&& echo {zoom / maxZoom*100}%"
        _thread.start_new_thread(os.system, (command,))
        zoom=zoom*speed
        n=n+1
        sleep(0.1)

    while True:
        if os.system('pgrep magick > /dev/null 2>&1') == 256:
            if os.system('pgrep mandelbrot > /dev/null 2>&1') == 256:
                break
        sleep(1)

    print("batch " , batch - 1000000 , "/", maxBatches , " done")
    command = f"magick -delay 10 -loop 0 *mandelbrotframe.gif batch{batch}.gif &&rm *mandelbrotframe.gif "
    os.system(command)
    batch=batch+1

os.system("magick -delay 10 -loop 0 batch* mandelbrot.gif && rm batch* ")
