#!/usr/bin/env python

"""Demonstration on how to place arbitrary axes in the different backends."""

from scitools.all import *

x = linspace(0,1,51)
y1 = sin(2*pi*x)
y2 = cos(4*pi*x)

plot(x, y1, 'rd-', xlabel='x-axis', ylabel='y-axis', legend='test')

if backend == 'veusz':
    pos = [.64, .55, .1, .2]  # [leftMargin,bottomMargin,rightMargin,topMargin]
elif backend == 'gnuplot':
    pos = [.6, .52, .33, .33] # [left,bottom,width,height]
elif backend == 'grace':
    pos = [.6, .5, .8, .75]   # [xmin,ymin,xmax,ymax]
elif backend == 'matplotlib':
    pos = [.62, .56, .2, .2]  # [left,bottom,width,height]
elif backend == 'matlab':
    pos = [.62, .56, .2, .2]  # [left,bottom,width,height]
elif backend == 'matlab2':
    pos = [.62, .56, .2, .2]  # [left,bottom,width,height]
elif backend == 'pyx':
    # default figure size (i.e., [width,height]) is [15,9.27].
    pos = [9.6, 3.5, 4, 4]    # [xpos,ypos,width,height]
else:
    print "The '%s' backend has currently no support for placement of " \
          "arbitrary axes." % backend
    pos = None

if pos is not None:
    ax = axes(viewport=pos)  # create a new axis at the given position
    plot(ax, x, y2, 'b--')   # draw a curve in the new axis

hardcopy('axes1a.eps')
if not backend == 'pyx':
    hardcopy('axes1a.png')

if backend == 'matlab2':
    save('test_axes.m')
elif backend == 'veusz':
    save('test_axes.vsz')

raw_input('press enter to continue')