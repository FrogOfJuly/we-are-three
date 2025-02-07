# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")

init python: 
    from collections import namedtuple

    # Simple namespace hack to combat the fact 
    # that all variables in ren'py are global
    # Go here for insight: https://stackoverflow.com/questions/4984647/accessing-dict-keys-like-an-attribute
    class Namespace(dict):
        def __init__(self, *args, **kwargs):
            super(Namespace, self).__init__(*args, **kwargs)
            self.__dict__ = self

    state = Namespace()

# The game starts here.

label start:

    $ state.awakening = Namespace()

    scene bg room

    jump sleepers_station

    """
    You were ill and you went to sleep. They promised cure in twenty years. 

    Now, after almost a hundred years in slumber, you are about to wake up in an unfamiliar world.     
    """

    label slumber:
    
        menu:
            "Rest":
                "Slumber persists for a little longer..."
                jump slumber
            "Wake up":
                pass

        """
        You feel pain. 

        You try to open your eyes, but the darkness around is impenetrable. 
        
        You feel fingers on your neck, they are cold and inhospitable. 
        """

        $ state.awakening.moved = False
        $ state.awakening.talked = False

        label .struggle:
        
            menu: 
                "Move" if not state.awakening.moved:
                    "You try to move your limbs, but pain is so strong, you can't actually feel if they obey your commands."
                    $ state.awakening.moved = True
                    jump .struggle
                "Say something" if not state.awakening.talked:
                    "You try to say something, but only dry rattle comes out of your mouth."
                    $ state.awakening.talked = True
                    jump .struggle
                "Give up":
                    pass

        "Your conciousness wonders away"

        # TODO: Here should be a fade to black with a
        # considerable delay to signify passage of time
            
        jump luddic_HQ

label the_end:
    return