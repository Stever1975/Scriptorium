#!/usr/bin/env python

from numpy import *
from random import *
from math import *
size=100
rooms=[]
mapArr=ones((size,size))

def makeRoom():
    width=randrange(10)+3
    height=randrange(10)+3
    return width,height

def placeRoom(width,height):
    failed=0
    RoomMade=0
    while RoomMade==0 and failed<10:
        x=randrange(size-1)
        y=randrange(size-1)
        for cnt in range(x,x+width):
            if failed>0:
                break
            for cnty in range(y,y+height):
                print cnt,cnty
                if  (size<=(y+height) or size<=(x+width)) or mapArr[cnt] [cnty]==0:
                    failed=+1
                    print failed
                    break    
        if failed==0:    
            for cnt in range(x,x+width):
                for cnty in range(y,y+height):
                    mapArr[cnt] [cnty]=0
            RoomMade=1
            rooms.append([x,y,width,height])
            print rooms

def makeCorridor(lst):
    
    pass

def displayLocalMap(map,pos):
    for y in range(size):
            line = ""
            for x in range(size):
                    if pos[0]==x and pos[1]==y:
                            line += "P"
                    else:
                        if mapArr[y][x]==0:
                                line += "."
                        if mapArr[y][x]==1:
                                line += "#"
            print line
for x in range(15): 
    width,height=makeRoom()
    placeRoom(width,height)
    
displayLocalMap(mapArr,[0,1])
