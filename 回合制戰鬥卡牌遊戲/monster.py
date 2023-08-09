# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 20:04:00 2023

@author: user
"""
import tkinter as tk
from threading import *
import random
import time
class a:
    def __init__(self):
        pass

class Plane:
    def __init__(self,level,canvas,player,inf1,inf2,damage,image_list,label):
        self.hp_var = tk.IntVar()
        self.hp = int(10 * (level*0.34 + 1))
        self.hp_var.set(self.hp)
        self.max_hp = self.hp
        self.atk = int(3 * (level*0.34 + 1))
        self.weak = 0
        self.bleed = 0
        self.weak_var = tk.IntVar()
        self.weak_var.set(self.weak)
        self.bleed_var = tk.IntVar()
        self.bleed_var.set(self.bleed)
        self.image_list = image_list
        #無須frantic
        #無須perseverance
        self.alive = True
        self.canvas = canvas
        self.inf1 = inf1
        self.inf2 = inf2
        self.player = player
        self.label = label
        
        self.thread = None
    
    def summon_cha(self,x,y):
        image_list = self.image_list
        canvas = self.canvas
        self.name = "牙控飛機"
        self.img = canvas.create_image(x, y-280, anchor='n',image=image_list[1])
        self.max_hpL = tk.Label(canvas,text='/' + str(self.max_hp), font=('Arial',17))
        self.max_hpL.place(x=x+10,y=y)
        self.hpL = tk.Label(canvas, textvariable=self.hp_var, font=('Arial',17))
        self.hpL.place(x=x-20, y=y, anchor='n')
        self.weak_iconL = tk.Label(canvas, image=image_list[8])
        self.weak_iconL.place(x=x-50, y=y+52, anchor='center')
        self.weakL = tk.Label(canvas, textvariable=self.weak_var, font=('Arial',15))
        self.weakL.place(x=x-20, y=y+52, anchor='center')
        self.bleed_iconL = tk.Label(canvas, image=image_list[7])
        self.bleed_iconL.place(x=x+20, y=y+52, anchor='center')
        self.bleedL = tk.Label(canvas, textvariable=self.bleed_var, font=('Arial',15))
        self.bleedL.place(x=x+50, y=y+52, anchor='center')
    def cha_delete(self):
        canvas = self.canvas
        canvas.delete(self.img)
        self.label.place_forget()
        self.max_hpL.destroy()
        self.hpL.destroy()
        self.weakL.destroy()
        self.weak_iconL.destroy()
        self.bleedL.destroy()
        self.bleed_iconL.destroy()
        inf = self.name+" 壞了"
        self.inf2.set(inf)
    def dmg_inflicted(self,damage,enemy_number):
        self.hp -= int(damage * (1 + 0.5*bool(self.weak)))
        self.hp_var.set(self.hp)
        if(self.hp <= 0):
            
            self.alive = False
            self.cha_delete()
            return enemy_number-1
        return enemy_number
    def weak_inflicted(self,lvl):
        self.weak += lvl
        self.weak_var.set(self.weak)
    def bleed_inflicted(self,lvl):
        self.bleed += lvl
        self.bleed_var.set(self.bleed)
    def skill(self,event_before=None,event_after=None): #傳入1~12任一數
        if event_before!=None:
            event_before.wait()
            
        if self.alive:
            random_var = random.randint(1,12)
            if(random_var%2 == 0): #attack
                dmg = int(self.atk * (1 + 0.5*bool(self.player.weak)))
                self.player.dmg_inflicted(dmg)
                inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
                self.inf1.set(inf)
                self.inf2.set("")
            elif(random_var%2 ==1): #inflict weak
                self.player.weak += 1
                self.player.weak_var.set(self.player.weak)
                inf = "被 " + self.name + " 附加了 1 層虛弱"
                self.inf1.set(inf)
                self.inf2.set("")
            self.end_round()
            time.sleep(1)
        
            
        event_after.set()
    def end_round(self):
        if(self.weak != 0):
            self.weak -= 1
            self.weak_var.set(self.weak)
        if(self.bleed != 0):
            self.bleed -= 1
            self.bleed_var.set(self.bleed)
            self.hp -= 5
            self.hp_var.set(self.hp)
            if(self.hp <= 0):
                self.alive = False
                self.cha_delete()
                return False
        return True

class Car:
    def __init__(self,level,canvas,player,inf1,inf2,damage,image_list,label):
        self.hp_var = tk.IntVar()
        self.hp = int(10 * (level*0.34 + 1))
        self.hp_var.set(self.hp)
        self.max_hp = self.hp
        self.atk = int(5 * (level*0.34 + 1))
        self.weak = 0
        self.bleed = 0
        self.weak_var = tk.IntVar()
        self.weak_var.set(self.weak)
        self.bleed_var = tk.IntVar()
        self.bleed_var.set(self.bleed)
        #無須frantic
        #無須perseverance
        self.thread = None
        self.alive = True
        self.label = label
        self.canvas = canvas
        self.inf1 = inf1
        self.inf2 = inf2
        self.player = player
        self.image_list = image_list
    def summon_cha(self,x,y,n):
        canvas = self.canvas
        image_list = self.image_list
        self.name = "牙控汽車" + n
        self.code = n
        self.img = canvas.create_image(x, y-180, anchor='n',image=image_list[0])
        self.max_hpL = tk.Label(canvas,text='/' + str(self.max_hp), font=('Arial',17))
        self.max_hpL.place(x=x+10,y=y)
        self.hpL = tk.Label(canvas, textvariable=self.hp_var, font=('Arial',17))
        self.hpL.place(x=x-20, y=y, anchor='n')
        self.weak_iconL = tk.Label(canvas, image=image_list[8])
        self.weak_iconL.place(x=x-50, y=y+52, anchor='center')
        self.weakL = tk.Label(canvas, textvariable=self.weak_var, font=('Arial',15))
        self.weakL.place(x=x-20, y=y+52, anchor='center')
        self.bleed_iconL = tk.Label(canvas, image=image_list[7])
        self.bleed_iconL.place(x=x+20, y=y+52, anchor='center')
        self.bleedL = tk.Label(canvas, textvariable=self.bleed_var, font=('Arial',15))
        self.bleedL.place(x=x+50, y=y+52, anchor='center')
    def cha_delete(self):
        canvas = self.canvas
        canvas.delete(self.img)
        print(33333)
        if(self.code == 'A'):
            self.label.place_forget()
        if(self.code == 'C'):
            self.label.place_forget()
        self.max_hpL.destroy()
        self.hpL.destroy()
        self.weakL.destroy()
        self.weak_iconL.destroy()
        self.bleedL.destroy()
        self.bleed_iconL.destroy()
        self.inf = self.name+" 壞了"
        self.inf2.set(self.inf)
      
    def dmg_inflicted(self,damage,enemy_number):
        
        self.hp -= int(damage * (1 + 0.5*bool(self.weak)))
        self.hp_var.set(self.hp)
        if(self.hp <= 0):
            self.alive = False
            self.cha_delete()
            return enemy_number-1
        return enemy_number
    def weak_inflicted(self,lvl):
        self.weak += lvl
        self.weak_var.set(self.weak)
    def bleed_inflicted(self,lvl):
        self.bleed += lvl
        self.bleed_var.set(self.bleed)
    def skill(self,event_before=None,event_after=None): #傳入1~12任一數
        if event_before!=None:
            event_before.wait()
        if self.alive:
            dmg = int(self.atk * (1 + 0.5*bool(self.player.weak)))
            self.player.dmg_inflicted(dmg)
            inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
            self.inf1.set(inf)
            self.inf2.set("")
            self.end_round()
            time.sleep(1)
        
        event_after.set()
    def end_round(self):
        if(self.weak != 0):
            self.weak -= 1
            self.weak_var.set(self.weak)
        if(self.bleed != 0):
            self.bleed -= 1
            self.bleed_var.set(self.bleed)
            self.hp -= 5
            self.hp_var.set(self.hp)
            if(self.hp <= 0):
                self.alive = False
                self.cha_delete()
                return False
        return True
                #enemy_number-=1
            
class Eight_Plus_Nine:
    def __init__(self,level,canvas,player,inf1,inf2,damage,image_list,label):
        self.hp_var = tk.IntVar()
        self.hp = int(20 * (level*0.34 + 1))
        self.hp_var.set(self.hp)
        self.max_hp = self.hp
        self.atk = int(3 * (level*0.34 + 1))
        self.weak = 0
        self.bleed = 0
        self.weak_var = tk.IntVar()
        self.weak_var.set(self.weak)
        self.bleed_var = tk.IntVar()
        self.bleed_var.set(self.bleed)
        #無須frantic
        #無須perseverance
        self.alive = True
        self.power = False
        self.label = label
        self.canvas = canvas
        self.inf1 = inf1
        self.inf2 = inf2
        self.player = player
        self.image_list = image_list 
        self.thread = None
    def summon_cha(self,x,y,n):
        image_list = self.image_list
        self.name = "8+9" + n
        self.code = n
        self.img = self.canvas.create_image(x, y-300, anchor='n',image=image_list[2])
        self.max_hpL = tk.Label(self.canvas,text='/' + str(self.max_hp), font=('Arial',17))
        self.max_hpL.place(x=x+10,y=y)
        self.hpL = tk.Label(self.canvas, textvariable=self.hp_var, font=('Arial',17))
        self.hpL.place(x=x-20, y=y, anchor='n')
        self.weak_iconL = tk.Label(self.canvas, image=image_list[8])
        self.weak_iconL.place(x=x-50, y=y+52, anchor='center')
        self.weakL = tk.Label(self.canvas, textvariable=self.weak_var, font=('Arial',15))
        self.weakL.place(x=x-20, y=y+52, anchor='center')
        self.bleed_iconL = tk.Label(self.canvas, image=image_list[7])
        self.bleed_iconL.place(x=x+20, y=y+52, anchor='center')
        self.bleedL = tk.Label(self.canvas, textvariable=self.bleed_var, font=('Arial',15))
        self.bleedL.place(x=x+50, y=y+52, anchor='center')
    def cha_delete(self):
        self.canvas.delete(self.img)
       
        if(self.code == 'A'):
            self.label.place_forget()
        if(self.code == 'B'):
            self.label.place_forget()
        self.max_hpL.destroy()
        self.hpL.destroy()
        self.weakL.destroy()
        self.weak_iconL.destroy()
        self.bleedL.destroy()
        self.bleed_iconL.destroy()
        inf = self.name+" 再起不能"
        self.inf2.set(inf)
        
    def dmg_inflicted(self,damage,enemy_number):
        self.hp -= int(damage * (1 + 0.5*bool(self.weak)))
        self.hp_var.set(self.hp)
        if(self.hp <= 0):
            self.alive = False
            self.cha_delete()
            return enemy_number-1
        return enemy_number
    def weak_inflicted(self,lvl):
        self.weak += lvl
        self.weak_var.set(self.weak)
    def bleed_inflicted(self,lvl):
        self.bleed += lvl
        self.bleed_var.set(self.bleed)
    def skill(self,event_before=None,event_after=None): #傳入1~12任一數
        if event_before!=None:
            event_before.wait()
        if self.alive:
            random_var = random.randint(1,12)
            if self.power:
                self.power = False
                self.hpL['fg'] = 'black'
                self.max_hpL['fg'] = 'black'
                dmg = int(self.atk * 2 * (1 + 0.5*bool(self.player.weak)))
                self.player.dmg_inflicted(dmg)
                self.player.bleed += 1
                self.player.bleed_var.set(self.player.bleed)
                inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
                self.inf1.set(inf)
                self.inf2.set("被附加了 1 層流血")
            elif(random_var%3 == 0): #attack
                dmg = int(self.atk * (1 + 0.5*bool(self.player.weak)))
                self.player.dmg_inflicted(dmg)
                inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
                self.inf1.set(inf)
                self.inf2.set("")
            elif(random_var%3 == 1): #atk up
                self.atk += 3
                inf = self.name + " 攻擊力上升了3點"
                self.inf1.set(inf)
                self.inf2.set("")
            elif(random_var%3 == 2): #powerful attack
                self.power = True
                self.hpL['fg'] = 'red'
                self.max_hpL['fg'] = 'red'
                inf = self.name + " 準備在下回合使出強力攻擊"
                self.inf1.set(inf)
                self.inf2.set("") 
            self.end_round()
            time.sleep(1)
        event_after.set()
    def end_round(self):
        if(self.weak != 0):
            self.weak -= 1
            self.weak_var.set(self.weak)
        if(self.bleed != 0):
            self.bleed -= 1
            self.bleed_var.set(self.bleed)
            self.hp -= 5
            self.hp_var.set(self.hp)
            if(self.hp <= 0):
                self.alive = False
                self.cha_delete()
                return False
        return True
class Robot:
    def __init__(self,level,canvas,player,inf1,inf2,damage,image_list,label):
        self.hp_var = tk.IntVar()
        self.hp = int(35 * (level*0.34 + 1))
        self.hp_var.set(self.hp)
        self.max_hp = self.hp
        self.atk = int(7 * (level*0.34 + 1))
        self.weak = 0
        self.bleed = 0
        self.weak_var = tk.IntVar()
        self.weak_var.set(self.weak)
        self.bleed_var = tk.IntVar()
        self.bleed_var.set(self.bleed)
        #無須frantic
        self.perseverance = 0
        self.perseverance_var = tk.IntVar()
        self.perseverance_var.set(self.perseverance)
        self.alive = True
        self.power = False
        
        self.label = label
        self.canvas = canvas
        self.inf1 = inf1
        self.inf2 = inf2
        self.player = player
        self.image_list = image_list
        self.thread = None
    def summon_cha(self,x,y,n):
        image_list = self.image_list
        canvas = self.canvas
        self.name = "超殺機器人" + n
        self.code = n
        self.img = canvas.create_image(x, y-300, anchor='n',image=image_list[3])
        self.max_hpL = tk.Label(canvas,text='/' + str(self.max_hp), font=('Arial',17))
        self.max_hpL.place(x=x+10,y=y)
        self.hpL = tk.Label(canvas, textvariable=self.hp_var, font=('Arial',17))
        self.hpL.place(x=x-20, y=y, anchor='n')
        self.weak_iconL = tk.Label(canvas, image=image_list[8])
        self.weak_iconL.place(x=x-50, y=y+52, anchor='center')
        self.weakL = tk.Label(canvas, textvariable=self.weak_var, font=('Arial',15))
        self.weakL.place(x=x-20, y=y+52, anchor='center')
        self.bleed_iconL = tk.Label(canvas, image=image_list[7])
        self.bleed_iconL.place(x=x+20, y=y+52, anchor='center')
        self.bleedL = tk.Label(canvas, textvariable=self.bleed_var, font=('Arial',15))
        self.bleedL.place(x=x+50, y=y+52, anchor='center')
    def cha_delete(self):
        canvas = self.canvas
        canvas.delete(self.img)
        if(self.code == 'A'):
            self.label.place_forget()
        if(self.code == 'B'):
            self.label.place_forget()
        self.max_hpL.destroy()
        self.hpL.destroy()
        self.weakL.destroy()
        self.weak_iconL.destroy()
        self.bleedL.destroy()
        self.bleed_iconL.destroy()
        inf = self.name+" 再起不能"
        self.inf2.set(inf)
       
    def dmg_inflicted(self,damage,enemy_number):
        self.hp -= int(damage * (1 + 0.5*bool(self.weak)) * (1 - 0.4*bool(self.perseverance)))
        self.hp_var.set(self.hp)
        if(self.hp <= 0):
            self.alive = False
            self.cha_delete()
            return enemy_number-1
        return enemy_number
    def weak_inflicted(self,lvl):
        self.weak += lvl
        self.weak_var.set(self.weak)
    def bleed_inflicted(self,lvl):
        self.bleed += lvl
        self.bleed_var.set(self.bleed)
    def skill(self,event_before=None,event_after=None): #傳入1~12任一數
        if event_before!=None:
            event_before.wait()
        if self.alive:
            random_var = random.randint(1,12)
            if self.power:
                self.power = False
                self.hpL['fg'] = 'black'
                self.max_hpL['fg'] = 'black'
                dmg = int(self.atk * 2 * (1 + 0.5*bool(self.player.weak)))
                self.player.dmg_inflicted(dmg)
                self.player.bleed += 2
                self.player.bleed_var.set(self.player.bleed)
                inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
                self.inf1.set(inf)
                self.inf2.set("被附加了 2 層流血")
            elif(random_var%4 == 0): #attack
                dmg = int(self.atk * (1 + 0.5*bool(self.player.weak)))
                self.player.dmg_inflicted(dmg)
                inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
                self.inf1.set(inf)
                self.inf2.set("")
            elif(random_var%4 == 1): #heal
                self.hp += 15
                if (self.hp > self.max_hp):
                    self.hp = self.max_hp
                    self.hp_var.set(self.hp)
                    inf = self.name + " 回復了自身血量"
                    self.inf1.set(inf)
                    self.inf2.set("")
            elif(random_var%4 == 2): #powerful attack
                self.power = True
                self.hpL['fg'] = 'red'
                self.max_hpL['fg'] = 'red'
                inf = self.name + " 準備在下回合使出強力攻擊"
                self.inf1.set(inf)
                self.inf2.set("")
            elif(random_var%4 == 3): #buff&debuff
                self.perseverance += 2
                self.perseverance_var.set(self.perseverance)
                self.player.weak += 2
                self.player.weak_var.set(self.player.weak)
                inf = self.name + " 對自身附加了 2 層堅毅"
                self.inf1.set(inf)
                self.inf2.set("被附加了 2 層虛弱")
            self.end_round()
            time.sleep(1)
        event_after.set()
    def end_round(self):
        if(self.weak != 0):
            self.weak -= 1
            self.weak_var.set(self.weak)
        if(self.bleed != 0):
            self.bleed -= 1
            self.bleed_var.set(self.bleed)
            self.hp -= 5
            self.hp_var.set(self.hp)
            if(self.hp <= 0):
                self.alive = False
                self.cha_delete()
                return False

                #enemy_number-=1
        if(self.perseverance != 0):
            self.perseverance -= 1
            self.perseverance_var.set(self.perseverance) 
        return True
class Boss_Ming:
    def __init__(self,level,canvas,player,inf1,inf2,damage,image_list,label):
        self.hp_var = tk.IntVar()
        self.hp = 80
        self.hp_var.set(self.hp)
        self.max_hp = self.hp
        self.max_hp_sec = 120
        self.atk = 10
        self.weak = 0
        self.bleed = 0
        self.weak_var = tk.IntVar()
        self.weak_var.set(self.weak)
        self.bleed_var = tk.IntVar()
        self.bleed_var.set(self.bleed)
        #無須frantic
        self.perseverance = 0
        self.perseverance_var = tk.IntVar()
        self.perseverance_var.set(self.perseverance)
        self.alive = True
        self.power = False
        self.transform = False
        
        self.label = label
        self.canvas = canvas
        self.inf1 = inf1
        self.inf2 = inf2
        self.player = player
        self.image_list = image_list
        self.thread = None
    def summon_cha(self,x,y):
        image_list = self.image_list
        canvas = self.canvas
        self.name = "Boss"
        self.img = canvas.create_image(x, y-300, anchor='n',image=image_list[4])
        self.max_hpL = tk.Label(canvas,text='/' + str(self.max_hp), font=('Arial',17))
        self.max_hpL.place(x=x+10,y=y)
        self.hpL = tk.Label(canvas, textvariable=self.hp_var, font=('Arial',17))
        self.hpL.place(x=x-20, y=y, anchor='n')
        self.weak_iconL = tk.Label(canvas, image=image_list[8])
        self.weak_iconL.place(x=x-80, y=y+52, anchor='center')
        self.weakL = tk.Label(canvas, textvariable=self.weak_var, font=('Arial',15))
        self.weakL.place(x=x-50, y=y+52, anchor='center')
        self.bleed_iconL = tk.Label(canvas, image=image_list[7])
        self.bleed_iconL.place(x=x-10, y=y+52, anchor='center')
        self.bleedL = tk.Label(canvas, textvariable=self.bleed_var, font=('Arial',15))
        self.bleedL.place(x=x+20, y=y+52, anchor='center')
        self.perseverance_iconL = tk.Label(canvas, image=image_list[6])
        self.perseverance_iconL.place(x=x+60, y=y+52, anchor='center')
        self.perseveranceL = tk.Label(canvas, textvariable=self.perseverance_var, font=('Arial',15))
        self.perseveranceL.place(x=x+90, y=y+52, anchor='center')
    def summon_cha_sec(self,x,y):
        image_list = self.image_list
        canvas = self.canvas
        canvas.delete(self.img)
        self.img = canvas.create_image(x, y-300, anchor='n',image=image_list[5])
        self.max_hpL['text'] = '/120'
        self.hp_var.set(self.hp)
    def cha_delete(self):
        canvas = self.canvas
        canvas.delete(self.img)
        self.label.place_forget()
        self.max_hpL.destroy()
        self.hpL.destroy()
        self.weakL.destroy()
        self.weak_iconL.destroy()
        self.bleedL.destroy()
        self.bleed_iconL.destroy()
        inf = self.name+" 敗北了"
        self.inf2.set(inf)
        
    def dmg_inflicted(self,damage,enemy_number):
      
        self.hp -= int(damage * (1 + 0.5*bool(self.weak)) * (1 - 0.4*bool(self.perseverance)))
        self.hp_var.set(self.hp)
        if(self.hp <= 0 and self.transform == True):
            self.alive = False
            self.cha_delete()
            return enemy_number-1
        
        elif(self.hp <= 0):
            self.transform = True
            inf = "小明進入第二階段"
            self.inf1.set(inf)
            inf = "能力大幅提升了"
            self.inf2.set(inf)
            self.hp = 120
            self.weak = 0
            self.bleed = 0
            self.perseverance = 0
            self.summon_cha_sec(950, 350)
        return enemy_number        
    def weak_inflicted(self,lvl):
        self.weak += lvl
        self.weak_var.set(self.weak)
    def bleed_inflicted(self,lvl):
        self.bleed += lvl
        self.bleed_var.set(self.bleed)
    def skill(self,event_before=None,event_after=None): #傳入1~12任一數
        if event_before!=None:
            event_before.wait()
        if self.alive:
            random_var = random.randint(1,12)
            if(self.transform == False): #第一階段技能組
                if(random_var%3 == 0): #attack
                    dmg = int(self.atk * (1 + 0.5*bool(self.player.weak)))
                    self.player.dmg_inflicted(dmg)
                    inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
                    self.inf1.set(inf)
                    self.inf2.set("")
                elif(random_var%3 == 1): #inflict debuff
                    self.player.weak += 2
                    self.player.weak_var.set(self.player.weak)
                    inf = "被 " + self.name + " 附加了 2 層虛弱"
                    self.inf1.set(inf)
                    self.inf2.set("")
                elif(random_var%3 == 2): #atk up
                    self.atk += 3
                    inf = self.name + " 攻擊力上升了3點"
                    self.inf1.set(inf)
                    self.inf2.set("")
                    
            else: #第二階段技能組
                if self.power:
                    self.power = False
                    self.hpL['fg'] = 'black'
                    self.max_hpL['fg'] = 'black'
                    dmg = int(self.atk * 2.5 * (1 + 0.5*bool(self.player.weak)))
                    self.player.dmg_inflicted(dmg)
                    inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
                    self.inf1.set(inf)
                    self.inf2.set("")
                elif(random_var%5 == 1): #attack
                    dmg = int(self.atk * (1 + 0.5*bool(self.player.weak)))
                    self.player.dmg_inflicted(dmg)
                    inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
                    self.inf1.set(inf)
                    self.inf2.set("")
                elif(random_var%5 == 0): #heal
                    self.hp += 30
                    if (self.hp > self.max_hp):
                        self.hp = self.max_hp
                        self.hp_var.set(self.hp)
                        inf = self.name + " 回復了自身血量"
                        self.inf1.set(inf)
                        self.inf2.set("")
                elif(random_var%5 == 3): #powerful attack
                    self.power = True
                    self.hpL['fg'] = 'red'
                    self.max_hpL['fg'] = 'red'
                    inf = self.name + " 準備在下回合使出強力攻擊"
                    self.inf1.set(inf)
                    self.inf2.set("")
                elif(random_var%5 == 2): #buff&debuff
                    self.perseverance += 2
                    self.perseverance_var.set(self.perseverance)
                    self.player.weak += 2
                    self.player.weak_var.set(self.player.weak)
                    inf = self.name + " 對自身附加了 2 層堅毅"
                    self.inf1.set(inf)
                    self.inf2.set("被附加了 2 層虛弱")
                elif(random_var%5 == 4): #bleeding atk
                    dmg = int(self.atk * (1 + 0.5*bool(self.player.weak)))
                    self.player.dmg_inflicted(dmg)
                    self.player.bleed += 2
                    self.player.bleed_var.set(self.player.bleed)
                    inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
                    self.inf1.set(inf)
                    self.inf2.set("被附加了 2 層流血")
            self.end_round()
            time.sleep(1)
        event_after.set()
    def end_round(self):
        if(self.weak != 0):
            self.weak -= 1
            self.weak_var.set(self.weak)
        if(self.bleed != 0):
            self.bleed -= 1
            self.bleed_var.set(self.bleed)
            self.hp -= 5
            self.hp_var.set(self.hp)
            if(self.hp <= 0 and self.transform == True):
                self.alive = False
                self.cha_delete()
                return False
            elif(self.hp <= 0):
                self.transform = True
                inf = "小明進入第二階段"
                self.inf1.set(inf)
                inf = "能力大幅提升了"
                self.inf2.set(inf)
                self.hp = 120
                self.weak = 0
                self.bleed = 0
                self.perseverance = 0
                self.summon_cha_sec(950, 350)
        if(self.perseverance != 0):
            self.perseverance -= 1
            self.perseverance_var.set(self.perseverance)

        return True
        