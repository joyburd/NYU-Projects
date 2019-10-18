#Joy Burkart
#Assignment 5
#hello! this is going to print a repeating pattern of moons and (eventually, they run second) that,
#on my screen, according to my set up, and the placement of my x axis and y axis
#covers the whole turtle window. I recognize there's some chance it might not
#on your screen, so I apologize in advance. I'm not really sure if turtle pulls up the same size window for everyone.
#be forewarned, it takes a hot minute to print, even though the speed is set to fastest

from turtle import *
#sprinkling that chicken blood and getting my turtle graphics going

def rays(): #this is for the rays on my sun

    #vertical red line
    color("red") #obviously sun rays are red; my red rays are all on the vertical and horozontal
    fd(40) #draws a line straight up (vertical) from the starting point

    #horozontal red line
    backward(20) #gets the turtle back to the center of the lines
    rt(90) #turns the focus of the turtle
    fd(20) #draws half a line on the horozontal (since i'm in the center of the graphic, drawing a half line forward and then a full line backward, and then moving forward half a line (lines all being 40 steps long) to get back to the center, seemed, to me, the best way to go about it)
    backward(40) #draws a full line on the horozontal
    fd(20) #gets turtle back to center of graphic

    #diagonal orange line
    color("orange") #obviously other suns rays are orange; my orange ones are at a diagonal
    rt(45) #turning the turtle to a diagonal
    fd(20) #moves turtle on the diagonal, half a line
    backward(40) #draws a full line on the diagonal
    fd(20) #gets turtle back to center

    #other diagonal orange line
    lt(90) #turns turtle to draw diagonal line at a 90 degree to the previous diagonal
    fd(20) #half a line on the diagonal
    backward(40) #full line on the diagonal
    fd(20) #back to center of graphic

    #recentering turtle
    rt(45) #moves turtle off diagonal so points down the bottom red line parallel to the y axis
    fd(10) #moves a 1/4 of the way down the line, for the optimal placement of the yellow circle (center of sun)
    lt(90) #orients the turtle facing the right (my right, and yours) parallel to the x-axis, so it can draw the circle


def suncircle(): #this is for the center of my sun (the lil yellow circle)
    size = 10 #the idea was to make the suns the same size as the moons, this gives my sun circle a diameter of 20, with ten on each side for the rays, so it totals 40 across, the diameter of the circles that make up the moons
    
    color ("yellow") #obviously the center of the sun is yellow.
    begin_fill() #you have to fill it
    circle(size) #size variable used as radius to create sun
    end_fill() #end the fill or tagic things happen, probably
    penup() #no drawing for this bit
    rt(90) #turns the turtle so it can move down the red line I drew previously
    backward(10) #going to the bottom of the graphic (aka, the tip of the red line parallel to the y axis. i found out the hard way if i don't do this part, all my suns print on a diagonal
    lt(90) #reorienting turtle so it can draw the next sun
    pendown() #putting the pen back down for drawing


def sun(): #all together now to create complete sun graphic
    rays() #maybe not the most necessary step, but it's nice and neat and creates a complete graphic, with rays and circles in proper order
    suncircle()

def sunrows():#to print a row of suns parallel to the x axis
    for row in range(7): #this will print me 7 suns (0-6)
        penup() #no drawing for this movement, otherwise i'd get weird lines between my suns
        fd(80) #kind of an odd space to move forward, but it took me for ever to figure out the exact spacing between the suns and moons (each 40pts long), as it stands they should have 10 steps of space between them
        pendown() #need the pen down so it can draw my suns!
        sun()

def suncol(): #for movement along the y axis
    y = 300 #orienting to the highest value pictured on screen
    while y!= -400:#lowest value on screen
        penup() #so it can move without visual evidence
        goto(-420,y) #starts in the upper left (as i see it)
        pendown()
        sunrows() #prints a row of suns along the x axis
        y-=50 #now moves down the y axis to print another row

def moon(): #moon function

    #i realize the way i've chosen to make a moon means that you can actually see the blue parts touching. sorry. i just kinda like it

    size = 20 #radius of initial circle
    circles = 4 #i needed an elif loop, so my moons have a blue outline on them

    for i in range(circles): #elif loop defining circles within each other to create a lil moon (0,3)
        if i % 4 == 1:
            color ("dodgerblue") #innermost circle of actual moon (2nd smallest)
        elif i % 4 == 2:
            color ("blue") #middle circle (it's a light blue stripe in the middle)
        elif i % 4 == 3:
            color("white") #this is the smallest circle, last to print (the one in the middle that's white, blocking out the rest of the other circles and creating the moon shape)
        else:
            color("blue") #outermost circle, largest and first to print
            lt(90) #technically this is the first circle drawn, and as such this is where i put the instruction that orients where the circles are drawn on the right (as i see it)

        begin_fill() #filling in my circles
        circle(size)
        end_fill()

        size -= 2 #radius decrease per circle

    rt(90) #reorients my turtle to draw the next moon, otherwise my moons print in like a circle starting on the left of each other, it isn't fun

def moonrows():#rows of moons along the x axis
    for row in range(6): #will give me five moons (0,5)
        penup()#for invisible movement between moon drawings
        fd(100) #space between the beginning of each moon. as each moon is 40 steps long, they actually have a space of 60 between them, and with a forty step sun between each of those, there's a remaining 10 steps of space between each individual graphic
        pendown()
        moon() #draws the moon; i feel i should mention that this sort of defeats the purpose of my specifying my x axis, as this moves it 100 steps off the specified place before it ever draws a moon, but i felt like that was fine as long as i compensated for it in my initial x axis value

def mooncol():#moves down the y axis
    y = 300 #highest point
    while y!= -350:#lowest point
        penup()
        goto(-350,y) #starting point in upper left corner of screen
        pendown()
        moonrows() #row of moons
        y-=50 #moves 50 pts down for the next row
        
        
def main(): #main function
    speed("fastest") #fast but not fast enough
    mooncol() #complete program of moons prints first
    suncol() #then a complete program of suns prints between those
    ht() #hides the turtle
    done() #specifies ending point

main() #runs program
