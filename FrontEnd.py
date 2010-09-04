#!/usr/bin/env python
import msvcrt


from main import *
pos=PlacePlayer(Rmap)
print "hey"
print pos
control=1
while control:
    command =msvcrt.getch()
    if command  == chr(27):
        control = 0
    else:
        if command in ["l","d","r","u"]:
            position=movePlayer(command,pos)
            if validMove(Rmap,position[0],position[1]):
                pos=position
                print pos
                displayLocalMap(Rmap,position)
            else:
                print pos
                displayLocalMap(Rmap,position)
            