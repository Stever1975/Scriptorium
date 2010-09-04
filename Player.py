#!/usr/bin/env python

class Player:
    x=0
    y=0
    Inventory=[]
    life=100
    gold=0
    armed=""
    inHand=""
    
    def addInventory(self,e):
        if e.desc=="gold":
            self.gold=self.gold+1
        else:
            self.Inventory.append(e)
        print self.Inventory
        
