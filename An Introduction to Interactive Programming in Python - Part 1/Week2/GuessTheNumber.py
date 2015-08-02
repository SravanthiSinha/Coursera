# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


#http://www.codeskulptor.org/#user40_sIzKlisGomKYi5d.py

import simplegui
import math
import random

# initialize global variables used in your code here
secret_number =0
num_range=100
number_guesses=0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number,number_guesses
    secret_number =random.randrange(0,num_range) 
    number_guesses=int(math.ceil(math.log(num_range+1,2)))
    print 
    print"New game. Range is [0,"+str(num_range)+")"
    print "Number of remaining guesses is ",number_guesses
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game       
    global num_range
    num_range=100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range=1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global number_guesses,num_range
    input_number=int(guess)  
    print 
    print "Guess was",input_number
    number_guesses-=1
    print "Number of remaining guesses is", number_guesses
    if number_guesses>0:
        if input_number<secret_number:
            print "Higher!"
        elif input_number>secret_number:
            print "Lower!"
        else:
            print "Correct!"
            num_range=100
            new_game()
    else:
        print "You ran out of guesses.  The number was ",secret_number
        num_range=100
        new_game()
        
# create frame
frame=simplegui.create_frame("Guess the number",200,200)


# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)",range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()

# Start the frame animation
frame.start()
