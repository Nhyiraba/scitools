#!/usr/bin/env python

# Example taken from:
# http://www.mathworks.fr/access/helpdesk/help/techdoc/visualize/f5-3558.html

import os
os.environ['EASYVIZ_BACKEND'] = 'vtk_'

from time import sleep
from scitools.easyviz import *

# Investigate the Data:
x,y,z,v = flow()

xmin = arrmin(x)
ymin = arrmin(y) 
zmin = arrmin(z)

xmax = arrmax(x) 
ymax = arrmax(y) 
zmax = arrmax(z)

set(show=False)

# Create a Slice Plane at an Angle to the X-Axes:
hslice = surf(linspace(xmin,xmax,100),
              linspace(ymin,ymax,100),
              zeros((100,100)))

#rotate(hslice,[-1,0,0],-45)
xd = hslice.get('xdata')
yd = hslice.get('ydata')
zd = hslice.get('zdata')
#delete(hslice)

# Draw the Slice Planes:
#h = slice_(x,y,z,v,xd,yd,zd)
h = slice_(x,y,z,v,[],[],0)
h.set(diffuse=.8)
#h.set('FaceColor','interp',
#      'EdgeColor','none',
#      'DiffuseStrength',.8)

hold('on')
#hx = slice_(x,y,z,v,xmax,[],[])
hx = slice_(x,y,z,v,xmax-0.001,[],[])
#set(hx,'FaceColor','interp','EdgeColor','none')

hy = slice_(x,y,z,v,[],ymax,[])
#set(hy,'FaceColor','interp','EdgeColor','none')

#hz = slice_(x,y,z,v,[],[],zmin)
hz = slice_(x,y,z,v,[],[],zmin+0.001)
#set(hz,'FaceColor','interp','EdgeColor','none')

# Define the View:
daspect([1,1,1])
box('on')
grid('off')
view(-38.5,16)
#camzoom(1.4)
camproj('perspective')

# Add Lighting and Specify Colors:
shading('interp')
colormap(jet(24))
#lightangle(-45,45)

set(show=True)
show()
sleep(3)