from math import *
import pygame as pg
import random

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
    
    
def moveforward(guard):
    firstloc=guard.y
    guard.y=guard.y+1000/par
    if 40/par<=firstloc<=1039/par and ((0/par<=guard.x<=4160/par)or(278400/par<=guard.x<=32000/par)):
        guard.y=1039/par
    if 3621/par  <=firstloc<=4620/par and (8664/par<=guard.x<=23336/par):
        guard.y=4620/par
    if guard.y>5999/par:
        guard.y=5999/par
        
def moveleft(guard):
    firstloc=guard.x
    guard.x=guard.x-1000/par
    if guard.x<0/par:
        guard.x=1/par
    
        
def moveright(guard):
    firstloc=guard.x
    guard.x=guard.x+1000/par
    if guard.y>31999/par:
        guard.y=31999/par
    
    
        
def moveback(guard):
    
    firstloc=guard.y
    
    guard.y=guard.y-1000/par
    if 1041/par<=firstloc<=2040/par and ((0/par<=guard.x<=4160/par)or(278400/par<=guard.x<=32000/par)):
        guard.y=1041/par
    elif 4622/par<=firstloc<=5621/par and (8664/par<=guard.x<=23336/par):
        guard.y=4622/par
    elif guard.y<0/par:
        guard.y=0/par
        
        
def moving():
    global c
    for i in moves:
        (G1.x,G1.y)=guard1start
        (G2.x,G2.y)=guard2start
        (G3.x,G3.y)=guard3start
        (G4.x,G4.y)=guard4start
        
        if i.digits12=='00':
            moveforward(G1)
        elif i.digits12=='01':
            moveleft(G1)
        elif i.digits12=='10':
            moveright(G1)
        elif i.digits12=='11':
            moveback(G1)
            
        if i.digits34=='00':
            moveforward(G2)
        elif i.digits34=='01':
            moveleft(G2)
        elif i.digits34=='10':
            moveright(G2)
        elif i.digits34=='11':
            moveback(G2)
            
        if i.digits56=='00':
            moveforward(G3)
        elif i.digits56=='01':
            moveleft(G3)
        elif i.digits56=='10':
            moveright(G3)
        elif i.digits56=='11':
            moveback(G3)
            
        if i.digits78=='00':
            moveforward(G4)
        elif i.digits78=='01':
            moveleft(G4)
        elif i.digits78=='10':
            moveright(G4)
        elif i.digits78=='11':
            moveback(G4)
            
        c=0
        G1.randtheta()
        G2.randtheta()
        G3.randtheta()
        G4.randtheta()
            
        for h in range(int(xmax)):
            for j in range(int(ymax)):
                
                scr.set_at((int(h/xmax*xmaxscr),int(j/xmax*xmaxscr)),red)
                
                
                vis1=visiblecheck(h,j,G1.x,G1.y,G1.theta11,G1.theta13,G1.theta21,G1.theta23,G1.theta31,G1.theta33,G1.r11,G1.r13,G1.r21,G1.r23,G1.r31,G1.r33)
                vis2=visiblecheck(h,j,G2.x,G2.y,G2.theta11,G2.theta13,G2.theta21,G2.theta23,G2.theta31,G2.theta33,G2.r11,G2.r13,G2.r21,G2.r23,G2.r31,G2.r33)
                vis3=visiblecheck(h,j,G3.x,G3.y,G3.theta11,G3.theta13,G3.theta21,G3.theta23,G3.theta31,G3.theta33,G3.r11,G3.r13,G3.r21,G3.r23,G3.r31,G3.r33)
                vis4=visiblecheck(h,j,G4.x,G4.y,G4.theta11,G4.theta13,G4.theta21,G4.theta23,G4.theta31,G4.theta33,G4.r11,G4.r13,G4.r21,G4.r23,G4.r31,G4.r33)
                 
                if (vis1+vis2+vis3+vis4)>=1:
                    scr.set_at((int(h/xmax*xmaxscr),int(j/xmax*xmaxscr)),green)
                    c=c+1
        
        result=c
        results.append(result)            
        
def comparemoves():  
    for j in range(len(results)):
        d=0
        for k in range(len(results)):
            if results[j]<=results[k]:
                d=d+1
        if d>=3:
            moves.pop(moves.index(moves[j]))
            moves.insert(j,0)
            results.pop(results.index(results[j]))
            results.insert(j,0)
            
    for i in range(3):
        results.pop(results.index(0))
        moves.pop(moves.index(0))
        
def comparemovestoone():
    for j in range(len(results)):
        d=0
        for k in range(len(results)):
            if results[j]<=results[k]:
                d=d+1
        if d>=2:
            moves.pop(moves.index(moves[j]))
            moves.insert(j,0)
            results.pop(results.index(results[j]))
            results.insert(j,0)
            
    for i in range(4):
        results.pop(results.index(0))
        moves.pop(moves.index(0))
    
        
