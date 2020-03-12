from math import *
import numpy as np
import pygame as pg

def closescr():
    keys = pg.key.get_pressed()
    # Check for quit event (closing of window)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
    # Escape key check
    if keys[pg.K_ESCAPE]:
        pg.quit()

def initscr(xmaxscr,ymaxscr):
    # Define a pygame window
    reso = (xmaxscr,ymaxscr)
    scr = pg.display.set_mode(reso)
    # Fill screen with white
    #white = (255,255,255)
    #scr.fill(white)
    pg.display.set_caption("My Game of Life")
    return scr

def show(board):
    flip = pg.display.flip()
    return True
# Make board
par=10 
xmax=32000/par
ymax=6000/par

# Initiate screen of x,y pixels
pg.init()
xmaxscr = 800
ymaxscr = 150
scr = initscr(xmaxscr,ymaxscr)

#position of the guard (cannot coincide with any of the important points)
xguard=10000/par
yguard=3000/par

#__________________________________________________________________
#defining the edge points as a class

class importantpoint():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.r=sqrt((x-xguard)**2+(y-yguard)**2)
        if self.r>0:
            if self.x-xguard>0:
                self.theta=asin((self.y-yguard)/self.r)
            elif self.x-xguard<0:
                self.theta=-asin((self.y-yguard)/self.r)+pi
            elif (self.x-xguard)==0:
                if self.y-yguard>0:
                    self.theta=pi/2
                elif self.y-yguard<0:
                        self.theta=3*pi/2
        elif self.r==0:
            self.theta=0
            
        if self.theta<0:
            self.theta=self.theta+2*pi
        

#________________________________________________________________________
#edge points
            
#first line left below
point11=importantpoint(0/par,1040/par)
point12=importantpoint(2080/par,1040/par)
point13=importantpoint(4160/par,1040/par)
#second line right below
point21=importantpoint(27840/par,1040/par)
point22=importantpoint(29920/par,1040/par)
point23=importantpoint(32000/par,1040/par)
#upper line
point31=importantpoint(8664/par,4621/par)
point32=importantpoint(16000/par,4621/par)
point33=importantpoint(23336/par,4621/par)

#______________________________________________________________________
#defining formulas
#lower left line
arr1=np.array([1,(point11.theta),(point11.theta)**2])
arr2=np.array([1,(point12.theta),(point12.theta)**2])
arr3=np.array([1,(point13.theta),(point13.theta)**2])
arr=np.array([arr1,arr2,arr3])
invarr=np.linalg.inv(arr)
finalarr1=np.dot(invarr,[point11.r,point12.r,point13.r])

#lower right line
arr1=np.array([1,(point21.theta),(point21.theta)**2])
arr2=np.array([1,(point22.theta),(point22.theta)**2])
arr3=np.array([1,(point23.theta),(point23.theta)**2])
arr=np.array([arr1,arr2,arr3])
invarr=np.linalg.inv(arr)
finalarr2=np.dot(invarr,[point21.r,point22.r,point23.r])

#upper line
arr1=np.array([1,(point31.theta),(point31.theta)**2])
arr2=np.array([1,(point32.theta),(point32.theta)**2])
arr3=np.array([1,(point33.theta),(point33.theta)**2])
arr=np.array([arr1,arr2,arr3])
invarr=np.linalg.inv(arr)
finalarr3=np.dot(invarr,[point31.r,point32.r,point33.r])

# Define colors and draw white screen
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
scr.fill(white)

b=0
c=0
#____________________________________________________________________________
#checking every point
for i in range(int(xmax)):
    for j in range(int(ymax)):
        b=b+1
        diffx=i-xguard
        diffy=j-yguard
        r=sqrt(diffx**2+diffy**2)
        
        #checking theta
        if r>0:
            if diffx>0:
                theta=asin(diffy/r)
            elif diffx<0:
                theta=-asin(diffy/r)+pi
            elif diffx==0:
                if diffy>0:
                    theta=pi/2
                elif diffy<0:
                    theta=3*pi/2
        if theta<0:
            theta=theta+2*pi
            
        #using the formulas to check if r is greater
        if point11.theta>=theta>=point13.theta or point13.theta>=theta>=point11.theta:
            border=finalarr1[0]+finalarr1[1]*theta+finalarr1[2]*theta*theta
            if r>border:
                c=c+1
                scr.set_at((int(i/xmax*xmaxscr),int(j/xmax*xmaxscr)),red)
                #surface.fill(color, (pos, (1, 1)))
            else:
                scr.set_at((int(i/xmax*xmaxscr),int(j/xmax*xmaxscr)),green)
        elif point21.theta>=theta>=point23.theta or point23.theta>=theta>=point21.theta:
            border=finalarr2[0]+finalarr2[1]*theta+finalarr2[2]*theta*theta
            if r>border:
                c=c+1
                scr.set_at((int(i/xmax*xmaxscr),int(j/xmax*xmaxscr)),red)
            else:
                scr.set_at((int(i/xmax*xmaxscr),int(j/xmax*xmaxscr)),green)

            
        elif point31.theta>=theta>=point33.theta or point33.theta>=theta>=point31.theta:
            border=finalarr3[0]+finalarr3[1]*theta+finalarr3[2]*theta*theta
            if r>border:
                c=c+1
                scr.set_at((int(i/xmax*xmaxscr),int(j/xmax*xmaxscr)),red)
            else:
                scr.set_at((int(i/xmax*xmaxscr),int(j/xmax*xmaxscr)),green)

        else:
            scr.set_at((int(i/xmax*xmaxscr),int(j/xmax*xmaxscr)),green)
            

pg.draw.line(scr,black,(int(point11.x/xmax*xmaxscr),int(point11.y/ymax*ymaxscr)),(int(point13.x/xmax*xmaxscr),int(point13.y/ymax*ymaxscr)))
pg.draw.line(scr,black,(int(point21.x/xmax*xmaxscr),int(point21.y/ymax*ymaxscr)),(int(point23.x/xmax*xmaxscr),int(point23.y/ymax*ymaxscr)))
pg.draw.line(scr,black,(int(point31.x/xmax*xmaxscr),int(point31.y/ymax*ymaxscr)),(int(point33.x/xmax*xmaxscr),int(point33.y/ymax*ymaxscr)))
pg.draw.circle(scr,black,(int(xguard/xmax*xmaxscr),int(yguard/ymax*ymaxscr)),int(3000/xmaxscr))

pg.display.flip()
pg.event.pump()
close = closescr()

print("the area visible is", (1-(c/b))*100, "procent")



# Screen loop
#running = pg.display.flip()
#while running:
 #   scr.fill(white)

    # Draw lines
  #  pg.draw.line(scr,black,
    
            
    # Show board with pattern
   # show(board)
    # Event pump
    #pg.event.pump()

    # Close screen when escape or cross is pressed
    #close = closescr()
