# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 02:12:55 2023

@author: user
"""
class CardCollection:
    def __init__(self):
        self.grave = []
        self.deck = []
        self.hand_card = []
        
        
        
class Card:
    def __init__(self,mana,damage,target,target_undef,inf1,inf2,grave,player):
        
        self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave = mana,damage,target,target_undef,inf1,inf2,grave
        self.player = player
    def renew_mana(self,mana):
        self.mana = mana
    def attack(self,enemy_number):
        
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
        if self.mana >=1 :
            if target_undef:
                inf1.set("你沒選擇目標")
                inf2.set("")      
            else:
                self.mana-=1
                damage=int(self.player.atk*(1+0.5*bool(self.player.frantic)))
                t = target
                inf = "對 "+target.name+" 造成了 "+str(damage)+" 點傷害"
                inf1.set(inf)
                inf2.set("")
                enemy_number = t.dmg_inflicted(damage,enemy_number)
                grave.append(1)
        else :
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"
        return enemy_number
    #class double_attack():
        #image_file = tk.PhotoImage(file='pictures/card_pige2.gif')
    def double_attack(self,enemy_number):
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
       
        if self.mana >=2 :
            if target_undef:
                inf1.set("你沒選擇目標")
                inf2.set("")      
            else:
                try:
                    self.mana-=2
                    damage=int(self.player.atk*(1+0.5*bool(self.player.frantic)))*2
                    t = target
                    inf = "對 "+target.name+" 造成了 "+str(damage)+" 點傷害"
                    inf1.set(inf)
                    inf2.set("")
                    enemy_number = t.dmg_inflicted(damage,enemy_number)
                    grave.append(2)
                    
                except:
                    inf1.set("你沒選擇目標")
                    inf2.set("")
        else :
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"
        return enemy_number
    #class bleed_attack():
        #image_file = tk.PhotoImage(file='pictures/card_bag.gif')
    def bleed_attack(self,enemy_number):
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
        if self.mana >=1 :
            if target_undef:
                inf1.set("你沒選擇目標")
                inf2.set("")      
            else:
                try:
                    self.mana-=1
                    damage=int(self.player.atk*(1+0.5*bool(self.player.frantic)))
                    t = target
                    inf = "對 "+target.name+" 造成了 "+str(damage)+" 點傷害,讓敵人增加一層流血"
                    inf1.set(inf)
                    inf2.set("")
                    enemy_number = t.dmg_inflicted(damage,enemy_number)
                    t.bleed_inflicted(1)
                    grave.append(3)
                except:
                    inf1.set("你沒選擇目標")
                    inf2.set("") 
        else:
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"
        return enemy_number
    #class go_frantic():
       # image_file = tk.PhotoImage(file='pictures/card_氣到吐血.gif')
    def go_frantic(self):
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
        if self.mana >= 1 :
            self.mana-=1
            self.player.frantic+=2
            self.player.frantic_var.set(self.player.frantic)                
            self.player.hp-=5
            inf = "狂暴狀態兩回合"
            inf1.set(inf)
            inf2.set("")
            grave.append(4)
    
        else :
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"
    #class inter_attack():
        #image_file = tk.PhotoImage(file='pictures/card_punch.gif')
    def inter_attack(self,enemy_number):
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
        if self.mana >=2 :
            if target_undef:
                inf1.set("你沒選擇目標")
                inf2.set("")      
            else:
                try:    
                    self.mana-=2
                    damage=int(self.player.atk*(2+0.5*bool(self.player.frantic)))
                    t = target
                    inf = "對 "+target.name+" 造成了 "+str(int(damage)*2)+" 點傷害,對你造成"+str(self.player.atk)+"傷害"
                    inf1.set(inf)
                    inf2.set("")
                    enemy_number = t.dmg_inflicted(damage,enemy_number)
                    self.player.hp -= self.player.atk
                    self.player.hp_var.set(self.player.hp)
                    grave.append(5)
                except:
                    inf1.set("你沒選擇目標")
                    inf2.set("")
        else :
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"
        return enemy_number
    #class atk_up():
        #image_file = tk.PhotoImage(file='pictures/card_vgr.gif')
    def atk_up(self):
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
        if self.mana >= 1:
            self.mana-=1
            self.player.atk+=1
            self.player.atk_var.set(self.player.atk)
            inf1.set("你沒選擇目標")
            inf2.set("")
            inf = "玩家增加一點攻擊力"
            inf1.set(inf)
            inf2.set("")
            grave.append(6)
    
            return self.player.atk
        else :
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"
    
    
    #class drink_blood():
        #image_file = tk.PhotoImage(file='pictures/card_DIO.gif')
    def drink_blood(self,enemy_number):
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
        if self.mana >= 1 :
            if target_undef:
                inf1.set("你沒選擇目標")
                inf2.set("")      
            else:
                try:
                    self.mana-=1
                    damage=int(self.player.atk*(1+0.5*bool(self.player.frantic)))
                    
                    t = target
                    self.player.hp+=5
                    inf = "對 "+target.name+" 造成了 "+str(damage)+" 點傷害,回復了五點血量"
                    inf1.set(inf)
                    inf2.set("")
                    enemy_number = t.dmg_inflicted(damage,enemy_number)
                    grave.append(7)
    
                    if self.player.hp>=self.player.max_hp:
                        
                        self.player.hp=self.player.max_hp
               
                    self.player.hp_var.set(self.player.hp)   
                    
                except:
                    inf1.set("你沒選擇目標")
                    inf2.set("")    
        else :
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"
        return enemy_number
                
           
    
    #class heal():
        #image_file = tk.PhotoImage(file='pictures/card_heal.gif')
    def heal(self):
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
        if self.mana >= 1 :
            self.player.hp+=5
            self.mana-=1
            self.player.hp_var.set(self.player.hp)
            if self.player.hp>=self.player.max_hp:
                
                self.player.hp=self.player.max_hp
                
                self.player.hp_var.set(self.player.hp)
            grave.append(8)
            inf = "你回復了五點血"
            inf1.set(inf)
            inf2.set("")
        else :
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"
    

    
    
    #class armor():
        #image_file = tk.PhotoImage(file='pictures/card_外套.gif')
    def armor(self):
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
        if self.mana >= 1 :
            self.mana-=1
            self.player.armor+=5
            self.player.armor_var.set(self.player.armor)
            grave.append(9)
    
            
            inf = "增加五點護甲"
            inf1.set(inf)
            inf2.set("")
        else :
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"
    #class double_armor():
        #image_file = tk.PhotoImage(file='pictures/card_後外套.gif')
    def double_armor(self):
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
        if self.mana >= 2:
            self.player.armor+=10
            self.mana-=2
            self.player.armor_var.set(self.player.armor)
            grave.append(10)
            inf = "增加十點護甲"
            inf1.set(inf)
            inf2.set("")        
        else :
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"
    #class weak_attack():
        #image_file = tk.PhotoImage(file='pictures/card_tests.gif')
    def weak_attack(self,enemy_number):
        
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
        if self.mana >= 1 :
            if target_undef:
                inf1.set("你沒選擇目標")
                inf2.set("")      
            else:
                try:
                    self.mana-=1
                    damage=int(self.player.atk*(1+0.5*bool(self.player.frantic)))
                    
                    t = target
                    inf = "對 "+target.name+" 造成了 "+str(damage)+" 點傷害,讓敵人增加兩層虛弱"
                    inf1.set(inf)
                    inf2.set("")
                    enemy_number = t.dmg_inflicted(damage,enemy_number)
                    t.weak_inflicted(3)
                    grave.append(11)
                    
                except:
                    inf1.set("你沒選擇目標")
                    inf2.set("")
        else :
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"
        return enemy_number
    
    def round_atk_up(self):
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
        if self.mana >= 1:
            self.player.atk_up+=1
            self.mana-=1
            
            
            inf = "每回合加一點攻擊力"
            inf1.set(inf)
            inf2.set("")
            grave.append(12)
        else :
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"
    
    def super_frantic(self):
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
        if self.mana >=2 :
            self.player.frantic+=3
            self.player.frantic_var.set(self.player.frantic)
            self.mana-=2
            grave.append(13)
        else :
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"
    
    def First_aid_kit(self):
        mana,damage,target,target_undef,inf1,inf2,grave = self.mana,self.damage,self.target,self.target_undef,self.inf1,self.inf2,self.grave
        if self.mana >=2 :
            self.player.heal+=3
            self.mana-=2 
            grave.append(14)
    
        else :
            inf1.set('魔力不足')
            inf2.set('')
            return "mana not enough"