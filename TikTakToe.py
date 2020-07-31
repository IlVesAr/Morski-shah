from tkinter import *

kk = Tk()

rez_o = 0
rez_x = 0
o_ta = StringVar(kk)
x_ove = StringVar(kk)

o_ta.set(f"O-ta: {rez_o}")
x_ove.set(f"X-ove: {rez_x}")

koi = 0

x = [0, 0, 0]
y = [0, 0, 0]
d = [0, 0]

butoni = [True, True, True, True, True, True, True, True, True]

x_o = [StringVar(kk), StringVar(kk), StringVar(kk), StringVar(kk), StringVar(kk), StringVar(kk), StringVar(kk),
       StringVar(kk),
       StringVar(kk)]

for i in x_o:
    i.set(".")


def nulirane():
    global x, y, d, koi, x_o, butoni
    x = [0, 0, 0]
    y = [0, 0, 0]
    d = [0, 0]

    koi = 0

    butoni = [True, True, True, True, True, True, True, True, True]

    for i2 in x_o:
        i2.set(".")


def cikal(kol, koia, a):
    global x_o, koi

    global x, y, d

    for i1 in a:
        if i1 == kol:
            koia += 1

            nulirane()

            break

    return koia


def check(kol, koia):
    global x, y, d, x_o
    koia = cikal(kol, koia, x)

    koia = cikal(kol, koia, y)

    koia = cikal(kol, koia, d)

    return koia


def puton(c):
    global rez_o, rez_x
    global x, y, d
    global koi
    global x_o
    global butoni

    if butoni[c - 1]:
        if koi % 2 == 0:
            x[(c % 3) - 1] += 4
            y[(c - 1) // 3] += 4
            if (c % 2) == 1 and 1 != c and c != 9:
                d[0] += 4
            if (c % 2) == 1 and 3 != c and c != 7:
                d[1] += 4

            x_o[c - 1].set("O")

            rez_o = check(12, rez_o)

        else:
            x[(c % 3) - 1] += 1
            y[(c - 1) // 3] += 1
            if (c % 2) == 1 and 1 != c != 9:
                d[0] += 1
            if (c % 2) == 1 and 3 != c != 7:
                d[1] += 1

            x_o[c - 1].set("X")

            rez_x = check(3, rez_x)

        butoni[c - 1] = False

        koi += 1

    o_ta.set(f"O-ta: {rez_o}")
    x_ove.set(f"X-ove: {rez_x}")


bt1 = Button(kk, textvariable=x_o[0], command=lambda: puton(1))
bt1.pack()
bt1.place(x=10, y=10)

bt1 = Button(kk, textvariable=x_o[1], command=lambda: puton(2))
bt1.pack()
bt1.place(x=30, y=10)

bt1 = Button(kk, textvariable=x_o[2], command=lambda: puton(3))
bt1.pack()
bt1.place(x=50, y=10)

bt1 = Button(kk, textvariable=x_o[3], command=lambda: puton(4))
bt1.pack()
bt1.place(x=10, y=36)

bt1 = Button(kk, textvariable=x_o[4], command=lambda: puton(5))
bt1.pack()
bt1.place(x=30, y=36)

bt1 = Button(kk, textvariable=x_o[5], command=lambda: puton(6))
bt1.pack()
bt1.place(x=50, y=36)

bt1 = Button(kk, textvariable=x_o[6], command=lambda: puton(7))
bt1.pack()
bt1.place(x=10, y=62)

bt1 = Button(kk, textvariable=x_o[7], command=lambda: puton(8))
bt1.pack()
bt1.place(x=30, y=62)

bt1 = Button(kk, textvariable=x_o[8], command=lambda: puton(9))
bt1.pack()
bt1.place(x=50, y=62)

bt2 = Button(kk, text="Clear", command=nulirane)
bt2.pack()
bt2.place(x=70, y=80)

lb = Label(kk, textvariable=o_ta)
lb.pack()
lb.place(x=10, y=100)

lb2 = Label(kk, textvariable=x_ove)
lb2.pack()
lb2.place(x=10, y=130)

kk.mainloop()
