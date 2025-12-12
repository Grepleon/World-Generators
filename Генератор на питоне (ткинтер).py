import msvcrt
import random
from tkinter import *
import random as r
import time as t
from tkinter import messagebox
from tkinter import ttk
import math

segs_size = 20
slos = 0
root = Tk()
root.title('Game')
canvas = Canvas(root, width=350, height=500, bg='green')
canvas.grid()
canvas.pack(anchor=CENTER, expand=1)

""""
python_image = PhotoImage(file="FON_COMPUTER_DARK+.png")
paus_image = PhotoImage(file="Settings.png")
canvas.create_image(0, 0, anchor=NW, image=python_image)
"""

sp = []
def gor():

    print('n')
    global biom, z , sp
    sp = []
    x = 579
    z = []
    biom = []
    for i in range(100*100):
        canvas.delete(f'{i}nn')
    for i in range(10000):
        z.append(r.randint(-100, 100))
    for i in range(10000):
        biom.append(r.randint(-80, 80))
    for i in range(12):
        for i in range(8000):
            z[i + 500] = (z[i + 501] + z[i + 499] + z[i + 580] + z[i + 420]) / 4
            z[i + 30] *= 1.35
    for i in range(12):
        for i in range(8000):
            biom[i + 500] = (biom[i + 501] + biom[i + 499] + biom[i + 580] + biom[i + 420]) / 4
            biom[i + 30] *= 1.35


    for u in range (94):
        for i in range(80):
            x+=1
            if z[x]>20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x]<-100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'



                if z[x] > 200:

                    if r.randint(1,10)!=10:

                        color = '#8a8a8a'

                    else:
                        if biom[x]>100:
                            color = '#ab9a9a'

                        else:
                            color = '#ffffff'
                    if z[x]>350:
                        if biom[x]>100:
                            color = '#d62f2f'
                        else:
                            if biom[x]<-100:
                                color = '#ffffff'
                            else:

                                color = '#ab9a9a'


            elif z[x] < -40:
                if biom[x]>100:
                    color = '#0b11d6'
                elif biom[x]<-250:
                    color ='#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x]<-30:
                    color = '#16b8c9'
                else:
                    if biom[x]<-100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 8
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
    print(len(sp))



x = 1
y = 1
n = 579

def led():
    global biom,z,sp
    x= 579
    biom = []
    for i in range (100*100):
        canvas.delete(f'{i}nn')
        biom.append(-1000)
    for u in range(94):
        for i in range(80):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'

                if z[x] > 200:

                    if r.randint(1, 10) != 10:

                        color = '#8a8a8a'
                        if biom[x]<-100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'

                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:

                                color = '#ab9a9a'


            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'



            coof = 8
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof*u,coof*i,coof*u+coof,coof*i,fill=color)
            canvas.create_line(coof * u, coof * i, coof * u , coof * i+ coof, fill=color)
def tepl():
    global biom,z,sp
    x= 579
    biom = []
    for i in range (100*100):
        canvas.delete(f'{i}nn')
        biom.append(1000)
    for u in range(94):
        for i in range(80):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'

                if z[x] > 200:

                    if r.randint(1, 10) != 10:

                        color = '#8a8a8a'
                        if biom[x]<-100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'

                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:

                                color = '#ab9a9a'


            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 8
            sp.append(color)
            canvas.create_rectangle(u * coof, i * coof, u * coof + coof, i * coof + coof, fill=color, tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)

