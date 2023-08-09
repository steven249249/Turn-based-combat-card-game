# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 00:10:19 2020

@author: a2894
"""

import sys
import tkinter as tk
import story as st
import random
from PIL import ImageTk, Image, ImageSequence
from monster import *
from player import *
from card import *
from threading import *
import time
from functools import partial
decks=[1,2,3,4,4,6,7,8,9,10,11,12,13,14]
grave=[]
Reward_Card=['a','b','c']
mana=3
damage=2
level = 0
abcd=True
enemy_number = 0

cc = CardCollection()
cc.grave=[]
cc.decks=[1,2,3,4,5,6,7,8,9,10]
cc.hand_card = []

    
class Mode_Start():
    def __init__(self,master):
        ba = tk.Button(master, text = "開始遊戲" ,command=lambda: self.frame_change())
        ba.pack()   
        self.s = st.Story(window)
        self.story_frame  = self.s.get_frame()
    def change_text(self,t):
        t['text'] = "後來變這樣"
    def frame_change(self):
        FrameStart.pack_forget()
        self.s.story1()
        FrameMap.pack()
        #m2.enter()
        

class Mode_Map():
    def __init__(self,master):
        self.image_file1 = tk.PhotoImage(file='pictures/map0.gif')
        self.image_file2 = tk.PhotoImage(file='pictures/map12.gif')
        self.image_file3 = tk.PhotoImage(file='pictures/map23.gif')
        self.image_file4 = tk.PhotoImage(file='pictures/map34.gif')
        self.image_file5 = tk.PhotoImage(file='pictures/map45.gif')
        self.image_file6 = tk.PhotoImage(file='pictures/next.png')
        self.canvas=tk.Canvas(master, width=1280, height=720)
        self.canvas.pack()
        path_map0 = 'pictures/map0.gif'
        self.Map01 = Image.open(path_map0)
        path_map12 = 'pictures/map12.gif'
        self.Map12 = Image.open(path_map12)
        path_map23 = 'pictures/map23.gif'
        self.Map23 = Image.open(path_map23)
        path_map34 = 'pictures/map34.gif'
        self.Map34 = Image.open(path_map34)
        path_map45 = 'pictures/map45.gif'
        self.Map45 = Image.open(path_map45)
        self.level = 0
        self.enter()
        self.story_num = 2

        ba = tk.Button(self.canvas,image=self.image_file6,height=5,width=5 ,command = self.frame_change_to_story)
        self.canvas.create_window(1070,620,width=187,height=76,window=ba)
    def frame_change_to_story(self):
        FrameMap.pack_forget()
        if self.story_num == 2:
            m1.s.story2()
        elif self.story_num ==4:
            m1.s.story3()
        elif self.story_num == 6:
            m1.s.story4()
        
        self.story_num+=1
        m4.renew(pack_flag=True)
    def enter(self):
        if self.level == 0 :
            self.map000= ImageTk.PhotoImage(self.Map01.resize((1280, 720), Image.ANTIALIAS))
            self. MAP00 = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.map000)
        elif self.level == 1:
            self.canvas.delete(self.MAP00)
            self.map100= ImageTk.PhotoImage(self.Map12.resize((1280, 720), Image.ANTIALIAS))
            self. MAP11 = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.map100)
    
        elif self.level == 2 :
            self.canvas.delete(self.MAP11)
            self.map200= ImageTk.PhotoImage(self.Map23.resize((1280, 720), Image.ANTIALIAS))
            self. MAP11 = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.map200)
         
        elif self.level == 3 :
            self.canvas.delete(self.MAP11)
            self.map300= ImageTk.PhotoImage(self.Map34.resize((1280, 720), Image.ANTIALIAS))

            self. MAP11 = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.map300)
           
        elif self.level == 4 :
            self.canvas.delete(self.MAP11)
            self.map400= ImageTk.PhotoImage(self.Map45.resize((1280, 720), Image.ANTIALIAS))

            self. MAP11 = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.map400)
        self.level +=1
class Mode_Draw():
    
    def __init__(self,master):
        self.reward_image = tk.Label(master,text="reward")
        self.button_draw = tk.Button(master,text="點我抽獎",command = lambda : self.draw())
        self.button_draw.pack()
        self.button_next = tk.Button(master,text="next",command = self.frame_change)
        self.button_next.pack()
        self.reward_image = tk.Label(master)
        self.reward_msg  = tk.StringVar()
        self.reward_msg_l = tk.Label(master, textvariable=self.reward_msg, font=('Arial',17))
    def renew(self):
        self.button_draw.pack()
        self.reward_image['image'] = ''
        self.reward_msg.set('')
    def draw(self):
        reward = random.randint(1,14)
        cc.deck.append(reward)
        images= [
            {},
            image_file14,
            image_file15,
            image_file16,
            image_file17,
            image_file18,
            image_file19,
            image_file20,
            image_file21,
            image_file22,
            image_file23,
            image_file24,
            image_file25,
            image_file26,
            image_file27,
        ]
        
        self.reward_image['image']=images[reward]
        self.reward_image.pack()
        self.reward_msg.set('獲得了')
        self.reward_msg_l.pack()
        self.button_draw.pack_forget()
    def frame_change(self):
        FrameDraw.pack_forget()
        FrameMap.pack()
        m2.enter()
        
class Mode_Battle():
    def __init__ (self, master):
        global damage,level
        self.canvas=tk.Canvas(master, width=1280, height=720)
        self.canvas.pack()
        path_map1 = 'background2.gif'
        background2=Image.open(path_map1)
        self.img = ImageTk.PhotoImage(background2.resize((1280, 720), Image.ANTIALIAS))
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.level = 0
        
        self.var = tk.StringVar()
        self.inf1 = tk.StringVar()
        self.inf1.set("資訊欄")
        self.inf1L = tk.Label(self.canvas, textvariable=self.inf1, font=('Arial',17))
        self.inf1L.place(x=350, y=370, anchor='center')
        self.inf2 = tk.StringVar()
        self.inf2.set("資訊資訊")
        self.inf2L = tk.Label(self.canvas, textvariable=self.inf2, font=('Arial',17))
        self.inf2L.place(x=350, y=401, anchor='center')
        self.player = ability(25,5,25,self.canvas,image_list)
        self.player.summon_cha(450, 225)
        self.enemy_list = []
        card_parameter = (mana,damage,None,True,self.inf1,self.inf2,cc.grave,self.player)
        self.all_card = Card(*card_parameter)
        self.a = None
        self.b = None
        self.c = None
        self.r1 = None
        self.r2 = None
        self.r3 = None
    def renew(self,pack_flag = False): 
        if pack_flag:
            FrameBattle.pack()
       
        self.all_card.renew_mana(3)
        self.player.atk = 5 + 2*self.level
        self.player.alive = True
        self.player.max_hp = 25 + 10*self.level
        self.player.max_hpL['text'] = '/{}'.format(str(self.player.max_hp))
        self.player.atk_var.set(self.player.atk)
        self.player.armor_var.set(0)
        self.player.bleed_var.set(0)
        self.player.weak_var.set(0)
        self.player.atk_up=0
        self.player.heal =0
        self.player.frantic = 0 
        self.player.frantic_var.set(self.player.frantic)
        if pack_flag ==False:
            self.player.hp = self.player.max_hp
            self.player.hp_var.set(self.player.hp)
            self.all_card.target_undef = True
            self.all_card.target = None
            
#----------------------------------------------------------------------------------------------------------------------------------------       
        
        self.inf1.set("資訊欄")
        self.inf2.set("資訊資訊")
        
        self.monster_parameter = (level,self.canvas,self.player,self.inf1,self.inf2,damage,image_list)
      
        self.enemy_number = 0
        
        
        self.button1=tk.Button(self.canvas,text="1",height=289,width=230)
        self.button1.place(x=10,y=425)
        self.button2=tk.Button(self.canvas,text="2",height=289,width=230)
        self.button2.place(x=265,y=425)
        self.button3=tk.Button(self.canvas,text="3",height=289,width=230)
        self.button3.place(x=520,y=425)
        self.button4=tk.Button(self.canvas,text="4",height=289,width=230)
        self.button4.place(x=775,y=425)
        self.button5=tk.Button(self.canvas,text="5",height=289,width=230)
        self.button5.place(x=1000,y=425)
        self.EndButton=tk.Button(self.canvas,text="end",command=self.end_turn)
        self.EndButton.place(x=1200,y=400)
        if self.level == 0:
            self.E_Mode1()
        elif self.level ==1 :
            self.E_Mode2()
        elif self.level ==2:
            self.E_Mode3()
        elif self.level ==3:
            self.E_Mode_Boss()
        
        self.draw()
        self.level+=1
    def select(self):
        global target, target_undef
        if(self.var.get() == 'A'):
           
            self.r1['bg'] = 'green'
            if self.r2:
                self.r2['bg'] = 'white'
            if self.r3:
                self.r3['bg'] = 'white'
            
            self.all_card.target = self.a
            self.all_card.target_undef = False

            
        elif(self.var.get() == 'B'):
            self.r1['bg'] = 'white'
            if self.r2:
                self.r2['bg'] = 'green'
            if self.r3:
                self.r3['bg'] = 'white'
            self.all_card.target = self.b
            self.all_card.target_undef = False
        elif(self.var.get() == 'C'):
            self.r1['bg'] = 'white'
            if self.r2:
                self.r2['bg'] = 'white'
            if self.r3:
                self.r3['bg'] = 'green'
            self.all_card.target = self.c
            self.all_card.target_undef = False
            
    def E_Mode1(self):
        
        self.enemy_number=3
        
        #variable	綁定哪個變數。value	選擇該按鈕時回傳到變數的值。
        self.r1 = tk.Radiobutton(self.canvas, text='牙控汽車A', bg = None , font=("Courier", 16, "bold") , variable=self.var, value='A', command = self.select)
        self.r1.place(x=650, y=30, anchor='n')
        self.r2 = tk.Radiobutton(self.canvas, text='牙控飛機', bg = None , font=("Courier", 16, "bold") , variable=self.var, value='B',command = self.select)
        self.r2.place(x=875, y=30, anchor='n')
        self.r3 = tk.Radiobutton(self.canvas, text='牙控汽車C', bg = None , font=("Courier", 16, "bold") , variable=self.var, value='C', command = self.select)
        self.r3.place(x=1100, y=30, anchor='n')
        
        self.a = Car(*self.monster_parameter,self.r1)  
        self.a.summon_cha(650,350,'A')
        self.b = Plane(*self.monster_parameter,self.r2)   
        self.b.summon_cha(875, 350)
        self.c = Car(*self.monster_parameter,self.r3)  
        self.c.summon_cha(1100, 350, 'C')
        self.enemy_list = [self.a,self.b,self.c]
    def E_Mode2(self):
        
        self.enemy_number=2
        self.r1 = tk.Radiobutton(self.canvas, text='8+9A', bg = None , font=("Courier", 16, "bold") , variable=self.var, value='A' , command = self.select)
        self.r1.place(x=790, y=10, anchor='n')
        self.r2 = tk.Radiobutton(self.canvas, text='8+9B', bg = None , font=("Courier", 16, "bold") , variable=self.var, value='B' , command = self.select)
        self.r2.place(x=1090, y=10, anchor='n')
       
        self.a = Eight_Plus_Nine(*self.monster_parameter,self.r1)
        self.a.summon_cha(790,350,'A')
        self.b = Eight_Plus_Nine(*self.monster_parameter,self.r2)
        self.b.summon_cha(1090,350,'B')
        self.c = None
        self.r3 = None
        self.enemy_list = [self.a,self.b]
    def E_Mode3(self):
        
        self.enemy_number=1
        self.r1 = tk.Radiobutton(self.canvas, text='超殺機器人', bg=None, font=("Courier", 16, "bold"),variable=self.var, value='A' , command = self.select)
        self.r1.place(x=950, y=10, anchor='n')
        self.a = Robot(*self.monster_parameter,self.r1)
        self.a.summon_cha(950,350,'A')
        self.b = None
        self.r2 = None
        self.c = None
        self.r3 = None
        self.enemy_list = [self.a]
    def E_Mode_Boss(self):
        
        self.r1 = tk.Radiobutton(self.canvas, text='小明', bg=None, font=("Courier", 16, "bold"),variable=self.var, value='A' , command = self.select)
        self.r1.place(x=950, y=10, anchor='n')
   
        self.a = Boss_Ming(*self.monster_parameter,self.r1)
        self.a.summon_cha(950,350)
        self.r2 = None
        self.b = None
        self.r3 = None
        self.c = None
        self.enemy_list = [self.a]
    def card_enemy_down_check(self,command,button):
        
        result = command(self.enemy_number) 
        if result == "mana not enough":
            return
        enemy_alive_list = [enemy.alive for enemy in self.enemy_list]
        enemy_number = 0
        for status in enemy_alive_list:
            if status:
                enemy_number+=1
        
        
        if enemy_number !=None and enemy_number == 0:
            mana =3 
            self.all_card.renew_mana(3)
            self.frame_change()
            m3.renew()
        else:
            self.enemy_number = enemy_number
        if not self.all_card.target_undef :
            button['image'] = ''
            button['command'] = ''
            
        if self.all_card.target.alive!= None and self.all_card.target.alive == False:
             self.all_card.target_undef = True
            
    def remove_hand_card(self,command,button):
        result = command()
        if result == "mana not enough":
            return 
        button['image'] = ''
        button['command'] = ''
        
    def set_button_properties(self,button, image, command,attack_flag=False):
        button['image'] = image
        if attack_flag:
            button['command'] = lambda: self.card_enemy_down_check(command,button)
        else:
            button['command'] = lambda: self.remove_hand_card(command,button)
            
        
    def draw(self):
        
        global cc
    
        if len(cc.decks)< 5:
            cc.decks.extend(cc.grave)
            random.shuffle(cc.decks)
            cc.grave.clear()
        
        button_mappings = [
            {},
            {image_file14: self.all_card.attack},
            {image_file15: self.all_card.double_attack},
            {image_file16: self.all_card.bleed_attack},
            {image_file17: self.all_card.go_frantic},
            {image_file18: self.all_card.inter_attack},
            {image_file19: self.all_card.atk_up},
            {image_file20: self.all_card.drink_blood},
            {image_file21: self.all_card.heal},
            {image_file22: self.all_card.armor},
            {image_file23: self.all_card.double_armor},
            {image_file24: self.all_card.weak_attack},
            {image_file25: self.all_card.round_atk_up},
            {image_file26: self.all_card.super_frantic},
            {image_file27: self.all_card.First_aid_kit},
        ]
        attack_flag = False
        draw_cards= [button_mappings[cc.decks[i]] for i  in range(5)]
     
        for i in range(len(draw_cards)):
         
            for image,command in draw_cards[i].items():
            
                button_num = str(i+1)
                button_name = "button{}".format(button_num)
                button = getattr(self, button_name)
                if image == image_file14 or image == image_file15 or image == image_file16 or image == image_file18 or image == image_file20:
                    attack_flag = True
                else:
                    attack_flag = False
                self.set_button_properties(button, image, command,attack_flag)
            cc.grave.append(cc.decks.pop(0))
            
    def frame_battle_to_lose(self,**kwargs):
        if kwargs['event_before']!=None:
            kwargs['event_before'].wait()
            
        self.player.end_round()
        if not self.player.alive: 
            FrameBattle.pack_forget()
            FrameLose.pack()
        else:
            
            self.draw()
        if kwargs['event_after'] !=None:
            kwargs['event_after'].set()
    def enemy_all_die(self,**kwargs):
        
        if kwargs['event_before']!=None:
            kwargs['event_before'].wait()
        
        if self.player.hp<=0:
            
            return
     
        enemy_alive_list = [enemy.alive for enemy in self.enemy_list]
        enemy_number = 0
        for status in enemy_alive_list:
            if status:
                enemy_number+=1
        
        if self.enemy_number != enemy_number:
            if self.all_card.target.alive == False:
                self.all_card.target_undef = True
            self.enemy_number = enemy_number
        if enemy_number ==0:
            self.frame_change()
            m3.renew()
        if kwargs['event_after'] !=None:
            kwargs['event_after'].set()
            
    def end_turn(self):
        # self.end_round()
        global mana
        self.all_card.renew_mana(3)
        self.EndButton.config(state=tk.DISABLED)
        window.after(6000, lambda:self.EndButton.config(state=tk.NORMAL))
        for i in range(1,6):
            button_num = str(i)
            button_name = "button{}".format(button_num)
            button = getattr(self, button_name)
            button.config(state=tk.DISABLED)
            window.after(2000, lambda btn=button: btn.config(state=tk.NORMAL))
            
        # event1 = Event()
        # event2 = Event()
        # event3 = Event()
        # event4 = Event()
        event_list = [Event() for i in range(10)]
        event_list.insert(0,None)
        for i in range(len(self.enemy_list)+1):
            
            if i<len(self.enemy_list):
                self.enemy_list[i].thread = Thread(target=self.enemy_list[i].skill,
                                   kwargs={"event_before":event_list[i],"event_after":event_list[i+1],}
                                  )
            else:
                self.player_alive_thread = Thread(target=self.frame_battle_to_lose,
                                       kwargs={"event_before":event_list[i],"event_after":event_list[i+1],}
                                       )
                self.enemy_all_die_thread = Thread(target=self.enemy_all_die,
                                       kwargs={"event_before":event_list[i+1],"event_after":event_list[i+2],}
                                       )
        for enemy in self.enemy_list:
            enemy.thread.start()
        self.player_alive_thread.start()
        self.enemy_all_die_thread.start()
        # self.a.thread = Thread(target=self.a.skill,
        #                        kwargs={"event_before":None,"event_after":event1,}
        #                        )
        
        # self.b.thread = Thread(target=self.b.skill,
        #                        kwargs={"event_before":event1,"event_after":event2,}
        #                        )
        # self.c.thread = Thread(target=self.c.skill,
        #                        kwargs={"event_before":event2,"event_after":event3,}
        #                        )
        # self.player_alive_thread = Thread(target=self.frame_battle_to_lose,
        #                        kwargs={"event_before":event3,"event_after":event4,}
        #                        )
        # self.enemy_all_die_thread = Thread(target=self.enemy_all_die,
        #                        kwargs={"event_before":event3,"event_after":event4,}
        #                        )
        # self.a.thread.start()
        # self.b.thread.start()
        # self.c.thread.start()
        # self.player_alive_thread.start()
        
        
        # self.b.thread.start()
        # print(2)
        # self.b.thread.join()
        # self.c.thread.start()
        # print(3)
        # self.c.thread.join()
        # self.draw()

        # self.player.end_round()
        # for monster in [self.a,self.b,self.c]:
        #     if monster!=None:
        #         monster.end_round()
        
    def frame_change(self):
        FrameBattle.pack_forget()
        if level<4:
            FrameDraw.pack()
        else:
            m1.s.story4()
    def change_text_color(self,t):
        t['fg'] = "red"

        
class Mode_Lose():
    
    def __init__(self,master):
        
        self.master = master
        self.msg  = tk.StringVar()
        self.msg_l = tk.Label(master, text='You Lose', font=('Arial',35))
        self.msg_l.pack()
        #time.sleep(3)
        #self.frame_change()
        #self.button=tk.Button(master,text="restart",command = self.frame_change)
        #self.button.pack()
    def frame_change(self):
        self.master.pack_forget()
        m2.level = 0 
        m4.level = 0
        FrameStart.pack()
        m4.renew()
        m4.level = 0
        FrameStart.pack_forget()
        FrameStart.pack()
        
        
window = tk.Tk()


image_file1 = tk.PhotoImage(file='Enimy_image/Car.gif')
image_file2 = tk.PhotoImage(file='Enimy_image/Plane.gif')
image_file3 = tk.PhotoImage(file='Enimy_image/Eight_Plus_Nine.gif')
image_file4 = tk.PhotoImage(file='Enimy_image/Robot.gif')
image_file5 = tk.PhotoImage(file='Enimy_image/Boss_Ming1.gif')
image_file6 = tk.PhotoImage(file='Enimy_image/Boss_Ming2.gif')
image_file7 = tk.PhotoImage(file='icon_image/perseverance.gif')
image_file8 = tk.PhotoImage(file='icon_image/bleed.gif')
image_file9 = tk.PhotoImage(file='icon_image/weak.gif')
image_file10 = tk.PhotoImage(file='Enimy_image/pro.gif')
image_file11 = tk.PhotoImage(file='icon_image/atk.gif')
image_file12 = tk.PhotoImage(file='icon_image/armor.gif')
image_file13 = tk.PhotoImage(file='icon_image/frantic.gif')
image_file14 = tk.PhotoImage(file='cards/card_pige.gif')
image_file15 = tk.PhotoImage(file='cards/card_pige2.gif')
image_file16 = tk.PhotoImage(file='cards/card_bag.gif')
image_file17 = tk.PhotoImage(file='cards/card_氣到吐血.gif')

image_file18 = tk.PhotoImage(file='cards/card_punch.gif')
image_file19 = tk.PhotoImage(file='cards/card_vgr.gif')
image_file20 = tk.PhotoImage(file='cards/card_DIO.gif')
image_file21 = tk.PhotoImage(file='cards/card_heal.gif')
image_file22 = tk.PhotoImage(file='cards/card_外套.gif')
image_file23 = tk.PhotoImage(file='cards/card_後外套.gif')
image_file24 = tk.PhotoImage(file='cards/card_後外套.gif')
image_file25 = tk.PhotoImage(file='cards/card_加攻1.gif')
image_file26 = tk.PhotoImage(file='cards/card_加攻1.gif')
image_file27 = tk.PhotoImage(file='cards/card_回.gif')

image_list = [value for key, value in locals().items() if key.startswith("image_file")]


    
FrameStart = tk.Frame(window)
FrameMap = tk.Frame(window)
FrameDraw=tk.Frame(window)
FrameBattle=tk.Frame(window)
FrameText=tk.Frame(window)
FrameLose = tk.Frame(window)

m1 = Mode_Start(FrameStart)
m2 = Mode_Map(FrameMap)
m3 = Mode_Draw(FrameDraw)
m4 = Mode_Battle(FrameBattle)
m5 = Mode_Lose(FrameLose)
#frame_list = [FrameStart,m1.s.frame,FrameMap,FrameDraw,FrameBattle,FrameText]

FrameStart.pack()


def on_closing():
    #劇情的下一個鍵的wait_variable會卡到而導致無法關掉console
    m1.s.wait_var.set(1000)
    window.destroy()
    window.quit()
    
    
    

window.protocol("WM_DELETE_WINDOW", on_closing)



window.title("test")
window.geometry("1280x720")


window.mainloop()
sys.exit(0)