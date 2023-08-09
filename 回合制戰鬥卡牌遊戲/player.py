# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 21:49:11 2023

@author: user
"""
import tkinter as tk

class ability:
    
    def __init__ (self,hp,atk,maxhp,canvas,image_list):
        
        self.hp_var = tk.IntVar()
        self.hp = hp
        self.hp_var.set(self.hp)
        self.atk_var = tk.IntVar()
        self.atk = atk   
        self.atk_var.set(self.atk)
        self.max_hp = maxhp 
        self.frantic_var=tk.IntVar()
        self.frantic = 0 
        self.frantic_var.set(self.frantic)
        self.weak = 0
        self.weak_var = tk.IntVar()
        self.weak_var.set(self.weak)
        self.armor_var = tk.IntVar()
        self.armor = 0
        self.armor_var.set(self.armor)
        self.bleed = 0
        self.bleed_var = tk.IntVar()
        self.bleed_var.set(self.bleed)
        self.img = canvas.create_image(130, 340, anchor='sw',image=image_list[9])
        self.image_list = image_list
        self.atk_up=0
        self.heal=0
        self.canvas = canvas
        self.alive = True


        self.weak = 0
        
        self.weak_var = tk.IntVar()
        self.weak_var.set(self.weak)
        self.bleed_var.set(self.bleed)
    
    def summon_cha(self,x,y):
        image_list = self.image_list
        canvas = self.canvas
        self.max_hpL = tk.Label(self.canvas,text='/' + str(self.max_hp), font=('Arial',17))
        self.max_hpL.place(x=x,y=y-20)
        self.hpL = tk.Label(canvas, textvariable=self.hp_var, font=('Arial',17))
        self.hpL.place(x=x-30, y=y-20, anchor='n')
        self.weak_iconL = tk.Label(canvas, image=image_list[8])
        self.weak_iconL.place(x=x-50, y=y+52, anchor='center')
        self.weakL = tk.Label(canvas, textvariable=self.weak_var, font=('Arial',15))
        self.weakL.place(x=x-20, y=y+52, anchor='center')
        self.frantic_iconL = tk.Label(canvas, image=image_list[12])
        self.frantic_iconL.place(x=x-10, y=y+100, anchor='center')
        self.franticL = tk.Label(canvas, textvariable=self.frantic_var, font=('Arial',15))
        self.franticL.place(x=x+20, y=y+100, anchor='center')                
        self.bleed_iconL = tk.Label(canvas, image=image_list[7])
        self.bleed_iconL.place(x=x+20, y=y+52, anchor='center')
        self.bleedL = tk.Label(canvas, textvariable=self.bleed_var, font=('Arial',15))
        self.bleedL.place(x=x+50, y=y+52, anchor='center')
        self.atk_iconL = tk.Label(canvas, image=image_list[10])
        self.atk_iconL.place(x=x-320,y=y-200,anchor='nw')
        self.atkL = tk.Label(canvas, textvariable=self.atk_var, font=('Arial',15))
        self.atkL.place(x=x-260, y=y-200, anchor='nw')                
        self.armor_iconL = tk.Label(canvas, image=image_list[11])
        self.armor_iconL.place(x=x-160,y=y-200, anchor='nw')  
        self.armorL = tk.Label(canvas, textvariable=self.armor_var, font=('Arial',15))
        self.armorL.place(x=x-100, y=y-200, anchor='nw')                                                           
    def dmg_inflicted(self,damage):
       
        if self.armor>=damage:
            self.armor-=damage
        else:                    
            damage_after_armor= damage -self.armor
            self.armor=0
            self.hp -= damage_after_armor
        self.hp_var.set(self.hp)
        self.armor_var.set(self.armor)
        if self.hp<=0:
            self.alive = False 
    def weak_inflicted(self,lvl):
        self.weak += lvl
        self.weak_var.set(self.weak)
        
  
    def end_round(self):
        
        if(self.weak != 0):
            self.weak -= 1
            self.weak_var.set(self.weak)
            
        if(self.atk_up != 0):
            self.atk+=1
            self.atk_var.set(self.atk)
            
        if(self.heal != 0):
            self.hp +=3
            self.hp_var.set(self.hp)
            if self.hp>=self.max_hp:
                self.hp=self.max_hp
                self.hp_var.set(self.hp)
        if self.bleed!=0:
            
            if self.armor>5:
                self.armor -=5
                damage = 0
            else:
                self.armor = 0
                damage = 5-self.armor
            self.hp -= damage
            self.armor_var.set(self.armor)
            self.hp_var.set(self.hp)
            self.bleed -=1 
            self.bleed_var.set(self.bleed)
            if self.hp<=0:
                self.alive = False
            
        if(self.weak != 0):
            self.weak -= 1
            self.weak_var.set(self.weak)
            
        if(self.weak != 0):
            self.weak -= 1
            self.weak_var.set(self.weak)
            