def zelen():
    global biom, z, sp
    x = 579
    biom = []
    for i in range(100 * 100):
        canvas.delete(f'{i}nn')
        biom.append(0)
    for u in range(94):
        for i in range(80):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'
                if z[x] > 200:
                    if r.randint(1, 10) != 10:
                        color = '#8a8a8a'
                        if biom[x] < -100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'
                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:
                                color = '#ab9a9a'
            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 8
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
def full_water():
    global biom, z, sp
    x = 579

    z = []
    for i in range(100 * 100):
        canvas.delete(f'{i}nn')
        z.append(-100)
    for u in range(94):
        for i in range(80):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'
                if z[x] > 200:
                    if r.randint(1, 10) != 10:
                        color = '#8a8a8a'
                        if biom[x] < -100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'
                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:
                                color = '#ab9a9a'
            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 8
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
def epid():
    global biom, z, sp
    x = 579



    for u in range(94):
        for i in range(80):
            x += 1
            if z[x]>-50:
                color = 'black'
                if r.randint(1, 96) == 1:
                    if biom[x] > 50:
                        color = '#363410'
                    else:
                        color = '#2c4004'
                if z[x]+1 <-60 or z[x]-1 <-60 or z[x]-80<-60 or z[x]+80<-60:
                    if r.randint(1,60) == 30:
                        color = '#6e3f0a'
                if z[x] > 300:
                    if r.randint(1, 10) == 1:
                        if biom[x]>60:
                            color = '#9c9522'

                        else:
                            color = '#5fa10a'
                if z[x]>200:
                    if r.randint(1,3)==1:
                        if biom[x]>50:
                            color = '#363410'
                        else:
                            color = '#2c4004'
            elif z[x]<-120:
                if biom[x]>50:
                    color = '#45206e'
                elif biom[x]<-50:
                    color = '#3b0d80'
                else:
                    color = '#38229c'
            else:

                color = '#211430'
            coof = 8
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)

def full_s():
    global biom, z, sp
    x = 579


    for i in range(100 * 100):
        canvas.delete(f'{i}nn')
        if z[i] <-20:
            z[i] = abs(z[i])/4
            biom[i] = abs(biom[i])/4
    for u in range(94):
        for i in range(80):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'
                if z[x] > 200:
                    if r.randint(1, 10) != 10:
                        color = '#8a8a8a'
                        if biom[x] < -100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'
                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:
                                color = '#ab9a9a'
            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 8
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
def rel():
    global biom, z, sp
    x = 579


    for i in range(100 * 100):
        canvas.delete(f'{i}nn')

    for u in range(94):
        for i in range(80):
            Voz = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']

            x += 1
            if not int((z[x]+700) // (5)) >255:
                rel = Voz[int((z[x]+700) // (6))]
            else:
                rel = 255
            coof = 8

            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=f'#{rel}{rel}{rel}',tags=f'{x}nn')
            color = f'#{rel}{rel}{rel}'
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
#GP
def gor2():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    print('n')
    global biom, z , sp
    sp = []
    x = 1079
    z = []
    biom = []
    X = 200
    Y = 100
    for i in range(100 * 1000):
        canvas.delete(f'{i}nn')
    for i in range(20000):
        z.append(r.randint(-100, 100))
    for i in range(20000):
        biom.append(r.randint(-80, 80))
    for i in range(12):
        for i in range(16000):
            z[i + 500] = (z[i + 501] + z[i + 499] + z[i + 580] + z[i + 420]) / 4
            z[i + 30] *= 1.35
    for i in range(12):
        for i in range(16000):
            biom[i + 500] = (biom[i + 501] + biom[i + 499] + biom[i + 580] + biom[i + 420]) / 4
            biom[i + 30] *= 1.35


    for u in range (94 * 2):
        for i in range(80):
            x+=1
            if z[x]>20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x]<-100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'



                if z[x] > 200:

                    if r.randint(1,10)!=10:

                        color = '#8a8a8a'

                    else:
                        if biom[x]>100:
                            color = '#ab9a9a'

                        else:
                            color = '#ffffff'
                    if z[x]>350:
                        if biom[x]>100:
                            color = '#d62f2f'
                        else:
                            if biom[x]<-100:
                                color = '#ffffff'
                            else:

                                color = '#ab9a9a'


            elif z[x] < -40:
                if biom[x]>100:
                    color = '#0b11d6'
                elif biom[x]<-250:
                    color ='#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x]<-30:
                    color = '#16b8c9'
                else:
                    if biom[x]<-100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 8
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
    print(len(sp))



x = 1
y = 1
n = 579

def led2():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom,z,sp
    x= 579
    biom = []
    for i in range (1000*100):
        canvas.delete(f'{i}nn')
        biom.append(-1000)
    for u in range(94 * 2):
        for i in range(80):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'

                if z[x] > 200:

                    if r.randint(1, 10) != 10:

                        color = '#8a8a8a'
                        if biom[x]<-100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'

                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:

                                color = '#ab9a9a'


            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'



            coof = 8
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof*u,coof*i,coof*u+coof,coof*i,fill=color)
            canvas.create_line(coof * u, coof * i, coof * u , coof * i+ coof, fill=color)
