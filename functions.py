#!/usr/bin/env python
import pygame, sys, random
from pygame.locals import *
from Enemy import *
from Item import *
from dMap import *
block_size=16

startx=40
starty=40
Rmap= dMap()
Rmap.makeMap(startx,starty,110,50,60)
RED = ( 255,0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
EH = (50, 100, 0)
BLACK = (0, 0, 0)
# set up the window
WINDOWWIDTH = block_size*40
WINDOWHEIGHT = block_size*40
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

def checkGameState(player,lst_npcs,lst_items):
    if player.life<=0:
        DisplayGameOver()
        return 3
    return 0


def DisplayGameOver():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", 1, (10, 255, 10))
    textpos = text.get_rect(centerx=windowSurface.get_width()/2)
    windowSurface.fill(BLACK)
    windowSurface.blit(text, textpos)


def DisplayVitals(player):
    font = pygame.font.Font(None, 18)
    text = font.render("Life:" + str(player.life), 1, (10, 255, 10))
    textpos = text.get_rect(centerx=windowSurface.get_width()-100)
    windowSurface.blit(text, textpos)
    
        
def DisplayInventory(player,type):
    cntInventory=0
    font = pygame.font.Font(None, 18)
    txtInventory=""
    text_y=100
    text = font.render("Inventory:", 1, (10, 255, 10))
    textpos = text.get_rect(centerx=windowSurface.get_width()-100,centery=text_y)
    windowSurface.blit(text, textpos)
    for item in player.Inventory:
        cntInventory=cntInventory+1
        txtInventory=item.desc
        print txtInventory
        text_y=text_y+18
        #text = font.render("Life:" + str(player.life), 1, (10, 255, 10))
        text = font.render("[" + str(cntInventory) + "]" + txtInventory, 1, (10, 255, 10))
        textpos = text.get_rect(centerx=windowSurface.get_width()-100,centery=text_y)
        windowSurface.blit(text, textpos)

def drawDungeon(arr,player):
    arr_height=len(arr.mapArr)
    arr_width=len(arr.mapArr[0])
    for y in range(arr_height):
            for x in range(arr_width):
                block = pygame.Rect(block_size*y, block_size*x,block_size, block_size)
                if arr.mapArr[y][x]==2:
                    pygame.draw.rect(windowSurface, WHITE, block)
                if y==player.x and x==player.y:
                    pygame.draw.rect(windowSurface, GREEN, block)
                if arr.mapArr[y][x]==9:
                    pygame.draw.rect(windowSurface, RED, block)
                if arr.mapArr[y][x]==6:
                    pygame.draw.rect(windowSurface,EH, block)

def attackEnemy(direction,lst,player):
    pos=movePlayer(direction,player)
    for e in lst:
        if e.x==pos[0] and  e.y==pos[1]:
            lst.remove(e)
            
def CleanMap(map):
    for x in range(startx):
        for y in range(starty):
            if map.mapArr[x][y]!=2:
                map.mapArr[x][y]=1
                
                
def PlacePlayer(map):
    for x in range(startx):
        for y in range(starty):
            if map.mapArr[x][y]==0:
                return [x,y]

def enemyUpdate(map,lst,player):
    lst_new=[]
    for e in lst:
        delta=lineOfSight(map,e,player)
        x=e.x+delta[0]
        y=e.y+delta[1]
        e.lastSighted=[x,y] # hmmm...
        if [delta[0],delta[1]]!=[0,0]:
            e.visible=True
        if player.x==x and player.y==y:
            attackPlayer(player)
        elif validMove(map,x,y):
            e.x=x
            e.y=y
        lst_new.append(e)
    return lst_new

def attackPlayer(player):
    player.life=player.life-5
    print player.life

def lineOfSight(map,obj1,obj2):
    """Returns relative cardinal direction if in line of sight
    otherwise returns [0,0] """
    if obj1.x==obj2.x:
        if obj1.y>obj2.y:
            for e in range(obj2.y,obj1.y):
                if  map.mapArr[obj1.x][e]==2:
                    return [0,0]
            return [0,-1]
        else:
            for e in range(obj1.y,obj2.y):
                if  map.mapArr[obj1.x][e]==2:
                    return [0,0]
            return [0,1]
    if obj1.y==obj2.y:
        if obj1.x>obj2.x:
            for e in range(obj2.x,obj1.x):
                if  map.mapArr[e][obj1.y]==2:
                    return [0,0]
            return [-1,0]
        else:
            for e in range(obj1.x,obj2.x):
                if  map.mapArr[e][obj1.y]==2:
                    return [0,0]
            return [1,0]   
    return [0,0]

def generateList(map,lst,obj,prob):
    for x in range(startx):
        for y in range(starty):
            if map.mapArr[x][y]==0 and random()<prob:
                e=obj()
                e.x,e.y=x,y
                lst.append(e)
    return lst
def CollisionList(map,lst,player):
    for e in lst:
        if e.x==player.x and  e.y==player.y:
            print type(e)
            if isinstance(e,Item): 
                player.addInventory(e)
                lst.remove(e)
            return 1
    return 0

def PlaceList(map,lst,num):
    for e in lst:
        if e.visible==True:
            x,y=e.x,e.y
            map.mapArr[x][y]=num
    return map


def displayMap(map):
    for y in range(starty):
            line = ""
            for x in range(startx):
                    if map.mapArr[y][x]==0:
                            line += "."
                    if map.mapArr[y][x]==1:
                            line += " "
                    if map.mapArr[y][x]==2:
                            line += "#"
                    if map.mapArr[y][x]==3 or map.mapArr[y][x]==4 or map.mapArr[y][x]==5:
                            line += "="
            print line
displayMap(Rmap)


def validMove(map,x,y):
    if map.mapArr[x][y]!=2:
        return 1
    else:
        return 0

def movePlayer(direction,player):
    x=player.x
    y=player.y
    if direction=="l":
       return [x-1,y]
    elif direction=="r":
       return [x+1,y]
    elif direction=="u":
       return [x,y-1]
    elif direction=="d":
       return [x,y+1]
    else:
        return [x,y]
    
