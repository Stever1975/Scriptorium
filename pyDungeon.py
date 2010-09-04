#!/usr/bin/env python
import pygame, sys, random
from pygame.locals import *
from dMap import *
from Player import *
from pgu import text
from pgu import gui
from Enemy import *
from Item import *
from functions import *



showInventory=False
npcs=[]
Inventory=[]
items=[]
gameState=0
Rmap= dMap()
Rmap.makeMap(startx,starty,110,50,60)
pos=PlacePlayer(Rmap)
guy=Player()
guy.x=pos[0]
guy.y=pos[1]
npcs=generateList(Rmap,npcs,Enemy,.09)
Rmap=PlaceList(Rmap,npcs,9)
attack=False
items=generateList(Rmap,items,Item,.07)
Rmap=PlaceList(Rmap,items,6)

def restart2():
    global showInventory,npcs,Rmap,gameState,guy
    print "hello"
    showInventory=False
    npcs=[]
    Inventory=[]
    items=[]
    gameState=0
    Rmap= dMap()
    Rmap.makeMap(startx,starty,110,50,60)
    pos=PlacePlayer(Rmap)
    #guy=Player()
    guy.life=100
    guy.x=pos[0]
    guy.y=pos[1]
    npcs=generateList(Rmap,npcs,Enemy,.09)
    Rmap=PlaceList(Rmap,npcs,9)
    attack=False
    items=generateList(Rmap,items,Item,.07)
    Rmap=PlaceList(Rmap,items,6)


# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = block_size*50
WINDOWHEIGHT = block_size*40
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Scriptorium')
player = pygame.Rect(300, 100, 50, 50)

while True:
    for event in pygame.event.get():
        direction=""
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_SPACE:
                restart2()
            if event.key == K_LEFT:
                direction="l"
                if pygame.key.get_mods() & pygame.KMOD_RSHIFT == pygame.KMOD_RSHIFT:
                    attack=True
                    print "hey"
                else:
                    moveRight = False
                    moveLeft = True
            if event.key == K_RIGHT:
                if pygame.key.get_mods() & pygame.KMOD_RSHIFT == pygame.KMOD_RSHIFT:
                    attack=True
                    print "hey"
                else:
                    moveLeft = False
                    moveRight = True
                    direction="r"
            if event.key == K_UP:
                direction="u"
                if pygame.key.get_mods() & pygame.KMOD_RSHIFT == pygame.KMOD_RSHIFT:
                    attack=True
                    print "hey"
                else:
                    moveDown = False
                    moveUp = True
            if event.key == K_DOWN:
                direction="d"
                if pygame.key.get_mods() & pygame.KMOD_RSHIFT == pygame.KMOD_RSHIFT:
                    attack=True
                    print "hey"
                else:
                    moveUp = False
                    moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_SPACE:
                restart2()
                print "restart"
            if event.key == K_LEFT: 
                moveLeft = False
                direction="l"
            if event.key == K_RIGHT: 
                moveRight = False
                direction="r"
            if event.key == K_UP:
                moveUp = False
                direction="u"
            if event.key == K_DOWN:
                moveDown = False
                direction="d"
            if event.key == K_i:
                if showInventory==True:
                    showInventory=False
                else:
                    showInventory=True
            if event.key in [K_DOWN,K_UP,K_RIGHT,K_LEFT]:
                npcs=enemyUpdate(Rmap,npcs,guy)
            if attack==True:
                attackEnemy(direction,npcs,guy)
                
            new_position=movePlayer(direction,guy)
            if validMove(Rmap,new_position[0],new_position[1]):
                pos=new_position
                guy.x=pos[0]
                guy.y=pos[1]
                CollisionList(Rmap,npcs,guy)
                CollisionList(Rmap,items,guy)
    CleanMap(Rmap)
    Rmap=PlaceList(Rmap,npcs,9)
    Rmap=PlaceList(Rmap,items,6)

    windowSurface.fill(BLACK)
    drawDungeon(Rmap,guy)
    if showInventory==True:
        DisplayInventory(guy)
    DisplayVitals(guy)
    font = pygame.font.SysFont("default", 24)
    bg = (255,255,255)
    text.write(windowSurface,font,(0,0),bg,"Hello World!")
    gameState=checkGameState(guy,npcs,items)
    
    pygame.display.update()
    mainClock.tick(40)