def tepl2():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom,z,sp
    x= 579
    biom = []
    for i in range (100*1000):
        canvas.delete(f'{i}nn')
        biom.append(1000)
    for u in range(94 * 2):
        for i in range(80):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'

                if z[x] > 200:

                    if r.randint(1, 10) != 10:

                        color = '#8a8a8a'
                        if biom[x]<-100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'

                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:

                                color = '#ab9a9a'


            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 8
            sp.append(color)
            canvas.create_rectangle(u * coof, i * coof, u * coof + coof, i * coof + coof, fill=color, tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)

def zelen2():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom, z, sp
    x = 579
    biom = []
    for i in range(100 * 1000):
        canvas.delete(f'{i}nn')
        biom.append(0)
    for u in range(94 * 2):
        for i in range(80):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'
                if z[x] > 200:
                    if r.randint(1, 10) != 10:
                        color = '#8a8a8a'
                        if biom[x] < -100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'
                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:
                                color = '#ab9a9a'
            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 8
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
def full_water2():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom, z, sp
    x = 579

    z = []
    for i in range(100 * 1000):
        canvas.delete(f'{i}nn')
        z.append(-100)
    for u in range(94 * 2):
        for i in range(80):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'
                if z[x] > 200:
                    if r.randint(1, 10) != 10:
                        color = '#8a8a8a'
                        if biom[x] < -100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'
                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:
                                color = '#ab9a9a'
            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 8
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
def epid2():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom, z, sp
    x = 579
    for u in range(94 * 2):
        for i in range(80):
            x += 1
            if z[x]>-50:
                color = 'black'
                if r.randint(1, 96) == 1:
                    if biom[x] > 50:
                        color = '#363410'
                    else:
                        color = '#2c4004'
                if z[x]+1 <-60 or z[x]-1 <-60 or z[x]-80<-60 or z[x]+80<-60:
                    if r.randint(1,60) == 30:
                        color = '#6e3f0a'
                if z[x] > 300:
                    if r.randint(1, 10) == 1:
                        if biom[x]>60:
                            color = '#9c9522'

                        else:
                            color = '#5fa10a'
                if z[x]>200:
                    if r.randint(1,3)==1:
                        if biom[x]>50:
                            color = '#363410'
                        else:
                            color = '#2c4004'
            elif z[x]<-120:
                if biom[x]>50:
                    color = '#45206e'
                elif biom[x]<-50:
                    color = '#3b0d80'
                else:
                    color = '#38229c'
            else:

                color = '#211430'
            coof = 8
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)

def full_s2():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom, z, sp
    x = 579


    for i in range(100 * 1000):
        canvas.delete(f'{i}nn')
        if z[i] <-20:
            z[i] = abs(z[i])/4
            biom[i] = abs(biom[i])/4
    for u in range(94 * 2):
        for i in range(80):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'
                if z[x] > 200:
                    if r.randint(1, 10) != 10:
                        color = '#8a8a8a'
                        if biom[x] < -100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'
                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:
                                color = '#ab9a9a'
            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 8
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
def rel2():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom, z, sp
    x = 579


    for i in range(100 * 1000):
        canvas.delete(f'{i}nn')

    for u in range(94 * 2):
        for i in range(80):
            Voz = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']

            x += 1
            if not int((z[x]+700) // (5)) >255:
                rel = Voz[int((z[x]+700) // (6))]
            else:
                rel = 255
            coof = 8

            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=f'#{rel}{rel}{rel}',tags=f'{x}nn')
            color = f'#{rel}{rel}{rel}'
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)

#KP

def gor3():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    print('n')
    global biom, z , sp
    sp = []
    x = 1079
    z = []
    biom = []
    X = 200
    Y = 100
    MEGACOOF = 1.35
    PA3MAX = 100
    for i in range(100 * 5000):
        canvas.delete(f'{i}nn')
    for i in range(20000 * 8 * 4):
        z.append(r.randint(-PA3MAX, PA3MAX))
    for i in range(20000 * 8 * 4):
        biom.append(r.randint(-80, 80))
    for i in range(12):
        for i in range(16000 * 8 * 4):
            z[i + 500] = (z[i + 500 + 1] + z[i + 500 - 1] + z[i + 500 + 80 * 4] + z[i + 500 - 80 * 4]) / 4
            z[i + 30] *= MEGACOOF
    for i in range(12):
        for i in range(16000 * 8 * 4):
            biom[i + 500] = (biom[i + 500 - 1] + biom[i + 500 + 1] + biom[i + 500 - 80 * 4] + biom[i + 500 + 80 * 4]) / 4
            biom[i + 30] *= 1.35


    for u in range (94 * 8):
        for i in range(80 * 4):
            x+=1
            if z[x]>20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x]<-100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'



                if z[x] > 200:

                    if r.randint(1,10)!=10:

                        color = '#8a8a8a'

                    else:
                        if biom[x]>100:
                            color = '#ab9a9a'

                        else:
                            color = '#ffffff'
                    if z[x]>350:
                        if biom[x]>100:
                            color = '#d62f2f'
                        else:
                            if biom[x]<-100:
                                color = '#ffffff'
                            else:

                                color = '#ab9a9a'


            elif z[x] < -40:
                if biom[x]>100:
                    color = '#0b11d6'
                elif biom[x]<-250:
                    color ='#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x]<-30:
                    color = '#16b8c9'
                else:
                    if biom[x]<-100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 2
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
    print(len(sp))

