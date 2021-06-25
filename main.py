from tqdm import tqdm
import time
from tkinter import *


# for i in tqdm(range(100)):
#     time.sleep(0.1)

def clearCanvas():
    canv.clipboard_clear()


root = Tk()

canv = Canvas(root, width=1000, height=500, bg='white')
canv.pack()
canv.create_line(10, 10, 190, 50)
# clearCanvas()
root.destroy()
canv.create_line(100, 100, 1900, 500)
root.mainloop()


# def print_hi(name):
#     print(f'Hi, {name}')
#
#
# if __name__ == '__main__':
#     print_hi('PyCharm')
