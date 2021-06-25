from tkinter import *
from highway import *
import time


def clearCanvas(n, canvWidth, canvHeight, array):
    newCanv = Canvas(root, width=canvWidth, height=canvHeight, bg='white')
    yStart = canvHeight / 2 - (1 / 2) * canvWidth / n
    for i in range(0, len(array)):
        newCanv.create_line((canvWidth / n) * i, yStart, (canvWidth / n) * i, canvWidth / n + yStart, width=3)
        if array[i] == 1:
            newCanv.create_oval((canvWidth / n) * i + 5, yStart + 5, (canvWidth / n) * i + (canvWidth / n) - 5,
                                canvWidth / n + yStart - 5, width=3)
    newCanv.create_line(0, canvWidth / n + yStart, canvWidth, canvWidth / n + yStart, width=5)
    newCanv.create_line(0, yStart, canvWidth, yStart, width=5)
    return newCanv


col = 10
cls = Road(6, col)
arr = cls.getMatrix()
root = Tk()
canv = clearCanvas(col, 1000, 300, arr)
canv.pack()

for j in range(100):
    arr = cls.makeMove()
    canv.destroy()
    canv = clearCanvas(col, 1000, 300, arr)
    canv.pack()
    root.update()
    time.sleep(1)

root.mainloop()