def gor_3():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    print('n')
    global biom, z , sp
    sp = []
    x = 1079
    z = []
    biom = []
    X = 200
    Y = 100
    MEGACOOF = 1.1
    PA3MAX = 20
    KOL_BO_PA3 = 35
    for i in range(100 * 5000):
        canvas.delete(f'{i}nn')
    for i in range(20000 * 8 * 4):
        z.append(r.randint(-PA3MAX, PA3MAX))
    for i in range(20000 * 8 * 4):
        A_ = random.randint(1,15000)
        if A_ == 1:
            z[i] = -500
        A_ = random.randint(1, 15000)
        if A_ == 1:
            z[i] = 500
    for i in range(20000 * 8 * 4):
        biom.append(r.randint(-80, 80))
    for i in range(12 * KOL_BO_PA3):
        for i in range(16000 * 8 * 4):
            z[i + 500] = (z[i + 500 + 1] + z[i + 500 - 1] + z[i + 500 + 80 * 4] + z[i + 500 - 80 * 4]) / 4
            z[i + 30] *= MEGACOOF
    for i in range(12):
        for i in range(16000 * 8 * 4):
            biom[i + 500] = (biom[i + 500 - 1] + biom[i + 500 + 1] + biom[i + 500 - 80 * 4] + biom[i + 500 + 80 * 4]) / 4
            biom[i + 30] *= 1.35
    for i in range(16000 * 8 * 4):
        z[i + 500] = 1 * (int(z[i + 500]) / (10 ** len('15531660979840')))
    print(int(3.1459455e+12 ))



    for u in range (94 * 8):
        for i in range(80 * 4):
            MAXHEIGHT = 640
            H = MAXHEIGHT / 2
            coof = 2
            POLOSHEHIE_PO_BbICOTE = math.sin(coof * u / 57.2958) * 15 + (abs(MAXHEIGHT / 2 - coof * i))
            Y = POLOSHEHIE_PO_BbICOTE + random.randint(-10,10)
            x+=1
            if z[x]>20:
                if biom[x] > 220:
                    color = '#d1c436'
                elif biom[x]<-220:
                    color = '#83c9f7'
                else:
                    if Y < 225:
                        if Y > 75:
                            if biom[x] > 100 or biom[x] < -100:
                                color = '#62ff00'
                            else:
                                color = 'green'

                        else:
                            if biom[x] > 100 or biom[x] < -100:
                                color = '#ff9900'
                            else:
                                color = 'orange'

                    else:
                        if biom[x] > 100 or biom[x] < -100:
                            color = '#87bbe8'
                        else:
                            color = '#a9c5de'
                    if 200 < Y < 240:
                        if biom[x] > 100 or biom[x] < -100:
                            color = '#34eba8'
                        else:
                            color = '#46cf91'
                    if 60 < Y < 85:
                        if biom[x] > 100 or biom[x] < -100:
                            color = '#b6cf46'
                        else:
                            color = '#7fe625'






                if z[x] > 500:

                    if r.randint(1,10)!=10:
                        if 75 < Y < 225:
                            color = '#8a8a8a'
                        elif Y < 75:
                            color = '#6b5d5d'
                        elif Y > 225:
                            color = '#cccaca'

                    else:
                        if Y < 75:
                            color = '#ab9a9a'

                        else:
                            color = '#ffffff'
                    if z[x] > 800:
                        if Y < 75:
                            if random.randint(1, 10) != 1:
                              if biom[x] > 100 or biom[x] < -100:
                                  color = '#d62f2f'
                              else:
                                  color = '#f50505'

                        else:
                            if Y > 225:
                                if random.randint(1,10) != 1:
                                    color = '#ffffff'
                            else:
                                if Y > 200:
                                  if random.randint(1, 10) != 1:
                                    color = '#cccccc'
                                else:
                                  if random.randint(1, 10) != 1:
                                    color = '#ab9a9a'


            elif z[x] < -40:
                if Y < 225:
                    if biom[x]>100:
                        color = '#0b11d6'
                    elif biom[x]<-250:
                        color ='#055ce8'
                    else:
                        color = '#002fff'
                else:
                    if biom[x] > 100 or biom[x] < -100:
                        color = '#209cf5'
                    else:
                        color = '#00dff7'
            else:
                if z[x]<-30:
                    color = '#16b8c9'
                else:
                    if biom[x]<-100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 2
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
    print(len(sp))

