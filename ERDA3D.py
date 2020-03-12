from math import *
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

def visiblecheck(i,j,xguard,yguard,theta11,theta13,theta21,theta23,theta31,theta33,r11,r13,r21,r23,r31,r33):
    visible=1
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
    else:
        theta=0
          
    if theta<0:
        theta=theta+2*pi
        
    #check if r is greater than the corresponding point on the wall
    if theta11>=theta>=theta13 or theta13>=theta>=theta11:
        border1=r11*sin(theta11)/sin(theta)
        
        if r>border1:            
            visible=0
            
    elif theta21>=theta>=theta23 or theta23>=theta>=theta21:
        border2=r21*sin(theta21)/sin(theta)
        
        if r>border2:
            visible=0
        
    if (theta31>=theta>=theta33 or theta33>=theta>=theta31) and ((r31<r11)and(r33<r13)or(r31<r21)and(r33<r23)):
        border3=r31*sin(theta31)/sin(theta)
            
        if r>border3:
            visible=0
    
    return(visible)
            
#_____________________________________________________________________________________________
            
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

#__________________________________________________________________
#defining the edge points as a class

class importantpoint():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class guard():
    def __init__(self,x,y):
        self.x=x
        self.y=y
            
        self.r11=sqrt((point11.x-self.x)**2+(point11.y-self.y)**2)
        if self.r11>0:
            if point11.x-self.x>0:
                self.theta11=asin((point11.y-self.y)/self.r11)
            elif point11.x-self.x<0:
                self.theta11=-asin((point11.y-self.y)/self.r11)+pi
            elif (point11.x-self.x)==0:
                if point11.y-self.y>0:
                    self.theta11=pi/2
                elif point11.y-self.y<0:
                        self.theta11=3*pi/2
        elif self.r11==0:
            self.theta11=0
            
        if self.theta11<0:
            self.theta11=self.theta11+2*pi
            
            
        self.r13=sqrt((point13.x-self.x)**2+(point13.y-self.y)**2)
        if self.r13>0:
            if point13.x-self.x>0:
                self.theta13=asin((point13.y-self.y)/self.r13)
            elif point13.x-self.x<0:
                self.theta13=-asin((point13.y-self.y)/self.r13)+pi
            elif (point13.x-self.x)==0:
                if point13.y-self.y>0:
                    self.theta13=pi/2
                elif point13.y-self.y<0:
                        self.theta13=3*pi/2
        elif self.r13==0:
            self.theta13=0
            
        if self.theta13<0:
            self.theta13=self.theta13+2*pi
            
            
        self.r21=sqrt((point21.x-self.x)**2+(point21.y-self.y)**2)
        if self.r21>0:
            if point21.x-self.x>0:
                self.theta21=asin((point21.y-self.y)/self.r21)
            elif point21.x-self.x<0:
                self.theta21=-asin((point21.y-self.y)/self.r21)+pi
            elif (point21.x-self.x)==0:
                if point21.y-self.y>0:
                    self.theta21=pi/2
                elif point21.y-self.y<0:
                        self.theta21=3*pi/2
        elif self.r21==0:
            self.theta21=0
            
        if self.theta21<0:
            self.theta21=self.theta21+2*pi
            
            
        self.r23=sqrt((point23.x-self.x)**2+(point23.y-self.y)**2)
        if self.r23>0:
            if point23.x-self.x>0:
                self.theta23=asin((point23.y-self.y)/self.r23)
            elif point23.x-self.x<0:
                self.theta23=-asin((point23.y-self.y)/self.r23)+pi
            elif (point23.x-self.x)==0:
                if point23.y-self.y>0:
                    self.theta23=pi/2
                elif point23.y-self.y<0:
                        self.theta23=3*pi/2
        elif self.r23==0:
            self.theta23=0
            
        if self.theta23<0:
            self.theta23=self.theta23+2*pi
            
            
        self.r31=sqrt((point31.x-self.x)**2+(point31.y-self.y)**2)
        if self.r31>0:
            if point31.x-self.x>0:
                self.theta31=asin((point31.y-self.y)/self.r31)
            elif point31.x-self.x<0:
                self.theta31=-asin((point31.y-self.y)/self.r31)+pi
            elif (point31.x-self.x)==0:
                if point31.y-self.y>0:
                    self.theta31=pi/2
                elif point31.y-self.y<0:
                        self.theta31=3*pi/2
        elif self.r31==0:
            self.theta31=0
            
        if self.theta31<0:
            self.theta31=self.theta31+2*pi
            
            
        self.r33=sqrt((point33.x-self.x)**2+(point33.y-self.y)**2)
        if self.r33>0:
            if point33.x-self.x>0:
                self.theta33=asin((point33.y-self.y)/self.r33)
            elif point33.x-self.x<0:
                self.theta33=-asin((point33.y-self.y)/self.r33)+pi
            elif (point33.x-self.x)==0:
                if point33.y-self.y>0:
                    self.theta33=pi/2
                elif point33.y-self.y<0:
                        self.theta33=3*pi/2
        elif self.r33==0:
            self.theta33=0
            
        if self.theta33<0:
            self.theta33=self.theta33+2*pi
        
        
