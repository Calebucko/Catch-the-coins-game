# Catch-the-coins-game
    Catch the protein products
    import pygame, simple GE random
    
    create class for protein products
        set image to jpeg
        set size
        rest sprite
    def rest property
        place y position
        bind x range in screen size
        set speed to random range

    define checkBoundes property
    if statement for if protein falls to bottom 
        reset to top

    create class for skinnyGuy
        set image to png
        set size 
        set initial position on screen
        set move speed

    define property for movement
        bind left, up, down, and right to if key is pressed functions

    class for score label:
        center label to the left of screen
        set size
        set text to "score"
        set text color
    
    class for timer label
        center label to right of the screen
        set size
        set text to "time"
        set text color

    create class for the Game
        set background image
        set sound effect for collision between protein and skinnyGuy
        define amount of protein at start of game
        refresh sprites

    create class for instructions 
        create multi label explaining game 
        " "You're a very skinny guy, down on his luck with getting gains.",
            "An angel descendes and commands you to begin the grind",
            "You are placed into a gym, as protein powder falls from the sky",
            "Get as much protein as you can before the gym closes"
        create quit button
            set text to "Quit(left key)"
            center to below multi label
        create play button
            set text to "Quit(right key)"
            center to below  multi label
        score label shows previous score
        score = 0

        set sprite list.

          define process function for playing sound when sprites collide
        set sound to play during collision
        reset protein sprite and sound effect when collison is over

        def process for buttons
            if quit button is clicked on or left key is pressed
                stop state
            if play button is clicked on or right key is pressed
                begin play state
            if left key button is typed
                stop state
            if right key button is typed 
                play state
            

  
    def main
        create while loop for states
        instructions state start 
        if instructions state button choice is "play
            start game
        else
            stop state

    