def gorM():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    print('n')
    global biom, z , sp
    sp = []
    x = 1079
    z = []
    biom = []
    X = 200
    Y = 100
    MEGACOOF = 1.1
    PA3MAX = 20
    KOL_BO_PA3 = 35
    for i in range(100 * 5000):
        canvas.delete(f'{i}nn')
    for i in range(20000 * 8 * 4 * 4):
        z.append(r.randint(-PA3MAX, PA3MAX))
    for i in range(20000 * 8 * 4 * 4):
        A_ = random.randint(1,15000)
        if A_ == 1:
            z[i] = -500
        A_ = random.randint(1, 15000)
        if A_ == 1:
            z[i] = 500
    for i in range(20000 * 8 * 4 * 4):
        biom.append(r.randint(-80, 80))
    for i in range(12 * KOL_BO_PA3):
        for i in range(16000 * 8 * 4 * 4):
            z[i + 500] = (z[i + 500 + 1] + z[i + 500 - 1] + z[i + 500 + 80 * 4] + z[i + 500 - 80 * 4]) / 4
            z[i + 30] *= MEGACOOF
    for i in range(12):
        for i in range(16000 * 8 * 4 * 4):
            biom[i + 500] = (biom[i + 500 - 1] + biom[i + 500 + 1] + biom[i + 500 - 80 * 4] + biom[i + 500 + 80 * 4]) / 4
            biom[i + 30] *= 1.35
    for i in range(16000 * 8 * 4 * 4):
        z[i + 500] = 1 * (int(z[i + 500]) / (10 ** len('15531660979840')))




    for u in range (94 * int(8 * 2)):
        for i in range(80 * 4 * 2):
            MAXHEIGHT = 640
            H = MAXHEIGHT / 2
            coof = 1
            POLOSHEHIE_PO_BbICOTE = math.sin(coof * u / 57.2958) * 15 + (abs(MAXHEIGHT / 2 - coof * i))
            Y = POLOSHEHIE_PO_BbICOTE + random.randint(-10,10)
            x+=1
            if z[x]>20:
                if biom[x] > 220:
                    color = '#d1c436'
                elif biom[x]<-220:
                    color = '#83c9f7'
                else:
                    if Y < 225:
                        if Y > 75:
                            if biom[x] > 100 or biom[x] < -100:
                                color = '#62ff00'
                            else:
                                color = 'green'

                        else:
                            if biom[x] > 100 or biom[x] < -100:
                                color = '#ff9900'
                            else:
                                color = 'orange'

                    else:
                        if biom[x] > 100 or biom[x] < -100:
                            color = '#87bbe8'
                        else:
                            color = '#a9c5de'
                    if 200 < Y < 240:
                        if biom[x] > 100 or biom[x] < -100:
                            color = '#34eba8'
                        else:
                            color = '#46cf91'
                    if 60 < Y < 85:
                        if biom[x] > 100 or biom[x] < -100:
                            color = '#b6cf46'
                        else:
                            color = '#7fe625'






                if z[x] > 500:

                    if r.randint(1,10)!=10:
                        if 75 < Y < 225:
                            color = '#8a8a8a'
                        elif Y < 75:
                            color = '#6b5d5d'
                        elif Y > 225:
                            color = '#cccaca'

                    else:
                        if Y < 75:
                            color = '#ab9a9a'

                        else:
                            color = '#ffffff'
                    if z[x] > 800:
                        if Y < 75:
                            if random.randint(1, 10) != 1:
                              if biom[x] > 100 or biom[x] < -100:
                                  color = '#d62f2f'
                              else:
                                  color = '#f50505'

                        else:
                            if Y > 225:
                                if random.randint(1,10) != 1:
                                    color = '#ffffff'
                            else:
                                if Y > 200:
                                  if random.randint(1, 10) != 1:
                                    color = '#cccccc'
                                else:
                                  if random.randint(1, 10) != 1:
                                    color = '#ab9a9a'


            elif z[x] < -40:
                if Y < 225:
                    if biom[x]>100:
                        color = '#0b11d6'
                    elif biom[x]<-250:
                        color ='#055ce8'
                    else:
                        color = '#002fff'
                else:
                    if biom[x] > 100 or biom[x] < -100:
                        color = '#209cf5'
                    else:
                        color = '#00dff7'
            else:
                if z[x]<-30:
                    color = '#16b8c9'
                else:
                    if biom[x]<-100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'

            #sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
    #print(len(sp))


