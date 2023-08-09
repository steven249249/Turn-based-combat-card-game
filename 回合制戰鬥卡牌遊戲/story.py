# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:07:49 2020

@author: Yurax
"""

import tkinter as tk



import random
from PIL import ImageTk, Image, ImageSequence
import threading 


class Story():
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(master)
        self.canvas=tk.Canvas(self.frame, width=1280, height=720)
        canvas2=self.canvas        
        canvas2.pack()
        self.imgfile_s_pro = tk.PhotoImage(file='story_image/Pro.gif')
        self.imgfile_s_ming = tk.PhotoImage(file='story_image/Ming.gif')
        self.imgfile_s_car = tk.PhotoImage(file='story_image/Car.gif')
        self.imgfile_s_background = tk.PhotoImage(file='story_image/storybackground.gif')
        self.imgfile_s_background_b = tk.PhotoImage(file='story_image/storybackground_b.gif')
    
        self.text_var = tk.StringVar()
        self.wait_var = tk.IntVar()
        self.text = tk.Label(canvas2, textvariable=self.text_var, font=('微軟正黑體',24), fg= 'black')
        self.text.place(x=640,y=500,anchor='center')
        self.next_b = tk.Button(canvas2, text="Next", command=lambda: self.wait_var.set(1))
        self.next_b.place(x=1200,y=700,anchor='center')
        
        path_map1 = 'story_image/background1.gif'
        background1=Image.open(path_map1)
        path_map2 = 'story_image/background2.gif'
        background2=Image.open(path_map2)
        self.index = 0
        self.act_list = []
        self.img = ImageTk.PhotoImage(background1.resize((1280, 720), Image.ANTIALIAS))
        
        self.bg = canvas2.create_image(0, 0, anchor=tk.NW, image=self.img) 
        
        self.img2= ImageTk.PhotoImage(background2.resize((1280, 720), Image.ANTIALIAS))
    def switch_frame(self):
        
        self.wait_var.set(1000)

    def get_frame(self):
        return self.frame
    def story1(self):
        global index,act_list
        self.frame.pack()
        self.skip = tk.Button(self.frame, text="skip", command=lambda: self.switch_frame())
        self.skip.place(x=1160,y=700,anchor='center')
        self.wait_var.set(0)
        self.act_list = [["又是個風和日麗的一天","同時xx大學也迎來了學期末","不過某間教學講堂內並不怎麼平靜"],
                    "pro_in",
                    ["教授：你這甚麼意思！！？有種再說一遍！！！"],
                    "ming_in",
                    ["小明：還好啦，在座各位也覺得我說得很對沒錯吧？","小明：教授你的學養就這點程度而已嗎，這期末考題根本就是個笑話","小明：我可是拿到了滿分呢，哈哈哈","小明：啊？！不好意思啊，我忘記在座的各位沒一個及格是吧？哈哈哈"],
                    ["教授：你......你......","教授：你給我......"],
                    ["小明：恩？教授想說甚麼呢，我可是在這浪費時間聽著呢","小明：啊啊，我這樣讓你很難調分對吧，誰叫你出這種鳥題目呢，哈哈哈"],
                    "pro_out",
                    "ming_out",
                    "background",
                    ["當天下午在教授家中"],
                    "pro_in",
                    ["教授：可惡啊！我一定要讓那個臭小子付出代價","教授：頭腦好又怎樣，我決定了，滿分我照當，當死你這小xx蛋"],
                    ["......"],
                    ["教授：唉！？奇怪......怎麼校務系統一直顯示錯誤......"],
                    ["此時，電腦畫面跳出一個奇怪視窗"],
                    ["教授：奇怪，這是甚麼？"],
                    ["畫面上出現了小明的臉"],
                    ["教授：X"],
                    "ming_in",
                    
                    ["小明：啊瞜哈，教授你好啊"],
                    ["教授：你怎麼會出現在這，你對我的電腦做了甚麼！？"],
                    ["小明：好心告訴你，這只是一個綠影，所以我是不可能回答你的問題的","小明：教授啊教授，我可是知道的喔，你一定很想當掉我對吧","小明：我怎麼可能會讓你這麼做呢，現在校務系統內針對我個人資料修改的存取\n都會被我給攔截呦","小明：目前只有校內主機有辦法做修改呢，所以教授你就乖乖等待學期過去\n讓我成功拿到學分吧"],
                    "ming_out",
                    ["教授：可惡啊，這口氣怎麼可能嚥得下去，看來只能前往校內主機去看看了"],
                    "pro_out",
                    ]
        
        for act in self.act_list:
            tem = self.wait_var.get()
            if tem == 1000:
                break
            if(act == "pro_in"):
                #self.pro.place(x=25,y=392,anchor='sw')
                pro =self.canvas .create_image(25,392, anchor='sw',image=self.imgfile_s_pro)           
                
            elif(act == "pro_out"):
                self.canvas.delete(pro)
            
            elif(act == "ming_in"):
                ming =self.canvas .create_image(884,392, anchor='sw',image=self.imgfile_s_ming)
            elif(act == "ming_out"):
                self.canvas.delete(ming)
            elif(act == "background"):
                self.bg2 = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img2) 
            else:
                for text in act:
                    #在點擊button之前都停住(button點擊後wait_var才會變)，由於有這個執行緒，這會導致tkinter雖然關掉了，console沒關掉，因此強制skip會檢查
                    self.text_var.set(text)
                    self.next_b.wait_variable(self.wait_var)
                    tem = self.wait_var.get()
                    if tem == 1000:
                        break
                    self.wait_var.set(tem + 1)

        self.frame.pack_forget()
    def story2(self):
        self.wait_var.set(0)
        #self.bg2 = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img2) 

        self.frame.pack()
        
        act_list = ["pro_in",
                    ["教授：呼噓，終於來到學校了，我記得學校伺服器機房應該在xx大樓的......"],
                    "car_in",
                    ["！！！"],
                    ["教授：X，這三小"],
                    ["突然，在遙控車上出現了螢幕"],
                    "car_out",
                    "ming_in",
                    ["螢幕上出現了小明的臉"],
                    ["小明：喔呵呵，教授你好啊，如果你看到這個一定表示你還沒放棄當掉我啊","小明：不過我也不是沒準備喔，既然無法阻止對學校主機的直接存取，\n我就只好採取物理手段了","小明：果然物理這門科目還是很有用的，我可是請了許多擅長物理攻擊的好手呢","小明：教授啊，最後給你一個忠告，在這邊放棄才是明智的選擇喔"],
                    "ming_out",
                    "car_in",
                    ["牙控汽車：攻擊！攻擊！"],
                    ["教授：嗚，看來只能硬著頭皮上了","教授：讓你們見識見識，物理什麼的，我懂得還真就不少呢"],
                    "car_out",
                    "pro_out"]
        for act in act_list:
            tem = self.wait_var.get()
            if tem == 1000:
                break
            if(act == "pro_in"):
                pro =self.canvas .create_image(25,392, anchor='sw',image=self.imgfile_s_pro)           
            elif(act == "pro_out"):
                self.canvas.delete(pro)
            elif(act == "ming_in"):
                ming =self.canvas .create_image(884,392, anchor='sw',image=self.imgfile_s_ming)
            elif(act == "ming_out"):
                self.canvas.delete(ming)
            elif(act == "car_in"):
                
                car =self.canvas .create_image(884,392, anchor='sw',image=self.imgfile_s_car)           
                
            elif(act == "car_out"):
                self.canvas.delete(car)
            else:
                for text in act:
                    self.text_var.set(text)
                    self.next_b.wait_variable(self.wait_var)
                    tem = self.wait_var.get()
                    if tem == 1000:
                        break
                    self.wait_var.set(tem + 1)
        self.frame.pack_forget()
    def story3(self):
        self.frame.pack()
       
        self.wait_var.set(0)
        act_list = ["pro_in",
                    ["教授：總算到這了，前面就是伺服器機房！！！"],
                    ["有一個身影擋住了教授的去路"],
                    ["教授:！！！"],
                    "ming_in",
                    ["小明：你好啊教授，真沒想到你可以到第五層來呢，不過就到這裡為止了，\n接下來由我絕頂天才的小明來做你的對手！"],
                    ["教授：蛤？"],
                    ["小明：沒事，玩個梗而已，反正接下來就由我親自來阻止你！！！"],
                    ["教授：好啊，那我也親自來好好教你甚麼叫做物理學！！！！！"],
                    "pro_out",
                    "ming_out",]
        for act in act_list:
            tem = self.wait_var.get()
            if tem == 1000:
                break
            if(act == "pro_in"):
                pro =self.canvas .create_image(25,392, anchor='sw',image=self.imgfile_s_pro)           
            elif(act == "pro_out"):
                self.canvas.delete(pro)
            elif(act == "ming_in"):
                ming =self.canvas .create_image(884,392, anchor='sw',image=self.imgfile_s_ming)
            elif(act == "ming_out"):
                self.canvas.delete(ming)
            else:
                for text in act:
                    self.text_var.set(text)
                    self.next_b.wait_variable(self.wait_var)
                    tem = self.wait_var.get()
                    if tem == 1000:
                        break
                    self.wait_var.set(tem + 1)
        self.frame.pack_forget()
    def story4(self):
        self.frame.pack()
        
        self.wait_var.set(0)
        act_list = ["pro_in",
                    "ming_in",
                    ["教授：哼哼，還算有兩把刷子，不過最終的勝利果然還是我的！！！"],
                    ["教授徑直走向機房"],
                    "pro_out",
                    ["小明：可...可惡......"],
                    "ming_out",
                    ["不久後......"],
                    "pro_in",
                    "ming_in",
                    ["教授：哈哈哈哈哈哈哈...痾...咳咳咳...咳恩","教授：總算被我給當掉了，這個問題學生"],
                    ["小明：亨，ㄏㄏㄏ"],
                    ["教授：你笑什麼？！"],
                    ["小明：教授啊教授，你忘了嗎，下學期這門課還是你開的啊！"],
                    ["教授：X"],
                    "pro_out",
                    "ming_out",]
        for act in act_list:
            tem = self.wait_var.get()
            if tem == 1000:
                break
            if(act == "pro_in"):
                pro =self.canvas .create_image(25,392, anchor='sw',image=self.imgfile_s_pro)           
            elif(act == "pro_out"):
                self.canvas.delete(pro)
            elif(act == "ming_in"):
                ming =self.canvas .create_image(884,392, anchor='sw',image=self.imgfile_s_ming)
            elif(act == "ming_out"):
                self.canvas.delete(ming)
            else:
                for text in act:
                    self.text_var.set(text)
                    self.next_b.wait_variable(self.wait_var)
                    tem = self.wait_var.get()
                    if tem == 1000:
                        break
                    self.wait_var.set(tem + 1)
        self.frame.pack_forget()
        self.master.destroy()
        self.master.quit()
        
                    
                
                
                
                
                
                
                
                
                
                