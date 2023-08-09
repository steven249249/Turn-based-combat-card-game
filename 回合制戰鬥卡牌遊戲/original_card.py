# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 02:25:51 2023

@author: user
"""

        def attack():
            global mana
            global damage
            if mana >=1 :
                if target_undef:
                    inf1.set("你沒選擇目標")
                    inf2.set("")      
                else:
                
                    mana-=1
                    damage=int(self.player.atk*(1+0.5*bool(self.player.frantic)))
                    t = target
                     inf = "對 "+target.name+" 造成了 "+str(damage)+" 點傷害"
                    inf1.set(inf)
                    inf2.set("")
                    t.dmg_inflicted(damage)
                    grave.append(1)

                  
            else :
                inf1.set('魔力不足')
                inf2.set('')
        
        
        #class double_attack():
            #image_file = tk.PhotoImage(file='pictures/card_pige2.gif')
        def double_attack():
            global mana
            global damage
            if mana >=2 :
                if target_undef:
                    inf1.set("你沒選擇目標")
                    inf2.set("")      
                else:
                    try:
                        mana-=2
                        damage=int(self.player.atk*(1+0.5*bool(self.player.frantic)))*2
                        t = target
                        inf = "對 "+target.name+" 造成了 "+str(damage)+" 點傷害"
                        inf1.set(inf)
                        inf2.set("")
                        t.dmg_inflicted(damage)
                        grave.append(2)

                    except:
                        inf1.set("你沒選擇目標")
                        inf2.set("")
            else :
                inf1.set('魔力不足')
                inf2.set('')
            
        #class bleed_attack():
            #image_file = tk.PhotoImage(file='pictures/card_bag.gif')
        def bleed_attack():
            global mana
            global damage
            if mana >=1 :
                if target_undef:
                    inf1.set("你沒選擇目標")
                    inf2.set("")      
                else:
                    try:
                        mana-=1
                        damage=int(self.player.atk*(1+0.5*bool(self.player.frantic)))
                        t = target
                        inf = "對 "+target.name+" 造成了 "+str(damage)+" 點傷害,讓敵人增加一層流血"
                        inf1.set(inf)
                        inf2.set("")
                        t.dmg_inflicted(damage)
                        t.bleed_inflicted(1)
                        grave.append(3)

                    except:
                        inf1.set("你沒選擇目標")
                        inf2.set("") 
            else:
                inf1.set('魔力不足')
                inf2.set('')
                    
                    
        #class go_frantic():
           # image_file = tk.PhotoImage(file='pictures/card_氣到吐血.gif')
        def go_frantic():
            global mana
            if mana >= 1 :
                mana-=1
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
        
        #class inter_attack():
            #image_file = tk.PhotoImage(file='pictures/card_punch.gif')
        def inter_attack():
            global damage
            global mana
            if mana >=2 :
                if target_undef:
                    inf1.set("你沒選擇目標")
                    inf2.set("")      
                else:
                    try:    
                        mana-=2
                        damage=int(self.player.atk*(1+0.5*bool(self.player.frantic)))
                        t = target
                        inf = "對 "+target.name+" 造成了 "+str(int(damage)*2)+" 點傷害,對你造成"+str(self.player.atk)+"傷害"
                        inf1.set(inf)
                        inf2.set("")
                        t.dmg_inflicted(damage)
                        grave.append(5)
                    except:
                        inf1.set("你沒選擇目標")
                        inf2.set("")
            else :
                inf1.set('魔力不足')
                inf2.set('')
        
        #class atk_up():
            #image_file = tk.PhotoImage(file='pictures/card_vgr.gif')
        def atk_up():
            global mana
            
            if mana >= 1:
                mana-=1
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
        
        
        
        #class drink_blood():
            #image_file = tk.PhotoImage(file='pictures/card_DIO.gif')
        def drink_blood():
            global damage
            global mana
            if mana >= 1 :
                if target_undef:
                    inf1.set("你沒選擇目標")
                    inf2.set("")      
                else:
                    try:
                        mana-=1
                        damage=int(self.player.atk*(1+0.5*bool(self.player.frantic)))
                        
                        t = target
                        self.player.hp+=3
                        inf = "對 "+target.name+" 造成了 "+str(damage)+" 點傷害,回復了三點血量"
                        inf1.set(inf)
                        inf2.set("")
                        t.dmg_inflicted(damage)
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
                
                    
               
        
        #class heal():
            #image_file = tk.PhotoImage(file='pictures/card_heal.gif')
        def heal():
            global mana
            if mana >= 1 :
                self.player.hp+=5
                mana-=1
                
                if self.player.hp>=self.player.max_hp:
                    
                    self.player.hp=self.player.max_hp
                    
                    self.player.hp_var.set(self.player.hp)
                grave.append(8)
            else :
                inf1.set('魔力不足')
                inf2.set('')
    
        
            inf = "你回復了五點血"
            inf1.set(inf)
            inf2.set("")
        
        
        #class armor():
            #image_file = tk.PhotoImage(file='pictures/card_外套.gif')
        def armor():
            global mana
            if mana >= 1 :
                mana-=1
                self.player.armor+=5
                self.player.armor_var.set(self.player.armor)
                grave.append(9)

                
                inf = "增加五點護甲"
                inf1.set(inf)
                inf2.set("")
            else :
                inf1.set('魔力不足')
                inf2.set('')
        #class double_armor():
            #image_file = tk.PhotoImage(file='pictures/card_後外套.gif')
        def double_armor():
            global mana
            if mana >= 2:
                self.player.armor+=10
                mana-=2
                self.player.armor_var.set(self.player.armor)
                grave.append(10)
                inf = "增加十點護甲"
                inf1.set(inf)
                inf2.set("")        
            else :
                inf1.set('魔力不足')
                inf2.set('')
        #class weak_attack():
            #image_file = tk.PhotoImage(file='pictures/card_tests.gif')
        def weak_attack():
            global mana
            global damage
            
            if mana >= 1 :
                if target_undef:
                    inf1.set("你沒選擇目標")
                    inf2.set("")      
                else:
                    try:
                        mana-=1
                        damage=int(self.player.atk*(1+0.5*bool(self.player.frantic)))
                        
                        t = target
                        inf = "對 "+target.name+" 造成了 "+str(damage)+" 點傷害,讓敵人增加兩層虛弱"
                        inf1.set(inf)
                        inf2.set("")
                        t.dmg_inflicted(damage)
                        t.weak_inflicted(3)
                        grave.append(11)
                    except:
                        inf1.set("你沒選擇目標")
                        inf2.set("")
            else :
                inf1.set('魔力不足')
                inf2.set('')
        

        def round_atk_up():
            global mana
            if mana >= 1:
                self.player.atk_up+=1
                mana-=1
                
                
                inf = "每回合加一點攻擊力"
                inf1.set(inf)
                inf2.set("")
                grave.append(12)
            else :
                inf1.set('魔力不足')
                inf2.set('')

        def super_frantic():
            global mana
            if mana >=2 :
                self.player.frantic+=3
                self.player.frantic_var.set(self.player.frantic)
                mana-=2
                grave.append(13)
            else :
                inf1.set('魔力不足')
                inf2.set('')

        def First_aid_kit():
            global mana
            if mana >=2 :
                Mode_Battle.player.heal+=3
                mana-=2 
                grave.append(14)

            else :
                inf1.set('魔力不足')
                inf2.set('')
        