x = 1
y = 1
n = 579

def led3():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom,z,sp
    x= 579
    biom = []
    for i in range (5000*100):
        canvas.delete(f'{i}nn')
        biom.append(-1000)
    for u in range(94 * 8):
        for i in range(80 * 4):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'

                if z[x] > 200:

                    if r.randint(1, 10) != 10:

                        color = '#8a8a8a'
                        if biom[x]<-100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'

                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:

                                color = '#ab9a9a'


            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'



            coof = 2
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof*u,coof*i,coof*u+coof,coof*i,fill=color)
            canvas.create_line(coof * u, coof * i, coof * u , coof * i+ coof, fill=color)
def tepl3():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom,z,sp
    x= 579
    biom = []
    for i in range (100*5000):
        canvas.delete(f'{i}nn')
        biom.append(1000)
    for u in range(94 * 8):
        for i in range(80 * 4):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'

                if z[x] > 200:

                    if r.randint(1, 10) != 10:

                        color = '#8a8a8a'
                        if biom[x]<-100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'

                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:

                                color = '#ab9a9a'


            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 2
            sp.append(color)
            canvas.create_rectangle(u * coof, i * coof, u * coof + coof, i * coof + coof, fill=color, tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)

def zelen3():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom, z, sp
    x = 579
    biom = []
    for i in range(100 * 5000):
        canvas.delete(f'{i}nn')
        biom.append(0)
    for u in range(94 * 8):
        for i in range(80 * 4):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'
                if z[x] > 200:
                    if r.randint(1, 10) != 10:
                        color = '#8a8a8a'
                        if biom[x] < -100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'
                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:
                                color = '#ab9a9a'
            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 2
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
def full_water3():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom, z, sp
    x = 579

    z = []
    for i in range(100 * 5000):
        canvas.delete(f'{i}nn')
        z.append(-100)
    for u in range(94 * 8):
        for i in range(80 * 4):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'
                if z[x] > 200:
                    if r.randint(1, 10) != 10:
                        color = '#8a8a8a'
                        if biom[x] < -100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'
                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:
                                color = '#ab9a9a'
            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 2
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
def epid3():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom, z, sp
    x = 579
    for u in range(94 * 8):
        for i in range(80 * 4):
            x += 1
            if z[x]>-50:
                color = 'black'
                if r.randint(1, 96) == 1:
                    if biom[x] > 50:
                        color = '#363410'
                    else:
                        color = '#2c4004'
                if z[x]+1 <-60 or z[x]-1 <-60 or z[x]-80<-60 or z[x]+80<-60:
                    if r.randint(1,60) == 30:
                        color = '#6e3f0a'
                if z[x] > 300:
                    if r.randint(1, 10) == 1:
                        if biom[x]>60:
                            color = '#9c9522'

                        else:
                            color = '#5fa10a'
                if z[x]>200:
                    if r.randint(1,3)==1:
                        if biom[x]>50:
                            color = '#363410'
                        else:
                            color = '#2c4004'
            elif z[x]<-120:
                if biom[x]>50:
                    color = '#45206e'
                elif biom[x]<-50:
                    color = '#3b0d80'
                else:
                    color = '#38229c'
            else:

                color = '#211430'
            coof = 2
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)

