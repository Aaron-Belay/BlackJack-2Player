"""
Blackjack!

See the doc on Google Classroom for further instructions.

"""

from tkinter import Tk, Label, Button, Entry
import random, timer,time

class BabyBlackJack:
    def __init__(self, master):

        self.master = master
        master.title("          BlackJack")
        root.configure(background='white')

        self.player_points = []
        self.player2hand_points = []
        self.dealer_points = []
        self.playertotal = 10000
        self.hand1bet = 0
        self.hand2bet = 0
        self.fixer = 0
        self.fixer2 = 0
        self.hold = 0
        self.game = 0
        self.bust1 = 0
        self.bust2 = 0
        self.winmoney = 0
        
        self.label_player = Label(master, text="~~~ BlackJack ~~~",font=("Times", 17,"italic"),background="white")
        self.label_player.place(x = 206, y = 0)

        self.label_player2hand = Label(master, text="",font=("Times", 17,"italic"),background="white")
        self.label_player2hand.place(x = 2060, y = 0) 

        self.label_dealer = Label(master, text="By: Aaron and Raihan", background="white",font=("Times", 11,"italic"))
        self.label_dealer.place(x = 243, y = 41)

        #blank for now, but this is where we will write "Player Busts! YOU LOSE" or "YOU WIN" etc
        self.label_win = Label(master, text="", background="white")
        self.label_win.place(x = 5000, y = 57)
       
        self.deal_button = Button(master, text="DEAL",background="white", font=("Times",13,"bold"),command=self.deal,state='disabled')
        self.deal_button.place(x = 281, y = 245)

        self.deal2_button = Button(master, text="DEAL",background="white", font=("Times",13,"bold"),command=self.deal2,state='disabled')
        self.deal2_button.place(x = 2810, y = 245)



        self.hand_label = Label(master, text="How Many Hands? (Max: 2)",background="white", font=("Times",13,"bold"))
        self.hand_label.place(x = 189, y = 110)




        
        self.hand1_button = Button(master, text="  1  ",background="white", font=("Times",13,"bold"), command=self.hand1,state='normal')
        self.hand1_button.place(x = 247, y = 165)

        self.hand2_button = Button(master, text="  2  ",background="white", font=("Times",13,"bold"), command=self.hand2,state='normal')
        self.hand2_button.place(x = 337, y = 165)




        self.label_continue = Label(master, text="", background="white")
        self.label_continue.place(x = 500, y = 57)


        self.hit_button = Button(master, text="  HIT  ",background="white", font=("Times",13,"bold"), command=self.hit,state='disabled')
        self.hit_button.place(x = 215, y = 299)

        self.stand_button = Button(master, text="STAND",background="white", font=("Times",13,"bold"), command=self.stand,state='disabled')
        self.stand_button.place(x = 340, y = 299)




        self.hit2hand1_button = Button(master, text="  HIT  ",background="white", font=("Times",13,"bold"), command=self.hit2hand1,state='disabled')
        self.hit2hand1_button.place(x = 2150, y = 299)

        self.hit2hand2_button = Button(master, text="  HIT  ",background="white", font=("Times",13,"bold"), command=self.hit2hand2,state='disabled')
        self.hit2hand2_button.place(x = 2150, y = 299)

        self.stand2hand1_button = Button(master, text="STAND",background="white", font=("Times",13,"bold"), command=self.stand2hand1,state='disabled')
        self.stand2hand1_button.place(x = 3400, y = 299)

        self.stand2hand2_button = Button(master, text="STAND",background="white", font=("Times",13,"bold"), command=self.stand2hand2,state='disabled')
        self.stand2hand2_button.place(x = 3400, y = 299)




        


        self.whatgon = Label(master, text="",background="white", font=("Times",13,"bold"))
        self.whatgon.place(x = 1890, y = 110)

        self.whatgon2 = Label(master, text="",background="white", font=("Times",13,"bold"))
        self.whatgon2.place(x = 1890, y = 110)


        self.labelplayer2hand_win = Label(master, text="",background="white", font=("Times",13,"bold"))
        self.labelplayer2hand_win.place(x = 1890, y = 110)

        self.finalstuff = Label(master, text="",background="white", font=("Times",13,"bold"))
        self.finalstuff.place(x = 1890, y = 110)

        self.label_win2 = Label(master, text="",background="white", font=("Times",13,"bold"))
        self.label_win2.place(x = 1890, y = 110)


        #bets
        self.bet100hand1_button = Button(master, text="100",background="white", font=("Times",9,"bold"),command=self.bet100hand1, state = 'disabled') 
        self.bet100hand1_button.place(x = 25, y = 150)
        

        self.bet200hand1_button = Button(master, text="200",background="white", font=("Times",9,"bold"),command=self.bet200hand1, state = 'disabled') 
        self.bet200hand1_button.place(x = 90, y = 150)
        
        self.bet300hand1_button = Button(master, text="300",background="white", font=("Times",9,"bold"),command=self.bet300hand1, state = 'disabled') 
        self.bet300hand1_button.place(x = 25, y = 185)

        self.bet400hand1_button = Button(master, text="400",background="white", font=("Times",9,"bold"),command=self.bet400hand1, state = 'disabled') 
        self.bet400hand1_button.place(x = 90, y = 185)

        self.bet500hand1_button = Button(master, text="500",background="white", font=("Times",9,"bold"),command=self.bet500hand1, state = 'disabled') 
        self.bet500hand1_button.place(x = 25, y = 220)

        self.bet600hand1_button = Button(master, text="600",background="white", font=("Times",9,"bold"),command=self.bet600hand1, state = 'disabled') 
        self.bet600hand1_button.place(x = 90, y = 220)

        self.bet700hand1_button = Button(master, text="700",background="white", font=("Times",9,"bold"),command=self.bet700hand1, state = 'disabled') 
        self.bet700hand1_button.place(x = 25, y = 255)

        self.bet800hand1_button = Button(master, text="800",background="white", font=("Times",9,"bold"),command=self.bet800hand1, state = 'disabled') 
        self.bet800hand1_button.place(x = 90, y = 255)

        self.bet900hand1_button = Button(master, text="900",background="white", font=("Times",9,"bold"), command=self.bet900hand1,state = 'disabled') 
        self.bet900hand1_button.place(x = 25, y = 290)

        self.bet1000hand1_button = Button(master, text="1000",background="white", font=("Times",9,"bold"),command=self.bet1000hand1, state = 'disabled') 
        self.bet1000hand1_button.place(x = 86, y = 290)
      
        #bets hand2
        self.bet100hand2_button = Button(master, text="100",background="white", font=("Times",9,"bold"),command=self.bet100hand2, state = 'disabled') 
        self.bet100hand2_button.place(x = 505, y = 150)

        self.bet200hand2_button = Button(master, text="200",background="white", font=("Times",9,"bold"),command=self.bet200hand2,  state = 'disabled') 
        self.bet200hand2_button.place(x = 570, y = 150)
        
        self.bet300hand2_button = Button(master, text="300",background="white", font=("Times",9,"bold"),command=self.bet300hand2,  state = 'disabled') 
        self.bet300hand2_button.place(x = 505, y = 185)

        self.bet400hand2_button = Button(master, text="400",background="white", font=("Times",9,"bold"),command=self.bet400hand2,  state = 'disabled') 
        self.bet400hand2_button.place(x = 570, y = 185)

        self.bet500hand2_button = Button(master, text="500",background="white", font=("Times",9,"bold"),command=self.bet500hand2,  state = 'disabled') 
        self.bet500hand2_button.place(x = 505, y = 220)

        self.bet600hand2_button = Button(master, text="600",background="white", font=("Times",9,"bold"),command=self.bet600hand2,  state = 'disabled') 
        self.bet600hand2_button.place(x = 570, y = 220)

        self.bet700hand2_button = Button(master, text="700",background="white", font=("Times",9,"bold"),command=self.bet700hand2,  state = 'disabled') 
        self.bet700hand2_button.place(x = 505, y = 255)

        self.bet800hand2_button = Button(master, text="800",background="white", font=("Times",9,"bold"),command=self.bet800hand2,  state = 'disabled') 
        self.bet800hand2_button.place(x = 570, y = 255)

        self.bet900hand2_button = Button(master, text="900",background="white", font=("Times",9,"bold"),command=self.bet900hand2,  state = 'disabled') 
        self.bet900hand2_button.place(x = 505, y = 290)

        self.bet1000hand2_button = Button(master, text="1000",background="white", font=("Times",9,"bold"),command=self.bet1000hand2,  state = 'disabled') 
        self.bet1000hand2_button.place(x = 566, y = 290)

        self.stopbet1_button = Button(master,text = "STOP BETTING",background="white", font=("Times",9,"bold"),command=self.stopbet1,  state = 'disabled')
        self.stopbet1_button.place(x = 22, y = 325)
        
        self.stopbet2_button = Button(master,text = "STOP BETTING",background="white", font=("Times",9,"bold"),command=self.stopbet2,  state = 'disabled')
        self.stopbet2_button.place(x = 501, y = 325)
        
        
        self.yourtotal = Label(master, text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        self.yourtotal.place(x = 20, y = 400)

        self.playerhand1bet = Label(master, text =  "You've bet $%d on Hand 1" % self.hand1bet,background="white", font=("Times",11,"italic"))
        self.playerhand1bet.place(x = 20, y = 380)

        self.playerhand2bet = Label(master, text =  "You've bet $%d on Hand 2" % self.hand2bet,background="white", font=("Times",11,"italic"))

        self.playerhand2bet.place(x = 2000, y = 380)

        #bet stuff
        self.label_win2 = Label(master, text="",background="white", font=("Times",9,"bold"))

        self.label_win2.place(x = 5000, y = 110)

        self.winnings = Label(master, text="No Money Has Been Won",background="white", font=("Times",13,"bold"))
        self.winnings.place(x = 1890, y = 110)

        self.gamereset = Label(master, text="The game will now reset...",background="white", font=("Times",12))
        self.gamereset.place(x = 1890, y = 110)


        self.startover_button = Button(master,text = "START OVER",background="white", font=("Times",11,"bold"),command=self.startover,  state = 'disabled')
        self.startover_button.place(x = 492, y = 390)

        self.startover_Label = Label(master, text="Your Total Will Now Reset!",background="white", font=("Times",11))
        self.startover_Label.place(x = 1890, y = 390)

        
        

        




    def hand1(self):
      self.hold += 1
      self.deal_button.config(state='disabled')
      self.hit_button.config(state='disabled')
      self.stand_button.config(state='disabled')
      self.hand1_button.config(state= 'disabled')
      self.hand2_button.config(state= 'disabled')
      

      self.hand1_button.place(x = 247, y = 145)
      self.hand2_button.place(x = 337, y = 145)


      self.label_continue.config (text="Great! Now Place Your Bets...",font=("Times", 15,"italic"))

      self.hand_label.config(text="Are You Feeling Lucky? \n(Bet More)",background="white", font=("Times",11,"bold"))
      self.hand_label.place(x = 224, y = 90) 

      self.label_win2.config (text = "HAND 1:\nHow Much Will You Bet? ",background="white", font=("Times",9,"bold"))
      self.label_win2.place(x = 5, y = 110)
      self.label_continue.place(x = 170, y = 195)

      self.bet100hand1_button.config(state = 'normal')  
      self.bet200hand1_button.config(state = 'normal') 
      self.bet300hand1_button.config(state = 'normal') 
      self.bet400hand1_button.config(state = 'normal') 
      self.bet500hand1_button.config(state = 'normal') 
      self.bet600hand1_button.config(state = 'normal') 
      self.bet700hand1_button.config(state = 'normal') 
      self.bet800hand1_button.config(state = 'normal') 
      self.bet900hand1_button.config(state = 'normal') 
      self.bet1000hand1_button.config(state = 'normal') 
      self.stopbet1_button.config(state = 'normal') 
      self.deal2_button.config(state='disabled')

    def bet100hand1(self):
        if self.playertotal > 0:
          self.fixer = self.hand1bet + self.playertotal
          self.playertotal -= 100
          if self.playertotal > 0:
            self.hand1bet += 100
            self.playerhand1bet.config(text =  "You've bet $%d on Hand 1" % self.hand1bet,background="white", font=("Times",11,"italic"))
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
          elif self.playertotal < 0:
            self.playertotal += 700
            self.playerhand1bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))    
          else:
            self.disablebet()
            self.hand1bet = self.fixer
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand1bet.config(text =  "You've gone all in on Hand 1! ($%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))

    def bet200hand1(self):
      if self.playertotal > 0:
        self.fixer = self.hand1bet + self.playertotal
        self.playertotal -= 200
        if self.playertotal > 0:
          self.hand1bet += 200
          self.playerhand1bet.config(text =  "You've bet $%d on Hand 1" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 200
          self.playerhand1bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))    
        else:
            self.disablebet()
            self.hand1bet = self.fixer
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand1bet.config(text =  "You've gone all in on Hand 1! ($%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))  
    def bet300hand1(self):
      if self.playertotal > 0:  
        self.fixer = self.hand1bet + self.playertotal
        self.playertotal -= 300
        if self.playertotal > 0: 
          self.hand1bet += 300
          self.playerhand1bet.config(text =  "You've bet $%d on Hand 1" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 300
          self.playerhand1bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))    
        else:
            self.disablebet()
            self.hand1bet = self.fixer
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand1bet.config(text =  "You've gone all in on Hand 1! ($%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
    def bet400hand1(self):
      if self.playertotal > 0:
        self.fixer = self.hand1bet + self.playertotal
        self.playertotal -= 400
        if self.playertotal > 0:
          self.hand1bet += 400
          self.playerhand1bet.config(text =  "You've bet $%d on Hand 1" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 400
          self.playerhand1bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))  
        else:
            self.disablebet()
            self.hand1bet = self.fixer
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand1bet.config(text =  "You've gone all in on Hand 1! ($%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
    def bet500hand1(self):
      if self.playertotal > 0:
        self.fixer = self.hand1bet + self.playertotal
        self.playertotal -= 500
        if self.playertotal > 0: 
          self.hand1bet += 500
          self.playerhand1bet.config(text =  "You've bet $%d on Hand 1" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 500
          self.playerhand1bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))    
        else:
            self.disablebet()
            self.hand1bet = self.fixer
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand1bet.config(text =  "You've gone all in on Hand 1! ($%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
    def bet600hand1(self):
      if self.playertotal > 0:
        self.fixer = self.hand1bet + self.playertotal
        self.playertotal -= 600
        if self.playertotal > 0:
          self.hand1bet += 600
          self.playerhand1bet.config(text =  "You've bet $%d on Hand 1" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 600
          self.playerhand1bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))    
        else:
            self.disablebet()
            self.hand1bet = self.fixer
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand1bet.config(text =  "You've gone all in on Hand 1! ($%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
    def bet700hand1(self):
      if self.playertotal > 0:
        self.fixer = self.hand1bet + self.playertotal
        self.playertotal -= 700
        if self.playertotal > 0:
          self.hand1bet += 700
          self.playerhand1bet.config(text =  "You've bet $%d on Hand 1" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 700
          self.playerhand1bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))  
        else:
            self.disablebet()
            self.hand1bet = self.fixer
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand1bet.config(text =  "You've gone all in on Hand 1! ($%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
    def bet800hand1(self):
      if self.playertotal > 0:
        self.fixer = self.hand1bet + self.playertotal
        self.playertotal -= 800
        if self.playertotal > 0: 
            self.hand1bet += 800
            self.playerhand1bet.config(text =  "You've bet $%d on Hand 1" % self.hand1bet,background="white", font=("Times",11,"italic"))
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 800
          self.playerhand1bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))    
        else:
            self.disablebet()
            self.hand1bet = self.fixer
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand1bet.config(text =  "You've gone all in on Hand 1! ($%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
    def bet900hand1(self):
      if self.playertotal > 0:
        self.fixer = self.hand1bet + self.playertotal
        self.playertotal -= 900
        if self.playertotal > 0: 
          self.hand1bet += 900
          self.playerhand1bet.config(text =  "You've bet $%d on Hand 1" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 900
          self.playerhand1bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))  
        else:
            self.disablebet()
            self.hand1bet = self.fixer
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand1bet.config(text =  "You've gone all in on Hand 1! ($%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
    def bet1000hand1(self):
      if self.playertotal > 0:
        self.fixer = self.hand1bet + self.playertotal
        self.playertotal -= 1000
        if self.playertotal > 0: 
          self.hand1bet += 1000
          self.playerhand1bet.config(text =  "You've bet $%d on Hand 1" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 1000
          self.playerhand1bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        else:
            self.disablebet()
            self.hand1bet = self.fixer
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand1bet.config(text =  "You've gone all in on Hand 1! ($%d)" % self.hand1bet,background="white", font=("Times",11,"italic"))
          
    def bet100hand2(self):
      if self.playertotal > 0:
        self.fixer2 = self.hand2bet + self.playertotal
        self.playertotal -= 100
        if self.playertotal > 0:  
          self.hand2bet += 100
          self.playerhand2bet.config(text =  "You've bet $%d on Hand 2" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 100
          self.playerhand2bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))    
        else:
            self.disablebet()
            self.hand2bet = self.fixer2
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand2bet.config(text =  "You've gone all in on Hand 2! ($%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
        
    def bet200hand2(self):
      if self.playertotal > 0:
        self.fixer2 = self.hand2bet + self.playertotal
        self.playertotal -= 200
        if self.playertotal > 0:  
          self.hand2bet += 200
          self.playerhand2bet.config(text =  "You've bet $%d on Hand 2" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 200
          self.playerhand2bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))    
        else:
            self.disablebet()
            self.hand2bet = self.fixer2
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand2bet.config(text =  "You've gone all in on Hand 2! ($%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
        
    def bet300hand2(self):
      if self.playertotal > 0:
        self.fixer2 = self.hand2bet + self.playertotal
        self.playertotal -= 300
        if self.playertotal > 0:  
          self.hand2bet += 300
          self.playerhand2bet.config(text =  "You've bet $%d on Hand 2" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 300
          self.playerhand2bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))      
        else:
            self.disablebet()
            self.hand2bet = self.fixer2
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand2bet.config(text =  "You've gone all in on Hand 2! ($%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
        
    def bet400hand2(self):
      if self.playertotal > 0:
        self.fixer2 = self.hand2bet + self.playertotal
        self.playertotal -= 400
        if self.playertotal > 0:  
          self.hand2bet += 400
          self.playerhand2bet.config(text =  "You've bet $%d on Hand 2" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 400
          self.playerhand2bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))      
        else:
            self.disablebet()
            self.hand2bet = self.fixer2
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand2bet.config(text =  "You've gone all in on Hand 2! ($%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
        
    def bet500hand2(self):
      if self.playertotal > 0:
        self.fixer2 = self.hand2bet + self.playertotal
        self.playertotal -= 500
        if self.playertotal > 0:  
          self.hand2bet += 500
          self.playerhand2bet.config(text =  "You've bet $%d on Hand 2" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 500
          self.playerhand2bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))      
        else:
            self.disablebet()
            self.hand2bet = self.fixer2
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand2bet.config(text =  "You've gone all in on Hand 2! ($%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
        
    def bet600hand2(self):
      if self.playertotal > 0:
        self.fixer2 = self.hand2bet + self.playertotal
        self.playertotal -= 600
        if self.playertotal > 0:  
          self.hand2bet += 600
          self.playerhand2bet.config(text =  "You've bet $%d on Hand 2" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 600
          self.playerhand2bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))      
        else:
            self.disablebet()
            self.hand2bet = self.fixer2
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand2bet.config(text =  "You've gone all in on Hand 2! ($%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
        
    def bet700hand2(self):
      if self.playertotal > 0:
        self.fixer2 = self.hand2bet + self.playertotal
        self.playertotal -= 700
        if self.playertotal > 0:  
          self.hand2bet += 700
          self.playerhand2bet.config(text =  "You've bet $%d on Hand 2" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 700
          self.playerhand2bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))      
        else:
            self.disablebet()
            self.hand2bet = self.fixer2
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand2bet.config(text =  "You've gone all in on Hand 2! ($%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
        
    def bet800hand2(self):
      if self.playertotal > 0:
        self.fixer2 = self.hand2bet + self.playertotal
        self.playertotal -= 800
        if self.playertotal > 0:  
          self.hand2bet += 800
          self.playerhand2bet.config(text =  "You've bet $%d on Hand 2" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 800
          self.playerhand2bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))              
        else:
            self.disablebet()
            self.hand2bet = self.fixer2
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand2bet.config(text =  "You've gone all in on Hand 2! ($%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
        
    def bet900hand2(self):
      if self.playertotal > 0:
        self.fixer2 = self.hand2bet + self.playertotal
        self.playertotal -= 900
        if self.playertotal > 0:  
          self.hand2bet += 900
          self.playerhand2bet.config(text =  "You've bet $%d on Hand 2" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 900
          self.playerhand2bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))      
        else:
            self.disablebet()
            self.hand2bet = self.fixer2
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand2bet.config(text =  "You've gone all in on Hand 2! ($%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
        
    def bet1000hand2(self):
      if self.playertotal > 0:
        self.fixer2 = self.hand2bet + self.playertotal
        self.playertotal -= 1000
        if self.playertotal > 0:  
          self.hand2bet += 1000
          self.playerhand2bet.config(text =  "You've bet $%d on Hand 2" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        elif self.playertotal < 0:
          self.playertotal += 1000
          self.playerhand2bet.config(text =  "You don't have enough! (Current bet: $%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))      
        else:
            self.disablebet()
            self.hand2bet = self.fixer2
            self.playertotal = 0
            self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
            self.playerhand2bet.config(text =  "You've gone all in on Hand 2! ($%d)" % self.hand2bet,background="white", font=("Times",11,"italic"))

    def disablebet(self):
        self.bet100hand1_button.config(state = 'disabled')  
        self.bet200hand1_button.config(state = 'disabled') 
        self.bet300hand1_button.config(state = 'disabled') 
        self.bet400hand1_button.config(state = 'disabled') 
        self.bet500hand1_button.config(state = 'disabled') 
        self.bet600hand1_button.config(state = 'disabled') 
        self.bet700hand1_button.config(state = 'disabled') 
        self.bet800hand1_button.config(state = 'disabled') 
        self.bet900hand1_button.config(state = 'disabled') 
        self.bet1000hand1_button.config(state = 'disabled') 

        self.bet100hand2_button.config(state = 'disabled')  
        self.bet200hand2_button.config(state = 'disabled') 
        self.bet300hand2_button.config(state = 'disabled') 
        self.bet400hand2_button.config(state = 'disabled') 
        self.bet500hand2_button.config(state = 'disabled') 
        self.bet600hand2_button.config(state = 'disabled') 
        self.bet700hand2_button.config(state = 'disabled') 
        self.bet800hand2_button.config(state = 'disabled') 
        self.bet900hand2_button.config(state = 'disabled') 
        self.bet1000hand2_button.config(state = 'disabled') 

    def stopbet1(self):
        self.bet100hand1_button.config(state = 'disabled')  
        self.bet200hand1_button.config(state = 'disabled') 
        self.bet300hand1_button.config(state = 'disabled') 
        self.bet400hand1_button.config(state = 'disabled') 
        self.bet500hand1_button.config(state = 'disabled') 
        self.bet600hand1_button.config(state = 'disabled') 
        self.bet700hand1_button.config(state = 'disabled') 
        self.bet800hand1_button.config(state = 'disabled') 
        self.bet900hand1_button.config(state = 'disabled') 
        self.bet1000hand1_button.config(state = 'disabled') 
        self.stopbet1_button.config(state = 'disabled')
        if self.hold == 1:
          self.deal_button.config(state='normal')
          self.hit_button.config(state='disabled')
          self.stand_button.config(state='disabled')
          self.hand1_button.config(state= 'disabled')
          self.hand2_button.config(state= 'disabled')
          

          self.hand1_button.place(x = 247, y = 145)
          self.hand2_button.place(x = 337, y = 145)


          self.label_continue.config (text="Great! Now Press Deal...",font=("Times", 15,"italic"))
          self.label_continue.place(x = 195, y = 195)


        else:
          self.playerhand2bet.place(x = 20, y = 400)
          self.yourtotal.place(x = 20, y = 420)
          if self.playertotal == 0:
            self.stopbet2()
          else:  
            self.bet100hand2_button.config(state = 'normal')  
            self.bet200hand2_button.config(state = 'normal') 
            self.bet300hand2_button.config(state = 'normal') 
            self.bet400hand2_button.config(state = 'normal') 
            self.bet500hand2_button.config(state = 'normal') 
            self.bet600hand2_button.config(state = 'normal') 
            self.bet700hand2_button.config(state = 'normal') 
            self.bet800hand2_button.config(state = 'normal') 
            self.bet900hand2_button.config(state = 'normal') 
            self.bet1000hand2_button.config(state = 'normal') 
            self.stopbet2_button.config(state = 'normal')
            self.deal_button.config(state='disabled')
            self.hit_button.config(state='disabled')
            self.stand_button.config(state='disabled')
            self.hand1_button.config(state= 'disabled')
            self.hand2_button.config(state= 'disabled')
            

            self.hand1_button.place(x = 247, y = 145)
            self.hand2_button.place(x = 337, y = 145)


            self.label_continue.config (text="Great! Now Place Your Bets...",font=("Times", 15,"italic"))

            self.hand_label.config(text="Are You Feeling Lucky? \n(Bet More)",background="white", font=("Times",11,"bold"))
            self.hand_label.place(x = 224, y = 90) 
            
            self.label_win2.config (text = "HAND 2:\nHow Much Will You Bet? ",background="white", font=("Times",9,"bold"))
            self.label_win2.place(x = 473, y = 110)
            self.label_continue.place(x = 170, y = 195)

          
    


        

    def stopbet2(self):
      self.bet100hand2_button.config(state = 'disabled')  
      self.bet200hand2_button.config(state = 'disabled') 
      self.bet300hand2_button.config(state = 'disabled') 
      self.bet400hand2_button.config(state = 'disabled') 
      self.bet500hand2_button.config(state = 'disabled') 
      self.bet600hand2_button.config(state = 'disabled') 
      self.bet700hand2_button.config(state = 'disabled') 
      self.bet800hand2_button.config(state = 'disabled') 
      self.bet900hand2_button.config(state = 'disabled') 
      self.bet1000hand2_button.config(state = 'disabled') 
      self.stopbet2_button.config(state = 'disabled') 
      self.deal2_button.config(state='normal')
      self.hit_button.config(state='disabled')
      self.stand_button.config(state='disabled')
      self.hand1_button.config(state= 'disabled')
      self.hand2_button.config(state= 'disabled')

      self.hand1_button.place(x = 247, y = 145)
      self.hand2_button.place(x = 337, y = 145)
      self.deal_button.place(x = 3800, y = 145)
      self.deal2_button.place(x = 281, y = 245)

      self.label_continue.config (text="Great! Now Press Deal...",font=("Times", 15,"italic"))
      self.label_continue.place(x = 195, y = 195)


    def hand2(self):
      self.hold += 2
      self.hand1()

    def bethand1(self):
      self.bet100hand1.config(state = 'normal')  
      self.bet200hand1.config(state = 'normal') 
      self.bet300hand1.config(state = 'normal') 
      self.bet400hand1.config(state = 'normal') 
      self.bet500hand1.config(state = 'normal') 
      self.bet600hand1.config(state = 'normal') 
      self.bet700hand1.config(state = 'normal') 
      self.bet800hand1.config(state = 'normal') 
      self.bet900hand1.config(state = 'normal') 
      self.bet1000hand1.config(state = 'normal') 
      self.deal2_button.config(state='disabled')

      def bet100hand1(self):
        self.playertotal -= 100
        self.hand1bet += 100
      def bet200hand1(self):
        self.playertotal -= 200
        self.hand1bet += 200
      def bet300hand1(self):
        self.playertotal -= 300
        self.hand1bet += 300
      def bet400hand1(self):
        self.playertotal -= 400
        self.hand1bet += 400
      def bet500hand1(self):
        self.playertotal -= 500
        self.hand1bet += 500
      def bet600hand1(self):
        self.playertotal -= 600
        self.hand1bet += 600
      def bet700hand1(self):
        self.playertotal -= 700
        self.hand1bet += 700
      def bet800hand1(self):
        self.playertotal -= 800
        self.hand1bet += 800
      def bet900hand1(self):
        self.playertotal -= 900
        self.hand1bet += 900
      def bet1000hand1(self):
        self.playertotal -= 1000
        self.hand1bet += 1000
  

      

    def deal(self):
      self.deal_button.config(state='disabled')
      self.hit_button.config(state='normal')
      self.stand_button.config(state='normal')

      self.deal_button.place(x = 281, y = 98)
      self.hit_button.place(x = 215, y = 165)
      self.stand_button.place(x = 340, y = 165)

      

      self.hand1_button.place(x = 5000, y = 145)
      self.hand2_button.place(x = 5090, y = 145)

      self.hand_label.place(x = 1809, y = 110)
      self.label_continue.place(x = 5950, y = 195)

      self.move()







      #give dealer cards
      self.dealer_points.append(random.randint(1,10))

      #give player cards
      self.player_points.append(random.randint(1,10))
      self.player_points.append(random.randint(1,10))
      
      self.label_player.config(text="Your Cards are: %d and %d\nTotal: %d" % (self.player_points[0],self.player_points[1],sum(self.player_points)),font=("Times", 12,"italic"))
      self.label_player.place(x = 226, y = 0)


      self.label_dealer.config(text="Dealers Cards are: %d and *hidden*" % (self.dealer_points[0]),font=("Times", 9,"italic"))
      self.label_dealer.place(x = 220, y = 49)

    def move(self):
      self.bet100hand1_button.place(x = 1809, y = 110) 
      self.bet200hand1_button.place(x = 1809, y = 110)
      self.bet300hand1_button.place(x = 1809, y = 110)
      self.bet400hand1_button.place(x = 1809, y = 110)
      self.bet500hand1_button.place(x = 1809, y = 110)
      self.bet600hand1_button.place(x = 1809, y = 110)
      self.bet700hand1_button.place(x = 1809, y = 110)
      self.bet800hand1_button.place(x = 1809, y = 110)
      self.bet900hand1_button.place(x = 1809, y = 110)
      self.bet1000hand1_button.place(x = 1809, y = 110) 

      self.bet100hand2_button.place(x = 1809, y = 110) 
      self.bet200hand2_button.place(x = 1809, y = 110)
      self.bet300hand2_button.place(x = 1809, y = 110)
      self.bet400hand2_button.place(x = 1809, y = 110)
      self.bet500hand2_button.place(x = 1809, y = 110)
      self.bet600hand2_button.place(x = 1809, y = 110)
      self.bet700hand2_button.place(x = 1809, y = 110)
      self.bet800hand2_button.place(x = 1809, y = 110)
      self.bet900hand2_button.place(x = 1809, y = 110)
      self.bet1000hand2_button.place(x = 1809, y = 110)

      self.label_win2.place(x = 5000, y = 110)
      self.stopbet1_button.place(x = 5000, y = 110)
      self.stopbet2_button.place(x = 5000, y = 110)

    def deal2(self):
      self.deal2_button.config(state='disabled')
      self.hit_button.config(state='normal')
      self.stand_button.config(state='normal')

      self.deal2_button.place(x = 2810, y = 118)
      self.hit_button.place(x = 2150, y = 185)
      self.stand_button.place(x = 3400, y = 185)


      self.deal_button.place(x = 2810, y = 98)


      self.hit2hand1_button.place(x = 80, y = 220)
      self.hit2hand1_button.config(text="  HIT  ",background="white", font=("Times",11,"bold"), state = "normal")

      self.stand2hand1_button.place(x = 200, y = 220)
      self.stand2hand1_button.config(text="STAND",background="white", font=("Times",11,"bold"), state = "normal")

      self.hit2hand2_button.place(x = 370, y = 220)
      self.hit2hand2_button.config(text="  HIT  ",background="white", font=("Times",11,"bold"), state = "disabled")

      self.stand2hand2_button.place(x = 490, y = 220)
      self.stand2hand2_button.config(text="STAND",background="white", font=("Times",11,"bold"), state = "disabled")


      self.whatgon.config(text="Do You Want To HIT or STAND \nFor HAND 1?",font=("Times",11,"bold"))
      self.whatgon.place(x = 56, y = 135)

      self.whatgon2.config(text="Do You Want To HIT or STAND \nFor HAND 2?",font=("Times",11,"bold"))
      self.whatgon2.place(x = 345, y = 135)


      self.hand1_button.place(x = 5000, y = 145)
      self.hand2_button.place(x = 5090, y = 145)

      self.hand_label.place(x = 1809, y = 110)
      self.label_continue.place(x = 5950, y = 195)


      self.move()

      #give dealer cards
      self.dealer_points.append(random.randint(1,10))
      self.dealer_points.append(random.randint(1,10))

      #give player cards
      self.player_points.append(random.randint(1,10))
      self.player_points.append(random.randint(1,10))

      self.player2hand_points.append(random.randint(1,10))
      self.player2hand_points.append(random.randint(1,10))
      
      self.label_player.config(text="HAND 1:\n Your Cards are: %d and %d\nTotal: %d" % (self.player_points[0],self.player_points[1],sum(self.player_points)),font=("Times", 12,"italic"))
      self.label_player.place(x = 80, y = 0)


      self.label_player2hand.config(text="HAND 2:\n Your Cards are: %d and %d\nTotal: %d" % (self.player2hand_points[0],self.player2hand_points[1],sum(self.player2hand_points)),font=("Times", 12,"italic"))
      self.label_player2hand.place(x = 370, y = 0)


      self.label_dealer.config(text="Dealers Cards are: %d and *hidden*" % (self.dealer_points[0]),background = "white",font=("Times", 11,"italic"))
      self.label_dealer.place(x = 200, y = 85)

    
      
    def hit(self):
      #complete this function so it does the following:
      #add a new random number to self.player_points
      self.player_points.append(random.randint(1,10))

      #update label_player so it says something like "you drew x, your total is y"
      self.label_player.config(text="You Drew a: %d, Your Total is: %d" % (self.player_points[-1],sum(self.player_points)),font=("Times", 12,"italic"))
      self.label_player.place(x = 197, y = 0)
      self.label_dealer.place(x = 220, y = 30)


      
      if sum(self.player_points) > 21:
        root.after(2000)
        self.label_win.config(text="You Lose",font=("Times", 15,"italic"))
        self.label_win.place(x = 275, y = 57)
        self.deal_button.config(state='disabled')
        self.hit_button.config(state='disabled')
        self.stand_button.config(state='disabled')
        self.winnings.place(x = 200, y = 300)
        self.gamereset.place(x = 220, y = 332)
        root.after(4500,self.reset)

        

        
      #if sum(self.player_points) goes over 21:
      #    update label_win with a loss message
      """  
      
      call the self.reset() function AFTER 2 seconds (2000 milliseconds) 

      root.after(2000, self.reset)
      
      """
      pass
    def hit2hand1(self):
      #complete this function so it does the following:
      #add a new random number to self.player_points
      self.player_points.append(random.randint(1,10))

      #update label_player so it says something like "you drew x, your total is y"
      self.label_player.config(text="HAND 1:\nYou Drew a: %d\nYour Total is: %d" % (self.player_points[-1],sum(self.player_points)),font=("Times", 12,"italic"))
      self.label_player.place(x = 118, y = 0)


    
      if sum(self.player_points) > 21:
        root.after(2000)
        self.label_win.config(text="You Lost Hand 1",font=("Times", 15,"italic"))
        self.label_win.place(x = 100, y = 270)
        self.deal_button.config(state='disabled')
        self.hit2hand1_button.config(state='disabled')
        self.stand2hand1_button.config(state='disabled')
        self.hit2hand2_button.config(state='normal')
        self.stand2hand2_button.config(state='normal') 
        self.game += 1
      

        
     
    def hit2hand2(self):
      #complete this function so it does the following:
      #add a new random number to self.player_points
      self.player2hand_points.append(random.randint(1,10))

      #update label_player so it says something like "you drew x, your total is y"
      self.label_player2hand.config(text="HAND 2:\nYou Drew a: %d\nYour Total is: %d" % (self.player2hand_points[-1],sum(self.player2hand_points)),font=("Times", 12,"italic"))
      self.label_player2hand.place(x = 400, y = 0)



      if sum(self.player2hand_points) > 21:
        root.after(2000)
        self.labelplayer2hand_win.config(text="You Lost Hand 2",font=("Times", 15,"italic"))
        self.labelplayer2hand_win.place(x = 387, y = 270)
        self.deal_button.config(state='disabled')
        self.hit2hand2_button.config(state='disabled')
        self.stand2hand2_button.config(state='disabled') 
        if sum(self.player2hand_points) > 21 and sum(self.player_points) > 21:
          #use for money thing that says wow you won all of this or sm
          self.finalstuff.config(text="You Lost Both Hands\nThe Game Will Now Reset",font=("Times", 13,"italic"))
          self.finalstuff.place(x = 200, y = 352)
          root.after(6000,self.reset)
        else:  
          root.after(6000,self.dealer_hit2)
          self.game += 1

      if sum(self.player2hand_points) > 21 and sum(self.player_points) > 21:
        #use for money thing that says wow you won all of this or sm
        self.finalstuff.config(text="You Lost Both Hands And Have Won No Money!\nThe Game Will Now Reset...",font=("Times", 12,"italic"))
        self.finalstuff.place(x = 135, y = 332)
        root.after(6000,self.reset)
        

    def stand(self):
      self.deal_button.config(state='disabled')
      self.hit_button.config(state='disabled')
      self.stand_button.config(state='disabled')
      self.dealer_hit()

      # complete this function so it does the following:

      # disable all buttons (see line 42)

      # call the self.dealer_hit() function 
      pass
    def stand2hand1(self):
      self.hit2hand1_button.config(state='disabled')
      self.stand2hand1_button.config(state='disabled')
      self.hit2hand2_button.config(state='normal')
      self.stand2hand2_button.config(state='normal')
    def stand2hand2(self):
      self.hit2hand1_button.config(state='disabled')
      self.stand2hand1_button.config(state='disabled')
      self.hit2hand2_button.config(state='disabled')
      self.stand2hand2_button.config(state='disabled') 
      self.dealer_hit2()


    def dealer_hit(self):
      if sum(self.dealer_points) > sum(self.player_points) and sum(self.dealer_points)<= 21 or sum(self.dealer_points) == sum(self.player_points) and sum(self.dealer_points) <= 21:
        if len(self.dealer_points) == 2:
          self.label_dealer.config(text="The Dealer's Hidden Card was: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 143, y = 0)
        elif len(self.dealer_points) == 1:
          self.label_dealer.config(text="The Dealer's Card: %d, Total is: %d" % (self.dealer_points[0],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 178, y = 0)
        else:  
          self.label_dealer.config(text="Dealer drew a: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 203, y = 0)

        
        self.label_player.config(text="You Drew a: %d, Your Total is: %d" % (self.player_points[-1],sum(self.player_points)),font=("Times", 9,"italic"))
        self.label_player.place(x = 222, y = 30)


        
        self.label_win.config(text="Dealer Wins",font=("Times",14,"italic")) 
        self.label_win.place(x = 263, y = 57)
       
        self.winnings.place(x = 200, y = 300)
        self.gamereset.place(x = 220, y = 332)
        root.after(5000,self.reset)
    
      elif sum(self.dealer_points) > 21:
        root.after(2000)
        self.label_win.config(text="Dealer Busts",font=("Times",14,"italic"))
        self.label_win.place(x = 263, y = 57)

        self.hand1bet = self.hand1bet * 2
        self.winnings.config(text="You've Won $%d!"% self.hand1bet,font=("Times",13,"bold"))
        
        
        
        self.playertotal = self.playertotal + self.hand1bet

        self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
        self.winnings.place(x = 210, y = 300)
        self.gamereset.place(x = 220, y = 332)
        root.after(5000,self.reset)  

      else:
        self.dealer_points.append(random.randint(1,10))
        if len(self.dealer_points) == 2:
          self.label_dealer.config(text="The Dealer's Hidden Card was: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 143, y = 0)
          root.after(1000)
        else:  
          self.label_dealer.config(text="Dealer drew a: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 203, y = 0)

        
        self.label_player.config(text="You Drew a: %d, Your Total is: %d" % (self.player_points[-1],sum(self.player_points)),font=("Times", 9,"italic"))
        self.label_player.place(x = 222, y = 30)
 
        root.after(2000,self.dealer_hit)
      """    call the self.dealer_hit() function again after 2 seconds (2000 milliseconds)"""

      # NOTE i recommended 2 second intervals for the timers but you can choose whatever feels more comfortable
      # for your game

      pass

    def dealer_hit2(self):
      if sum(self.dealer_points) > sum(self.player_points) and sum(self.dealer_points)<= 21 or self.game < 2 or sum(self.dealer_points) == sum(self.player_points) and sum(self.dealer_points) <= 21 and self.game < 2:
        if len(self.dealer_points) == 2:
          self.label_dealer.config(text="The Dealer's Hidden Card was: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 130, y = 85)
        elif len(self.dealer_points) == 1:
          self.label_dealer.config(text="The Dealer's Card: %d, Total is: %d" % (self.dealer_points[0],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 130, y = 85)
        else:  
          self.label_dealer.config(text="Dealer drew a: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 200, y = 85)

        root.after(1000)
        self.label_win.config(text="Dealer Wins This Hand",font=("Times",14,"italic")) 
        self.label_win.place(x=92,y=270)
        root.after(1000)
        self.game += 1
        self.bust1 +=1
        if self.game == 2:
          self.playertotal = self.playertotal + self.winmoney
          self.finalstuff.config(text="You Have Won $%d\nThe Game Will Now Reset"%self.winmoney,font=("Times", 13,"italic"))
          self.finalstuff.place(x = 208, y = 332)
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
          root.after(8000,self.reset)
        


      if sum(self.dealer_points) > sum(self.player2hand_points) and sum(self.dealer_points)<= 21 and self.game < 2 or sum(self.dealer_points) == sum(self.player2hand_points) and sum(self.dealer_points) <= 21 and self.game < 2:
        if len(self.dealer_points) == 2:
          self.label_dealer.config(text="The Dealer's Hidden Card was: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 130, y = 85)
        elif len(self.dealer_points) == 1:
          self.label_dealer.config(text="The Dealer's Card: %d, Total is: %d" % (self.dealer_points[0],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 130, y = 85)
        else:  
          self.label_dealer.config(text="Dealer drew a: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 200, y = 85)

        root.after(1000)
        self.labelplayer2hand_win.config(text="Dealer Wins This Hand",font=("Times",14,"italic")) 
        self.labelplayer2hand_win.place(x = 387, y = 270)
        root.after(1000)
        self.game += 1
        self.bust2 +=1
        if self.game == 2:
          self.playertotal = self.playertotal + self.winmoney
          self.finalstuff.config(text="You Have Won $%d\nThe Game Will Now Reset"%self.winmoney,font=("Times", 13,"italic"))
          self.finalstuff.place(x = 208, y = 332)
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
          root.after(8000,self.reset)
        
    


      if sum(self.dealer_points) > 21 and sum(self.player_points) <= 21 and self.bust1 != 1 and self.game < 2:
        if len(self.dealer_points) == 2:
          self.label_dealer.config(text="The Dealer's Hidden Card was: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 130, y = 85)
        elif len(self.dealer_points) == 1:
          self.label_dealer.config(text="The Dealer's Card: %d, Total is: %d" % (self.dealer_points[0],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 130, y = 85)
        else:  
          self.label_dealer.config(text="Dealer drew a: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 200, y = 85)
        root.after(2000)
        self.label_win.config(text="Dealer Busts",font=("Times",14,"italic"))
        self.label_win.place(x=92,y=270)
        self.game += 1
        self.winmoney = self.winmoney + self.hand1bet * 2
        if self.game == 2:
          self.playertotal = self.playertotal + self.winmoney
          self.finalstuff.config(text="You Have Won $%d\nThe Game Will Now Reset"%self.winmoney,font=("Times", 13,"italic"))
          self.finalstuff.place(x = 208, y = 332)
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
          root.after(5000,self.reset)

      if sum(self.dealer_points) > 21 and sum(self.player2hand_points) <= 21 and self.bust2 != 1 and self.game < 2:
        if len(self.dealer_points) == 2:
          self.label_dealer.config(text="The Dealer's Hidden Card was: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 130, y = 85)
        elif len(self.dealer_points) == 1:
          self.label_dealer.config(text="The Dealer's Card: %d, Total is: %d" % (self.dealer_points[0],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 130, y = 85)
        else:  
          self.label_dealer.config(text="Dealer drew a: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
          self.label_dealer.place(x = 200, y = 85)
        root.after(2000)
        self.labelplayer2hand_win.config(text="Dealer Busts",font=("Times",14,"italic")) 
        self.labelplayer2hand_win.place(x = 387, y = 270)
        self.game += 1
        self.winmoney = self.winmoney + self.hand2bet * 2
        if self.game == 2:
          self.playertotal = self.playertotal + self.winmoney
          self.finalstuff.config(text="You Have Won $%d\nThe Game Will Now Reset"%self.winmoney,font=("Times", 13,"italic"))
          self.finalstuff.place(x = 208, y = 332)
          self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
          root.after(5000,self.reset)    

      else:
          if len(self.dealer_points) == 2:
            self.label_dealer.config(text="The Dealer's Hidden Card was: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
            self.label_dealer.place(x = 130, y = 85)
            root.after(1000)
          elif len(self.dealer_points) == 1:
            self.label_dealer.config(text="The Dealer's Card: %d, Total is: %d" % (self.dealer_points[0],sum(self.dealer_points)),font=("Times", 12,"italic"))
            self.label_dealer.place(x = 130, y = 85)
          else:  
            if self.game < 2:
              self.label_dealer.config(text="Dealer drew a: %d, Total is: %d" % (self.dealer_points[-1],sum(self.dealer_points)),font=("Times", 12,"italic"))
              self.label_dealer.place(x = 200, y = 85)
  
          self.dealer_points.append(random.randint(1,10))
          root.after(2000,self.dealer_hit2)
        

      
    def startover(self):
      self.playertotal = 10000
      self.yourtotal.config(text =  "Your Total Is: $%d" % self.playertotal,background="white", font=("Times",11,"italic"))
      root.after(2500)

      self.reset()
      


        

        
        

      
        
    def reset(self):
      self.hit_button.config(state='disabled')
      self.stand_button.config(state='disabled')
      self.deal_button.config(state='disabled')
      self.hand1_button.config(state='normal')
      self.hand2_button.config(state='normal')
      
      self.bet100hand1_button.config(state = 'disabled')  
      self.bet200hand1_button.config(state = 'disabled') 
      self.bet300hand1_button.config(state = 'disabled') 
      self.bet400hand1_button.config(state = 'disabled') 
      self.bet500hand1_button.config(state = 'disabled') 
      self.bet600hand1_button.config(state = 'disabled') 
      self.bet700hand1_button.config(state = 'disabled') 
      self.bet800hand1_button.config(state = 'disabled') 
      self.bet900hand1_button.config(state = 'disabled') 
      self.bet1000hand1_button.config(state = 'disabled') 

      self.bet100hand2_button.config(state = 'disabled')  
      self.bet200hand2_button.config(state = 'disabled') 
      self.bet300hand2_button.config(state = 'disabled') 
      self.bet400hand2_button.config(state = 'disabled') 
      self.bet500hand2_button.config(state = 'disabled') 
      self.bet600hand2_button.config(state = 'disabled') 
      self.bet700hand2_button.config(state = 'disabled') 
      self.bet800hand2_button.config(state = 'disabled') 
      self.bet900hand2_button.config(state = 'disabled') 
      self.bet1000hand2_button.config(state = 'disabled')
      self.stopbet1_button.config(state = 'disabled')
      self.stopbet2_button.config(state = 'disabled')
      self.startover_button.config(state='disabled')

      self.bet100hand1_button.place(x = 25, y = 150)
      self.bet200hand1_button.place(x = 90, y = 150)
      self.bet300hand1_button.place(x = 25, y = 185)
      self.bet400hand1_button.place(x = 90, y = 185)
      self.bet500hand1_button.place(x = 25, y = 220)
      self.bet600hand1_button.place(x = 90, y = 220)
      self.bet700hand1_button.place(x = 25, y = 255)
      self.bet800hand1_button.place(x = 90, y = 255)
      self.bet900hand1_button.place(x = 25, y = 290)
      self.bet1000hand1_button.place(x = 86, y = 290)
      self.bet100hand2_button.place(x = 505, y = 150)
      self.bet200hand2_button.place(x = 570, y = 150)
      self.bet300hand2_button.place(x = 505, y = 185)
      self.bet400hand2_button.place(x = 570, y = 185)
      self.bet500hand2_button.place(x = 505, y = 220)
      self.bet600hand2_button.place(x = 570, y = 220)
      self.bet700hand2_button.place(x = 505, y = 255)
      self.bet800hand2_button.place(x = 570, y = 255)
      self.bet900hand2_button.place(x = 505, y = 290)
      self.bet1000hand2_button.place(x = 566, y = 290)
      self.stopbet1_button.place(x = 22, y = 325)
      self.stopbet2_button.place(x = 501, y = 325)
      self.startover_Label.place(x = 2400, y = 400)

      self.player_points = []
      self.player2hand_points = []
      self.dealer_points = []

      self.game = 0
      self.bust1 = 0
      self.bust2 = 0
      self.hand1bet = 0
      self.hand2bet = 0
      self.hold = 0
      self.game = 0
      self.fixer = 0
      self.fixer2 = 0
      self.winmoney = 0

      self.label_player.config(text="~~~ BlackJack ~~~",font=("Times", 17,"italic"),background="white")
      self.label_player.place(x = 206, y = 0)
      
      self.label_dealer.config(text="By: Aaron and Raihan", background="white",font=("Times", 11,"italic"))
      
      self.label_dealer.place(x = 243, y = 41)

      self.hand_label.config(text="How Many Hands? (Max: 2)",background="white", font=("Times",13,"bold"))
      self.hand_label.place(x = 189, y = 110)

      self.playerhand1bet.config(text =  "You've bet $%d on Hand 1" % self.hand1bet,background="white", font=("Times",11,"italic"))
      self.playerhand2bet.config(text =  "You've bet $%d on Hand 2" % self.hand2bet,background="white", font=("Times",11,"italic"))
      self.playerhand2bet.place(x = 2000, y = 380)

      self.yourtotal.place(x = 20, y = 400)

      self.label_win.config(text="") 
      self.label_win.place(x = 5000, y = 57)

      self.whatgon.place(x = 5000, y = 57)
      self.whatgon2.place(x = 5000, y = 57)

   
      self.hit2hand1_button.place(x = 2150, y = 299)
      self.hit2hand2_button.place(x = 2150, y = 299)
      self.stand2hand1_button.place(x = 3400, y = 299)
      self.stand2hand2_button.place(x = 3400, y = 299)
      
      self.labelplayer2hand_win.place(x = 3400, y = 299)
      
      self.label_player2hand.place(x = 3400, y = 299)
      self.finalstuff.place(x = 3400, y = 299)

      self.deal_button.place(x = 281, y = 245)
      self.deal2_button.place(x = 2810, y = 245)

      self.hit_button.place(x = 215, y = 299)
      self.stand_button.place(x = 340, y = 299)


      self.hand1_button.place(x = 247, y = 165)
      self.hand2_button.place(x = 337, y = 165)

      self.hand_label.place(x = 189, y = 110)
      self.label_continue.place(x = 5950, y = 195)

      self.winnings.config(text="No Money Has Been Won",font=("Times",13,"bold"))
      
      self.winnings.place(x = 2000, y = 300)
      self.gamereset.place(x = 2200, y = 332)
      
      if self.playertotal == 0:
        self.hand1_button.config(state='disabled')
        self.hand2_button.config(state='disabled') 
        self.startover_Label.config(text = "You've Run Out Of Money!\nPress Start Over To Refill --->")
        self.startover_Label.place(x = 236, y = 383)
        self.startover_button.config(state ='normal')

    #disable the hit and stand buttons

    #enable the deal button

    #set self.player_points and self.dealer_points back to an empty list

    #set all labels back to a default message state, either blank or "Deal to Play!"

      pass

root = Tk()
my_gui = BabyBlackJack(root) #creates the BabyBlackJack instance
root.geometry("650x500")
root.mainloop()

"""
if sum(self.dealer_points) > sum(self.player_points) and sum(self.dealer_points) > sum(self.player2hand_points) and sum(self.dealer_points) <= 21
"""
