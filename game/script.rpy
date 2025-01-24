# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    scene bg room

    """
    You were ill and you went to sleep. They promised cure in twenty years. 

    Now, after almost a hundred years in slumber, you are about to wake up in an unfamiliar world.     
    """

    label slumber:
    
    menu:
        "Wake up":
            jump awake
        "Rest":
            "Slumber persists a little longer..."
            jump slumber

    label awake:
    """
    You feel pain. 

    You try to open your eyes, but the darkness around is impenetrable. 
    
    You feel fingers on your neck, they are cold and inhospitable. 
    """

    $ moved = False
    $ talked = False

    label first_actions:
    
    menu: 
        "Move" if not moved:
            "You try to move your limbs, but pain is so strong, you can't actually feel if they obey your commands."
            $ moved = True
            jump first_actions
        "Try to say something" if not talked:
            "You try to say something, but only dry rattle comes out of your mouth."
            $ talked = True
            jump first_actions
        
        "Give up":
            jump sleep

    label sleep:

    "Your conciousness wanders away"
        
    return