#________________________________________________________________________
#edge points
            
#first line left below
        
point11=importantpoint(0/par,1040/par)
point13=importantpoint(4160/par,1040/par)
#second line right below
point21=importantpoint(27840/par,1040/par)
point23=importantpoint(32000/par,1040/par)
#upper line
point31=importantpoint(8664/par,4621/par)
point33=importantpoint(23336/par,4621/par)

#guards
G1=guard(10500/par,700/par)
G2=guard(500/par,5700/par)
G3=guard(16000/par,700/par)
G4=guard(27000/par,2700/par)

#______________________________________________________________________

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
        
        scr.set_at((int(i/xmax*xmaxscr),int(j/xmax*xmaxscr)),red)
        b=b+1
        
        vis1=visiblecheck(i,j,G1.x,G1.y,G1.theta11,G1.theta13,G1.theta21,G1.theta23,G1.theta31,G1.theta33,G1.r11,G1.r13,G1.r21,G1.r23,G1.r31,G1.r33)
        vis2=visiblecheck(i,j,G2.x,G2.y,G2.theta11,G2.theta13,G2.theta21,G2.theta23,G2.theta31,G2.theta33,G2.r11,G2.r13,G2.r21,G2.r23,G2.r31,G2.r33)
        vis3=visiblecheck(i,j,G3.x,G3.y,G3.theta11,G3.theta13,G3.theta21,G3.theta23,G3.theta31,G3.theta33,G3.r11,G3.r13,G3.r21,G3.r23,G3.r31,G3.r33)
        vis4=visiblecheck(i,j,G4.x,G4.y,G4.theta11,G4.theta13,G4.theta21,G4.theta23,G4.theta31,G4.theta33,G4.r11,G4.r13,G4.r21,G4.r23,G4.r31,G4.r33)
         
        if (vis1+vis2+vis3+vis4)>=1:
            scr.set_at((int(i/xmax*xmaxscr),int(j/xmax*xmaxscr)),green)
            c=c+1
        
        
       
            
#____________________________________________________________________________________
pg.draw.line(scr,black,(int(point11.x/xmax*xmaxscr),int(point11.y/ymax*ymaxscr)),(int(point13.x/xmax*xmaxscr),int(point13.y/ymax*ymaxscr)))
pg.draw.line(scr,black,(int(point21.x/xmax*xmaxscr),int(point21.y/ymax*ymaxscr)),(int(point23.x/xmax*xmaxscr),int(point23.y/ymax*ymaxscr)))
pg.draw.line(scr,black,(int(point31.x/xmax*xmaxscr),int(point31.y/ymax*ymaxscr)),(int(point33.x/xmax*xmaxscr),int(point33.y/ymax*ymaxscr)))
pg.draw.circle(scr,black,(int(G1.x/xmax*xmaxscr),int(G1.y/ymax*ymaxscr)),int(3000/xmaxscr))
pg.draw.circle(scr,black,(int(G2.x/xmax*xmaxscr),int(G2.y/ymax*ymaxscr)),int(3000/xmaxscr))
pg.draw.circle(scr,black,(int(G3.x/xmax*xmaxscr),int(G3.y/ymax*ymaxscr)),int(3000/xmaxscr))
pg.draw.circle(scr,black,(int(G4.x/xmax*xmaxscr),int(G4.y/ymax*ymaxscr)),int(3000/xmaxscr))

pg.display.flip()
pg.event.pump()
close = closescr()

print("the area visible is", ((c/b))*100, "procent")



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
