# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 20:52:46 2023

@author: user
"""

 class ability:
     
     def __init__ (self,hp,atk,maxhp):
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
         self.img = canvas.create_image(130, 340, anchor='sw',image=image_file10)    
         self.atk_up=0
         self.heal=0
         
 
 
 
         self.weak = 0
         
         self.weak_var = tk.IntVar()
         self.weak_var.set(self.weak)
 
         self.bleed_var.set(self.bleed)
     def summon_cha(self,x,y):
         
         
         self.max_hpL = tk.Label(canvas,text='/' + str(self.max_hp), font=('Arial',17))
         self.max_hpL.place(x=x,y=y-20)
         self.hpL = tk.Label(canvas, textvariable=self.hp_var, font=('Arial',17))
         self.hpL.place(x=x-30, y=y-20, anchor='n')
         self.weak_iconL = tk.Label(canvas, image=image_file9)
         self.weak_iconL.place(x=x-50, y=y+52, anchor='center')
         self.weakL = tk.Label(canvas, textvariable=self.weak_var, font=('Arial',15))
         self.weakL.place(x=x-20, y=y+52, anchor='center')
         self.frantic_iconL = tk.Label(canvas, image=image_file13)
         self.frantic_iconL.place(x=x-10, y=y+100, anchor='center')
         self.franticL = tk.Label(canvas, textvariable=self.frantic_var, font=('Arial',15))
         self.franticL.place(x=x+20, y=y+100, anchor='center')                
         self.bleed_iconL = tk.Label(canvas, image=image_file8)
         self.bleed_iconL.place(x=x+20, y=y+52, anchor='center')
         self.bleedL = tk.Label(canvas, textvariable=self.bleed_var, font=('Arial',15))
         self.bleedL.place(x=x+50, y=y+52, anchor='center')
         self.atk_iconL = tk.Label(canvas, image=image_file11)
         self.atk_iconL.place(x=x-320,y=y-200,anchor='nw')
         self.atkL = tk.Label(canvas, textvariable=self.atk_var, font=('Arial',15))
         self.atkL.place(x=x-260, y=y-200, anchor='nw')                
         self.armor_iconL = tk.Label(canvas, image=image_file12)
         self.armor_iconL.place(x=x-160,y=y-200, anchor='nw')  
         self.armorL = tk.Label(canvas, textvariable=self.armor_var, font=('Arial',15))
         self.armorL.place(x=x-100, y=y-200, anchor='nw')                                                           
     def dmg_inflicted(self):
         
         if self.armor>=damage:
             self.armor-=int(damage * (1 + 0.5*bool(self.weak)))
         else:                    
             damage_after_armor=int(damage * (1 + 0.5*bool(self.weak)))-self.armor
             self.armor=0
             
             self.hp -= damage_after_armor
         self.hp_var.set(self.hp)
         self.armor_var.set(self.armor)
             
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
             
         if(self.weak != 0):
             self.weak -= 1
             self.weak_var.set(self.weak)
             
         if(self.weak != 0):
             self.weak -= 1
             self.weak_var.set(self.weak)
 
 
 
 self.player = ability(21,5,25)


 level= 0
 
 class Plane:
     def __init__(self):
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
         #無須frantic
         #無須perseverance
         self.alive = True
     def summon_cha(self,x,y):
         self.name = "牙控飛機"
         self.img = canvas.create_image(x, y-280, anchor='n',image=image_file2)
         self.max_hpL = tk.Label(canvas,text='/' + str(self.max_hp), font=('Arial',17))
         self.max_hpL.place(x=x+10,y=y)
         self.hpL = tk.Label(canvas, textvariable=self.hp_var, font=('Arial',17))
         self.hpL.place(x=x-20, y=y, anchor='n')
         self.weak_iconL = tk.Label(canvas, image=image_file9)
         self.weak_iconL.place(x=x-50, y=y+52, anchor='center')
         self.weakL = tk.Label(canvas, textvariable=self.weak_var, font=('Arial',15))
         self.weakL.place(x=x-20, y=y+52, anchor='center')
         self.bleed_iconL = tk.Label(canvas, image=image_file8)
         self.bleed_iconL.place(x=x+20, y=y+52, anchor='center')
         self.bleedL = tk.Label(canvas, textvariable=self.bleed_var, font=('Arial',15))
         self.bleedL.place(x=x+50, y=y+52, anchor='center')
     def cha_delete(self):
         canvas.delete(self.img)
         r2.place_forget()
         self.max_hpL.destroy()
         self.hpL.destroy()
         self.weakL.destroy()
         self.weak_iconL.destroy()
         self.bleedL.destroy()
         self.bleed_iconL.destroy()
         inf = target.name+" 壞了"
         inf2.set(inf)
         global target_undef
         target_undef = True
     def dmg_inflicted(self):
         self.hp -= int(damage * (1 + 0.5*bool(self.weak)))
         self.hp_var.set(self.hp)
         if(self.hp <= 0):
             global enemy_number
             self.alive = False
             self.cha_delete()
             enemy_number-=1
     def weak_inflicted(self,lvl):
         self.weak += lvl
         self.weak_var.set(self.weak)
     def bleed_inflicted(self,lvl):
         self.bleed += lvl
         self.bleed_var.set(self.bleed)
     def skill(self,random): #傳入1~12任一數
         if(random%2 == 0): #attack
             dmg = int(self.atk * (1 + 0.5*bool(Mode_Battle.player.weak)))
             Mode_Battle.player.dmg_inflicted(dmg)
             inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
             inf1.set(inf)
             inf2.set("")
         elif(random%2 ==1): #inflict weak
             Mode_Battle.player.weak += 1
             Mode_Battle.player.weak_var.set(Mode_Battle.player.weak)
             inf = "被 " + self.name + " 附加了 1 層虛弱"
             inf1.set(inf)
             inf2.set("")           
     def end_round(self):
         if(self.weak != 0):
             self.weak -= 1
             self.weak_var.set(self.weak)
         if(self.bleed != 0):
             self.bleed -= 1
             self.bleed_var.set(self.bleed)
             self.hp -= 5
             if(self.hp <= 0):
                 self.alive = False
                 self.cha_delete()

 class Car:
     def __init__(self):
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
         self.alive = True
     def summon_cha(self,x,y,n):
         self.name = "牙控汽車" + n
         self.code = n
         self.img = canvas.create_image(x, y-180, anchor='n',image=image_file1)
         self.max_hpL = tk.Label(canvas,text='/' + str(self.max_hp), font=('Arial',17))
         self.max_hpL.place(x=x+10,y=y)
         self.hpL = tk.Label(canvas, textvariable=self.hp_var, font=('Arial',17))
         self.hpL.place(x=x-20, y=y, anchor='n')
         self.weak_iconL = tk.Label(canvas, image=image_file9)
         self.weak_iconL.place(x=x-50, y=y+52, anchor='center')
         self.weakL = tk.Label(canvas, textvariable=self.weak_var, font=('Arial',15))
         self.weakL.place(x=x-20, y=y+52, anchor='center')
         self.bleed_iconL = tk.Label(canvas, image=image_file8)
         self.bleed_iconL.place(x=x+20, y=y+52, anchor='center')
         self.bleedL = tk.Label(canvas, textvariable=self.bleed_var, font=('Arial',15))
         self.bleedL.place(x=x+50, y=y+52, anchor='center')
     def cha_delete(self):
         canvas.delete(self.img)
         if(self.code == 'A'):
             r1.place_forget()
         if(self.code == 'C'):
             r3.place_forget()
         self.max_hpL.destroy()
         self.hpL.destroy()
         self.weakL.destroy()
         self.weak_iconL.destroy()
         self.bleedL.destroy()
         self.bleed_iconL.destroy()
         inf = target.name+" 壞了"
         inf2.set(inf)
         global target_undef
         target_undef = True
     def dmg_inflicted(self):
         self.hp -= int(damage * (1 + 0.5*bool(self.weak)))
         self.hp_var.set(self.hp)
         if(self.hp <= 0):
             self.alive = False
             self.cha_delete()
             global enemy_number
             enemy_number-=1
     def weak_inflicted(self,lvl):
         self.weak += lvl
         self.weak_var.set(self.weak)
     def bleed_inflicted(self,lvl):
         self.bleed += lvl
         self.bleed_var.set(self.bleed)
     def skill(self,random): #傳入1~12任一數
         dmg = int(self.atk * (1 + 0.5*bool(Mode_Battle.player.weak)))
         Mode_Battle.player.dmg_inflicted(dmg)
         inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
         inf1.set(inf)
         inf2.set("")
     def end_round(self):
         if(self.weak != 0):
             self.weak -= 1
             self.weak_var.set(self.weak)
         if(self.bleed != 0):
             self.bleed -= 1
             self.bleed_var.set(self.bleed)
             self.hp -= 5
             if(self.hp <= 0):
                 self.alive = False
                 self.cha_delete()
                 global enemy_number
                 enemy_number-=1
             
 class Eight_Plus_Nine:
     def __init__(self):
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
     def summon_cha(self,x,y,n):
         self.name = "8+9" + n
         self.code = n
         self.img = self.canvas.create_image(x, y-300, anchor='n',image=image_file3)
         self.max_hpL = tk.Label(self.canvas,text='/' + str(self.max_hp), font=('Arial',17))
         self.max_hpL.place(x=x+10,y=y)
         self.hpL = tk.Label(self.canvas, textvariable=self.hp_var, font=('Arial',17))
         self.hpL.place(x=x-20, y=y, anchor='n')
         self.weak_iconL = tk.Label(self.canvas, image=image_file9)
         self.weak_iconL.place(x=x-50, y=y+52, anchor='center')
         self.weakL = tk.Label(self.canvas, textvariable=self.weak_var, font=('Arial',15))
         self.weakL.place(x=x-20, y=y+52, anchor='center')
         self.bleed_iconL = tk.Label(self.canvas, image=image_file8)
         self.bleed_iconL.place(x=x+20, y=y+52, anchor='center')
         self.bleedL = tk.Label(self.canvas, textvariable=self.bleed_var, font=('Arial',15))
         self.bleedL.place(x=x+50, y=y+52, anchor='center')
     def cha_delete(self):
         self.canvas.delete(self.img)
         if(self.code == 'A'):
             r1.place_forget()
         if(self.code == 'B'):
             r2.place_forget()
         self.max_hpL.destroy()
         self.hpL.destroy()
         self.weakL.destroy()
         self.weak_iconL.destroy()
         self.bleedL.destroy()
         self.bleed_iconL.destroy()
         inf = target.name+" 再起不能"
         inf2.set(inf)
         global target_undef
         target_undef = True
     def dmg_inflicted(self):
         self.hp -= int(damage * (1 + 0.5*bool(self.weak)))
         self.hp_var.set(self.hp)
         if(self.hp <= 0):
             self.alive = False
             self.cha_delete()
             global enemy_number
             enemy_number-=1
     def weak_inflicted(self,lvl):
         self.weak += lvl
         self.weak_var.set(self.weak)
     def bleed_inflicted(self,lvl):
         self.bleed += lvl
         self.bleed_var.set(self.bleed)
     def skill(self,random): #傳入1~12任一數
         if self.power:
             self.power = False
             self.hpL['fg'] = 'black'
             self.max_hpL['fg'] = 'black'
             dmg = int(self.atk * 2 * (1 + 0.5*bool(Mode_Battle.player.weak)))
             Mode_Battle.player.dmg_inflicted(dmg)
             Mode_Battle.player.bleed += 1
             Mode_Battle.player.bleed_var.set(Mode_Battle.player.bleed)
             inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
             inf1.set(inf)
             inf2.set("被附加了 1 層流血")
         elif(random%3 == 0): #attack
             dmg = int(self.atk * (1 + 0.5*bool(Mode_Battle.player.weak)))
             Mode_Battle.player.dmg_inflicted(dmg)
             inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
             inf1.set(inf)
             inf2.set("")
         elif(random%3 == 1): #atk up
             self.atk += 3
             inf = self.name + " 攻擊力上升了3點"
             inf1.set(inf)
             inf2.set("")
         elif(random%3 == 2): #powerful attack
             self.power = True
             self.hpL['fg'] = 'red'
             self.max_hpL['fg'] = 'red'
             inf = self.name + " 準備在下回合使出強力攻擊"
             inf1.set(inf)
             inf2.set("") 
     def end_round(self):
         if(self.weak != 0):
             self.weak -= 1
             self.weak_var.set(self.weak)
         if(self.bleed != 0):
             self.bleed -= 1
             self.bleed_var.set(self.bleed)
             self.hp -= 5
             if(self.hp <= 0):
                 self.alive = False
                 self.cha_delete()
                 global enemy_number
                 enemy_number-=1
         
 class Robot:
     def __init__(self):
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
     def summon_cha(self,x,y,n):
         self.name = "8+9" + n
         self.code = n
         self.img = canvas.create_image(x, y-300, anchor='n',image=image_file3)
         self.max_hpL = tk.Label(canvas,text='/' + str(self.max_hp), font=('Arial',17))
         self.max_hpL.place(x=x+10,y=y)
         self.hpL = tk.Label(canvas, textvariable=self.hp_var, font=('Arial',17))
         self.hpL.place(x=x-20, y=y, anchor='n')
         self.weak_iconL = tk.Label(canvas, image=image_file9)
         self.weak_iconL.place(x=x-50, y=y+52, anchor='center')
         self.weakL = tk.Label(canvas, textvariable=self.weak_var, font=('Arial',15))
         self.weakL.place(x=x-20, y=y+52, anchor='center')
         self.bleed_iconL = tk.Label(canvas, image=image_file8)
         self.bleed_iconL.place(x=x+20, y=y+52, anchor='center')
         self.bleedL = tk.Label(canvas, textvariable=self.bleed_var, font=('Arial',15))
         self.bleedL.place(x=x+50, y=y+52, anchor='center')
     def cha_delete(self):
         canvas.delete(self.img)
         if(self.code == 'A'):
             r1.place_forget()
         if(self.code == 'B'):
             r2.place_forget()
         self.max_hpL.destroy()
         self.hpL.destroy()
         self.weakL.destroy()
         self.weak_iconL.destroy()
         self.bleedL.destroy()
         self.bleed_iconL.destroy()
         inf = target.name+" 再起不能"
         inf2.set(inf)
         global target_undef
         target_undef = True
     def dmg_inflicted(self):
         self.hp -= int(damage * (1 + 0.5*bool(self.weak)) * (1 - 0.4*bool(self.perseverance)))
         self.hp_var.set(self.hp)
         if(self.hp <= 0):
             self.alive = False
             self.cha_delete()
             global enemy_number
             enemy_number-=1
     def weak_inflicted(self,lvl):
         self.weak += lvl
         self.weak_var.set(self.weak)
     def bleed_inflicted(self,lvl):
         self.bleed += lvl
         self.bleed_var.set(self.bleed)
     def skill(self,random): #傳入1~12任一數
         if self.power:
             self.power = False
             self.hpL['fg'] = 'black'
             self.max_hpL['fg'] = 'black'
             dmg = int(self.atk * 2 * (1 + 0.5*bool(Mode_Battle.player.weak)))
             Mode_Battle.player.dmg_inflicted(dmg)
             Mode_Battle.player.bleed += 2
             Mode_Battle.player.bleed_var.set(Mode_Battle.player.bleed)
             inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
             inf1.set(inf)
             inf2.set("被附加了 2 層流血")
         elif(random%4 == 0): #attack
             dmg = int(self.atk * (1 + 0.5*bool(Mode_Battle.player.weak)))
             Mode_Battle.player.dmg_inflicted(dmg)
             inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
             inf1.set(inf)
             inf2.set("")
         elif(random%4 == 1): #heal
             self.hp += 15
             if (self.hp > self.max_hp):
                 self.hp = self.max_hp
                 self.hp_var.set(self.hp)
                 inf = self.name + " 回復了自身血量"
                 inf1.set(inf)
                 inf2.set("")
         elif(random%4 == 2): #powerful attack
             self.power = True
             self.hpL['fg'] = 'red'
             self.max_hpL['fg'] = 'red'
             inf = self.name + " 準備在下回合使出強力攻擊"
             inf1.set(inf)
             inf2.set("")
         elif(random%4 == 3): #buff&debuff
             self.perseverance += 2
             self.perseverance_var.set(self.perseverance)
             Mode_Battle.player.weak += 2
             Mode_Battle.player.weak_var.set(Mode_Battle.player.weak)
             inf = self.name + " 對自身附加了 2 層堅毅"
             inf1.set(inf)
             inf2.set("被附加了 2 層虛弱")
     def end_round(self):
         if(self.weak != 0):
             self.weak -= 1
             self.weak_var.set(self.weak)
         if(self.bleed != 0):
             self.bleed -= 1
             self.bleed_var.set(self.bleed)
             self.hp -= 5
             if(self.hp <= 0):
                 self.alive = False
                 self.cha_delete()
                 global enemy_number
                 enemy_number-=1
         if(self.perseverance != 0):
             self.perseverance -= 1
             self.perseverance_var.set(self.perseverance) 
class Boss_Ming:
    def __init__(self):
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
    def summon_cha(self,x,y):
        self.name = "Boss"
        self.img = canvas.create_image(x, y-300, anchor='n',image=image_file5)
        self.max_hpL = tk.Label(canvas,text='/' + str(self.max_hp), font=('Arial',17))
        self.max_hpL.place(x=x+10,y=y)
        self.hpL = tk.Label(canvas, textvariable=self.hp_var, font=('Arial',17))
        self.hpL.place(x=x-20, y=y, anchor='n')
        self.weak_iconL = tk.Label(canvas, image=image_file9)
        self.weak_iconL.place(x=x-80, y=y+52, anchor='center')
        self.weakL = tk.Label(canvas, textvariable=self.weak_var, font=('Arial',15))
        self.weakL.place(x=x-50, y=y+52, anchor='center')
        self.bleed_iconL = tk.Label(canvas, image=image_file8)
        self.bleed_iconL.place(x=x-10, y=y+52, anchor='center')
        self.bleedL = tk.Label(canvas, textvariable=self.bleed_var, font=('Arial',15))
        self.bleedL.place(x=x+20, y=y+52, anchor='center')
        self.perseverance_iconL = tk.Label(canvas, image=image_file7)
        self.perseverance_iconL.place(x=x+60, y=y+52, anchor='center')
        self.perseveranceL = tk.Label(canvas, textvariable=self.perseverance_var, font=('Arial',15))
        self.perseveranceL.place(x=x+90, y=y+52, anchor='center')
    def summon_cha_sec(self,x,y):
        canvas.delete(self.img)
        self.img = canvas.create_image(x, y-300, anchor='n',image=image_file6)
        self.max_hpL['text'] = '/120'
        self.hp_var.set(self.hp)
    def cha_delete(self):
        canvas.delete(self.img)
        r1.place_forget()
        self.max_hpL.destroy()
        self.hpL.destroy()
        self.weakL.destroy()
        self.weak_iconL.destroy()
        self.bleedL.destroy()
        self.bleed_iconL.destroy()
        inf = target.name+" 敗北了"
        inf2.set(inf)
        global target_undef
        target_undef = True
    def dmg_inflicted(self):
        self.hp -= int(damage * (1 + 0.5*bool(self.weak)) * (1 - 0.4*bool(self.perseverance)))
        self.hp_var.set(self.hp)
        if(self.hp <= 0 and self.transform == True):
            self.alive = False
            self.cha_delete()
        elif(self.hp <= 0):
            self.transform = True
            inf = "小明進入第二階段"
            inf1.set(inf)
            inf = "能力大幅提升了"
            inf2.set(inf)
            self.hp = 120
            self.weak = 0
            self.bleed = 0
            self.perseverance = 0
            self.summon_cha_sec(950, 350)
    def weak_inflicted(self,lvl):
        self.weak += lvl
        self.weak_var.set(self.weak)
    def bleed_inflicted(self,lvl):
        self.bleed += lvl
        self.bleed_var.set(self.bleed)
    def skill(self,random): #傳入1~12任一數
        if(self.transform == False): #第一階段技能組
            if(random%3 == 0): #attack
                dmg = int(self.atk * (1 + 0.5*bool(Mode_Battle.player.weak)))
                Mode_Battle.player.dmg_inflicted(dmg)
                inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
                inf1.set(inf)
                inf2.set("")
            elif(random%3 == 1): #inflict debuff
                Mode_Battle.player.weak += 2
                Mode_Battle.player.weak_var.set(Mode_Battle.player.weak)
                inf = "被 " + self.name + " 附加了 2 層虛弱"
                inf1.set(inf)
                inf2.set("")
            elif(random%3 == 2): #atk up
                self.atk += 3
                inf = self.name + " 攻擊力上升了3點"
                inf1.set(inf)
                inf2.set("")
        else: #第二階段技能組
            if self.power:
                self.power = False
                self.hpL['fg'] = 'black'
                self.max_hpL['fg'] = 'black'
                dmg = int(self.atk * 2.5 * (1 + 0.5*bool(Mode_Battle.player.weak)))
                Mode_Battle.player.dmg_inflicted(dmg)
                inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
                inf1.set(inf)
                inf2.set("")
            elif(random%5 == 1): #attack
                dmg = int(self.atk * (1 + 0.5*bool(Mode_Battle.player.weak)))
                Mode_Battle.player.dmg_inflicted(dmg)
                inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
                inf1.set(inf)
                inf2.set("")
            elif(random%5 == 0): #heal
                self.hp += 30
                if (self.hp > self.max_hp):
                    self.hp = self.max_hp
                    self.hp_var.set(self.hp)
                    inf = self.name + " 回復了自身血量"
                    inf1.set(inf)
                    inf2.set("")
            elif(random%5 == 3): #powerful attack
                self.power = True
                self.hpL['fg'] = 'red'
                self.max_hpL['fg'] = 'red'
                inf = self.name + " 準備在下回合使出強力攻擊"
                inf1.set(inf)
                inf2.set("")
            elif(random%5 == 2): #buff&debuff
                self.perseverance += 2
                self.perseverance_var.set(self.perseverance)
                Mode_Battle.player.weak += 2
                Mode_Battle.player.weak_var.set(Mode_Battle.player.weak)
                inf = self.name + " 對自身附加了 2 層堅毅"
                inf1.set(inf)
                inf2.set("被附加了 2 層虛弱")
            elif(random%5 == 4): #bleeding atk
                dmg = int(self.atk * (1 + 0.5*bool(Mode_Battle.player.weak)))
                Mode_Battle.player.dmg_inflicted(dmg)
                Mode_Battle.player.bleed += 2
                Mode_Battle.player.bleed_var.set(Mode_Battle.player.bleed)
                inf = "從 " + self.name + " 受到了 " + str(dmg) + " 點傷害"
                inf1.set(inf)
                inf2.set("被附加了 2 層流血")
    def end_round(self):
        if(self.weak != 0):
            self.weak -= 1
            self.weak_var.set(self.weak)
        if(self.bleed != 0):
            self.bleed -= 1
            self.bleed_var.set(self.bleed)
            self.hp -= 5
            if(self.hp <= 0 and self.transform == True):
                self.alive = False
                self.cha_delete()
            elif(self.hp <= 0):
                self.transform = True
                inf = "小明進入第二階段"
                inf1.set(inf)
                inf = "能力大幅提升了"
                inf2.set(inf)
                self.hp = 120
                self.weak = 0
                self.bleed = 0
                self.perseverance = 0
                self.summon_cha_sec(950, 350)
        if(self.perseverance != 0):
            self.perseverance -= 1
            self.perseverance_var.set(self.perseverance)