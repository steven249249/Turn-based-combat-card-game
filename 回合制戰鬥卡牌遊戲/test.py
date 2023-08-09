# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 18:02:21 2023

@author: user
"""

import tkinter as tk

def remove_image():
    button['image'] = ''
    button['command'] = ''
    print(1)
root = tk.Tk()

image = tk.PhotoImage(file="cards/card_vgr.gif")  # 替换为你的按钮图像路径

button = tk.Button(root, image=image, command=remove_image)
button.pack()

root.mainloop()