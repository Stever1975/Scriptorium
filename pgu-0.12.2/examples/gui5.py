"""<title>Tables, Widgets, and Groups!</title>
An example of tables and most of the included widgets.
"""

import pygame
from pygame.locals import *

# the following line is not needed if pgu is installed
import sys; sys.path.insert(0, "..")

from pgu import gui

app = gui.Desktop()
app.connect(gui.QUIT,app.quit,None)

##The table code is entered much like HTML.
##::
c = gui.Table()


c.tr()
c.td(gui.Label("Gui Widgets"),colspan=4)

c.tr()
c.td(gui.Label("Button"))
c.td(gui.Button("Click Me!"),colspan=3)
##

c.tr()
c.td(gui.Label("Switch"))
c.td(gui.Switch(False),colspan=3)

c.tr()
c.td(gui.Label("Checkbox"))
##Note how Groups are used for Radio buttons, Checkboxes, and Tools.
##::
g = gui.Group(value=[1,3])
c.td(gui.Checkbox(g,value=1))
c.td(gui.Checkbox(g,value=2))
c.td(gui.Checkbox(g,value=3))
##

c.tr()
c.td(gui.Label("Radio"))
g = gui.Group()
c.td(gui.Radio(g,value=1))
c.td(gui.Radio(g,value=2))
c.td(gui.Radio(g,value=3))

c.tr()
c.td(gui.Label("Select"))
e = gui.Select()
e.add("Goat",'goat')
e.add("Horse",'horse')
e.add("Dog",'dog')
e.add("Pig",'pig')
c.td(e,colspan=3)

c.tr()
c.td(gui.Label("Tool"))
g = gui.Group(value='b')
c.td(gui.Tool(g,gui.Label('A'),value='a'))
c.td(gui.Tool(g,gui.Label('B'),value='b'))
c.td(gui.Tool(g,gui.Label('C'),value='c'))

c.tr()
c.td(gui.Label("Input"))
c.td(gui.Input(value='Cuzco',size=8),colspan=3)

c.tr()
c.td(gui.Label("Slider"))
c.td(gui.HSlider(value=23,min=0,max=100,size=20,height=16,width=120),colspan=3)

c.tr()
c.td(gui.Label("Keysym"))
c.td(gui.Keysym(),colspan=3)

app.run(c)