def full_s3():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom, z, sp
    x = 579


    for i in range(100 * 5000):
        canvas.delete(f'{i}nn')
        if z[i] <-20:
            z[i] = abs(z[i])/4
            biom[i] = abs(biom[i])/4
    for u in range(94 * 8):
        for i in range(80 * 4):
            x += 1
            if z[x] > 20:
                if biom[x] > 100:
                    color = '#d1c436'
                elif biom[x] < -100:
                    color = '#83c9f7'
                else:
                    if biom[x] > 50 or biom[x] < -50:
                        color = '#62ff00'
                    else:
                        color = 'green'
                if z[x] > 200:
                    if r.randint(1, 10) != 10:
                        color = '#8a8a8a'
                        if biom[x] < -100:
                            color = '#759e99'
                    else:
                        if biom[x] > 100:
                            color = '#ab9a9a'
                        else:
                            color = '#ffffff'
                    if z[x] > 350:
                        if biom[x] > 100:
                            color = '#d62f2f'
                        else:
                            if biom[x] < -100:
                                color = '#ffffff'
                            else:
                                color = '#ab9a9a'
            elif z[x] < -40:
                if biom[x] > 100:
                    color = '#0b11d6'
                elif biom[x] < -250:
                    color = '#055ce8'
                else:
                    color = '#002fff'
            else:
                if z[x] < -30:
                    color = '#16b8c9'
                else:
                    if biom[x] < -100:
                        color = '#36bcd1'
                    else:
                        color = '#f2ff00'
            coof = 2
            sp.append(color)
            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=color,tags=f'{x}nn')
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
def rel3():
    root = Tk()
    root.title('Game')
    canvas = Canvas(root, width=1200, height=640, bg='green')
    canvas.grid()
    canvas.pack(anchor=CENTER, expand=1)
    global biom, z, sp
    x = 579


    for i in range(100 * 5000):
        canvas.delete(f'{i}nn')

    for u in range(94 * 8):
        for i in range(80 * 4):
            Voz = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']

            x += 1
            if not int((z[x]+700) // (5)) >255:
                rel = Voz[int((z[x]+700) // (6))]
            else:
                rel = 255
            coof = 2

            canvas.create_rectangle(u*coof,i*coof,u*coof+coof,i*coof+coof,fill=f'#{rel}{rel}{rel}',tags=f'{x}nn')
            color = f'#{rel}{rel}{rel}'
            canvas.create_line(coof * u, coof * i, coof * u + coof, coof * i, fill=color)
            canvas.create_line(coof * u, coof * i, coof * u, coof * i + coof, fill=color)
#BT
def _EXIT_():
    exit(1)
def go (event):
    global x , y , n , biom , z
    if event.char == 'd':
        x+=8
        n+=1

    if event.char == 'a':
        x-=8
        n-=1

    if event.char == 's':
        y+=8
        n+=80

    if event.char == 'w':
        y-=8
        n-=80

    print(z[n])
    canvas.delete('GO_G')
    canvas.create_rectangle(x,y,x+4,y+4,tags = 'GO_G',fill=
    '#9505e8')
    print(x,y)
root.bind('<Key>', go)

Fbt = Button(text=f' Фон'.format('i', 'r'), bg='black', foreground='green', padx='35', pady='12',
            font='34', command=gor)
Frt = Button(text=f' Фон'.format('i', 'r'), bg='black', foreground='blue', padx='35', pady='12',
            font='34', command=led)
Ftt = Button(text=f' Фон'.format('i', 'r'), bg='black', foreground='orange', padx='35', pady='12',
            font='34', command=tepl)
Fzt = Button(text=f' Фон'.format('i', 'r'), bg='black', foreground='#56e034', padx='35', pady='12',
            font='34', command=zelen)
Ffo = Button(text=f' Фон'.format('i', 'r'), bg='black', foreground='blue', padx='35', pady='12',
            font='34', command=full_water)
Ffs = Button(text=f' Фон'.format('i', 'r'), bg='black', foreground='orange', padx='35', pady='12',
            font='34', command=full_s)

Fep = Button(text=f' Фон'.format('i', 'r'), bg='black', foreground='#36165c', padx='35', pady='12',
            font='34', command=epid)
Fbw = Button(text=f' Фон'.format('i', 'r'), bg='black', foreground='white', padx='35', pady='12',
            font='34', command=rel)

Ftt.place(relx=.12, rely=.25, anchor='c')
Frt.place(relx=.12, rely=.15, anchor='c')
Fzt.place(relx=.12, rely=.35, anchor='c')
Fbt.place(relx=.12, rely=.05, anchor='c')
Ffo.place(relx=.12,rely=.45,anchor='c')
Ffs.place(relx=.12,rely=.55,anchor='c')
Fep.place(relx=.12,rely=.65,anchor='c')

Gbt = Button(text=f' Генератор'.format('i', 'r'), bg='black', foreground='green', padx='10', pady='12',
            font='34', command=gor2)
Grt = Button(text=f' Генератор'.format('i', 'r'), bg='black', foreground='blue', padx='10', pady='12',
            font='34', command=led2)
Gtt = Button(text=f' Генератор'.format('i', 'r'), bg='black', foreground='orange', padx='10', pady='12',
            font='34', command=tepl2)
Gzt = Button(text=f' Генератор'.format('i', 'r'), bg='black', foreground='#56e034', padx='10', pady='12',
            font='34', command=zelen2)
Gfo = Button(text=f' Генератор'.format('i', 'r'), bg='black', foreground='blue', padx='10', pady='12',
            font='34', command=full_water2)
Gfs = Button(text=f' Генератор'.format('i', 'r'), bg='black', foreground='orange', padx='10', pady='12',
            font='34', command=full_s2)
Gep = Button(text=f' Генератор'.format('i', 'r'), bg='black', foreground='#36165c', padx='10', pady='12',
            font='34', command=epid2)
Gbw = Button(text=f' Генератор'.format('i', 'r'), bg='black', foreground='white', padx='10', pady='12',
            font='34', command=rel2)

Gtt.place(relx=.84, rely=.25, anchor='c')
Grt.place(relx=.84, rely=.15, anchor='c')
Gzt.place(relx=.84, rely=.35, anchor='c')
Gbt.place(relx=.84, rely=.05, anchor='c')
Gfo.place(relx=.84,rely=.45,anchor='c')
Gfs.place(relx=.84,rely=.55,anchor='c')
Gep.place(relx=.84,rely=.65,anchor='c')

Kbt = Button(text=f'Остров '.format('i', 'r'), bg='black', foreground='green',   padx='0 ', pady='12',
            font='34', command=gor3)
KbT = Button(text=f'Материк'.format('i', 'r'), bg='black', foreground='green',  padx='0 ', pady='12',
            font='34', command=gor_3)
Krt = Button(text=f' Большой'.format('i', 'r'), bg='black', foreground='blue',   padx='20', pady='12',
            font='34', command=led3)
Ktt = Button(text=f' Большой'.format('i', 'r'), bg='black', foreground='orange', padx='20', pady='12',
            font='34', command=tepl3)
Kzt = Button(text=f' Большой'.format('i', 'r'), bg='black', foreground='#56e034',padx='20', pady='12',
            font='34', command=zelen3)
Kfo = Button(text=f' Большой'.format('i', 'r'), bg='black', foreground='blue',   padx='20', pady='12',
            font='34', command=full_water3)
Kfs = Button(text=f' Большой'.format('i', 'r'), bg='black', foreground='orange', padx='20', pady='12',
            font='34', command=full_s3)
Kep = Button(text=f' Большой'.format('i', 'r'), bg='black', foreground='#36165c',padx='20', pady='12',
            font='34', command=epid3)
Kbw = Button(text=f' Большой'.format('i', 'r'), bg='black', foreground='white',  padx='20', pady='12',
            font='34', command=rel3)

Ktt.place(relx=.48, rely=.25, anchor='c')
Krt.place(relx=.48, rely=.15, anchor='c')
Kzt.place(relx=.48, rely=.35, anchor='c')
Kbt.place(relx=.36, rely=.05, anchor='c')
KbT.place(relx=.59, rely=.05, anchor='c')
Kfo.place(relx=.48, rely=.45, anchor='c')
Kfs.place(relx=.48, rely=.55, anchor='c')
Kep.place(relx=.48, rely=.65, anchor='c')

_ENDING_ = Button(text=f'выход'.format('i', 'r'), bg='black', foreground='red', padx='20', pady='12',
            font='34', command=_EXIT_)
_ENDING_.place(relx=.48, rely=.91, anchor='c')

Mbt = Button(text=f'МЕГА '.format('i', 'r'), bg='black', foreground='green',   padx='0 ', pady='12',
            font='34', command=gorM)
Mbt.place(relx=.15, rely=.91, anchor='c')
gor()

root.mainloop()

#секретный шифр: «55:45  48:44»
