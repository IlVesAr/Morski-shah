from tkinter import *


o_ta = StringVar()
x_ove = StringVar()
# napravi gi tez


koi = 0

x = [0, 0, 0]
y = [0, 0, 0]
d = [0, 0]

x_o = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]
for x in x_o:
    x.set(".")

def puton(c):
    global x, y, d
    global koi
    global x_o
    if koi % 2 == 0:
        x[(c % 3) - 1] += 4
        y[c // 3] += 4
        if (c // 2) == 1 and 1 != c != 9:
            d[1] += 4
        if (c // 2) == 1 and 3 != c != 7:
            d[2] += 4

        #cikli za proverka dali ima popalneni redove

    else:
        x[(c % 3) - 1] += 1
        y[c // 3] += 1
        if (c // 2) == 1 and 1 != c != 9:
            d[1] += 1
        if (c // 2) == 1 and 3 != c != 7:
            d[2] += 1