def addmoves():       
    for i in range(3):
        e=random.randint(1,6)
        if e==1:
            moves.append(move(moves[0].digits12,moves[0].digits34,moves[1].digits56,moves[1].digits78))
        if e==2:
            moves.append(move(moves[0].digits12,moves[1].digits34,moves[0].digits56,moves[1].digits78))
        if e==3:
            moves.append(move(moves[0].digits12,moves[1].digits34,moves[1].digits56,moves[0].digits78))
        if e==4:
            moves.append(move(moves[1].digits12,moves[0].digits34,moves[0].digits56,moves[1].digits78))
        if e==5:
            moves.append(move(moves[1].digits12,moves[0].digits34,moves[1].digits56,moves[0].digits78))
        if e==6:
            moves.append(move(moves[1].digits12,moves[1].digits34,moves[0].digits56,moves[0].digits78))
            
#_____________________________________________________________________________________________
            
# Make board
par=100
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
        
    def randtheta(self):        
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
        
class move():
   def __init__(self,digits12,digits34,digits56,digits78):
        self.digits12=digits12
        self.digits34=digits34
        self.digits56=digits56
        self.digits78=digits78
        
        
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
G1=guard(random.randint(0,31999)/par,random.randint(0,5999)/par)
G2=guard(random.randint(0,31999)/par,random.randint(0,5999)/par)
G3=guard(random.randint(0,31999)/par,random.randint(0,5999)/par)
G4=guard(random.randint(0,31999)/par,random.randint(0,5999)/par)
G1.randtheta()
G2.randtheta()
G3.randtheta()
G4.randtheta()


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

print("the initial area visible is", ((c/b))*100, "procent")



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
    
#generating moves
posi=['00','01','10','11']
moveA=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveB=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveC=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveD=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveE=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moves=[moveA, moveB, moveC, moveD, moveE]
guards=[G1,G2,G3,G4]
guard1start=(G1.x,G1.y)
guard2start=(G2.x,G2.y)
guard3start=(G3.x,G3.y)
guard4start=(G4.x,G4.y)
results=[]


moving()
comparemoves()
addmoves()
results=[]
moving()
comparemoves()
addmoves()
results=[]
moving()
comparemovestoone()
moving()
print("the second area visible is", ((c/b))*100, "procent")
print("movements:")
print(moves[0].digits12,moves[0].digits34,moves[0].digits56,moves[0].digits78)

                

guard1start=(G1.x,G1.y)
guard2start=(G2.x,G2.y)
guard3start=(G3.x,G3.y)
guard4start=(G4.x,G4.y)
moveA=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveB=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveC=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveD=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveE=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moves=[moveA, moveB, moveC, moveD, moveE]
results=[]


moving()
comparemoves()
addmoves()
results=[]
moving()
comparemoves()
addmoves()
results=[]
moving()
comparemovestoone()
moving()
print("the third area visible is", ((c/b))*100, "procent")
print("movements:")
print(moves[0].digits12,moves[0].digits34,moves[0].digits56,moves[0].digits78)



guard1start=(G1.x,G1.y)
guard2start=(G2.x,G2.y)
guard3start=(G3.x,G3.y)
guard4start=(G4.x,G4.y)
moveA=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveB=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveC=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveD=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveE=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moves=[moveA, moveB, moveC, moveD, moveE]
results=[]


moving()
comparemoves()
addmoves()
results=[]
moving()
comparemoves()
addmoves()
results=[]
moving()
comparemovestoone()
moving()
print("the fourth area visible is", ((c/b))*100, "procent")
print("movements:")
print(moves[0].digits12,moves[0].digits34,moves[0].digits56,moves[0].digits78)



guard1start=(G1.x,G1.y)
guard2start=(G2.x,G2.y)
guard3start=(G3.x,G3.y)
guard4start=(G4.x,G4.y)
moveA=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveB=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveC=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveD=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveE=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moves=[moveA, moveB, moveC, moveD, moveE]
results=[]


moving()
comparemoves()
addmoves()
results=[]
moving()
comparemoves()
addmoves()
results=[]
moving()
comparemovestoone()
moving()
print("the fifth area visible is", ((c/b))*100, "procent")
print("movements:")
print(moves[0].digits12,moves[0].digits34,moves[0].digits56,moves[0].digits78)



guard1start=(G1.x,G1.y)
guard2start=(G2.x,G2.y)
guard3start=(G3.x,G3.y)
guard4start=(G4.x,G4.y)
moveA=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveB=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveC=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveD=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moveE=move(random.choice(posi),random.choice(posi),random.choice(posi),random.choice(posi))
moves=[moveA, moveB, moveC, moveD, moveE]
results=[]


moving()
comparemoves()
addmoves()
results=[]
moving()
comparemoves()
addmoves()
results=[]
moving()
comparemovestoone()
moving()
print("the final area visible is", ((c/b))*100, "procent")
print("movements:")
print(moves[0].digits12,moves[0].digits34,moves[0].digits56,moves[0].digits78)
