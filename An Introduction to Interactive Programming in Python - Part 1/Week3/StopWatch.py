#"Stopwatch: The Game"

#import modules

import simplegui

# define global variables
counter=0
ntotal=0
ncurrent=0
running=False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    nmSec, t = t%10, t//10
    nSec2, t = t%10, t//10
    nSec1, nMin = t%6, t//6
    return str(nMin)+":"+str(nSec1)+str(nSec2)+"."+str(nmSec)

def score():
    return str(ncurrent)+"/"+str(ntotal)     
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global running
    timer.start()
    running=True
    
def stop_timer():
    global counter,ntotal,ncurrent,running
    timer.stop()
    if running:
        if counter%10==0:
            ncurrent=ncurrent+1
        ntotal=ntotal+1
    running=False

def reset_timer():
    global counter,ntotal,ncurrent
    timer.stop()
    counter=0
    ntotal=0
    ncurrent=0  
    running=False
    
# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter=counter+1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter),[40,120],50,"White")
    canvas.draw_text(score(), [155, 25], 26, "Green")
    
# create frame
frame=simplegui.create_frame("Stopwatch: The Game",200,200);

# register event handlers
frame.add_button("Start",start_timer,125)
frame.add_button("Stop",stop_timer,125)
frame.add_button("Reset",reset_timer,125)
frame.set_draw_handler(draw)

# start frame
frame.start()
timer=simplegui.create_timer(100,tick)
