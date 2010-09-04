#!/usr/bin/env python

from dMap import *
startx=80
starty=40
Rmap= dMap()
Rmap.makeMap(startx,starty,110,50,60) 

def PlacePlayer(map):
    for x in range(startx):
        for y in range(starty):
            if map.mapArr[x][y]==0:
                return [x,y]





def displayLocalMap(map,pos):
    for y in range(starty):
            line = ""
            for x in range(startx):
                    if pos[0]==x and pos[1]==y:
                            line += "P"
                    else:
                        if map.mapArr[y][x]==0:
                                line += "."
                        if map.mapArr[y][x]==1:
                                line += " "
                        if map.mapArr[y][x]==2:
                                line += "#"
                        if map.mapArr[y][x]==3 or map.mapArr[y][x]==4 or map.mapArr[y][x]==5:
                                line += "="
            print line


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
    if map.mapArr[x][y]==0:
        return 1
    else:
        return 0

def movePlayer(direction,pos):
    x=pos[0]
    y=pos[1]
    if direction=="l":
       return [x-1,y]
    elif direction=="r":
       return [x+1,y]
    elif direction=="u":
       return [x,y-1]
    elif direction=="d":
       return [x,y+1]


