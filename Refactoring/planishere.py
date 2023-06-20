'''
-The below code creates a class "Room" with 3 methods i.e __init__,go and add_path
-The __init__ method of the class creates the name,description and paths attributes of the Room's name

-The 'go' method takes a direction parameter and return the values of the corresponding directions in "paths" of the Room and if the direction is not in the "paths" attribute,it returns None
-The "add_paths" mehod takes the paths parameter and updates the "paths" attribute of the Room with the given paths
'''
class Room():
    def __init__(self,name,description):
        self.name=name
        self.description=description
        self.paths={}

    def go(self,direction):
        return self.paths.get(direction,None) 
     
    def add_paths(self,paths):
        return self.paths.update(paths)

#Laying out of the basic structure of the map using Room class
#Create room objects
central_corridor=Room('central corridor',
'''
The Gothons of Planet Percal #25 have invaded your ship and destroyedyour entire crew.
You are the last surviving member and yourlast mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an escape pod.
You're running down the central corridor to the Weapons Armory when a Gothon jumps out,
red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate filled body.
He's blocking the door to the Armory and about to pull a weapon to blast you.
''')                     

guru=Room('guru',
'''
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,fur fvgf nebhaq gur ubhfr.
The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the head putting him down,
then jump through the Weapon Armory door.
You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding. 
It's dead quiet, too quiet. 
You stand up and run to the far side of the room and find the neutron bomb in its container. 
There's a keypad lock on the box and you need the code to get the bomb out. 
If you get the code wrong 10 times then the lock closes forever and you can't get the bomb. 
The code is 3 digits.
'''
) 

guress=Room('guress',
'''
The container clicks open and the seal breaks, letting gas out. 
You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right spot.
You burst onto the Bridge with the netron destruct bomb under
your arm and surprise 5 Gothons who are trying to take control of the ship. 
Each of them has an even uglier clown costume than the last. 
They haven't pulled their weapons out yet, as they see the active bomb under your arm and don't want to set it off.
'''
)

thalia=Room('thalia',
'''
You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat. 
You inch backward to the door, open it, and then carefully place the bomb on the floor, pointing your blaster at it. 
You then jump back through the door, punch the close button and blast the lock so the Gothons can't get out. 
Now that the bomb is placed you run to the escape pod to get off this tin can.
You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes. 
It seems like hardly any Gothons are on the ship, so your run is clear of interference. 
You get to the chamber with the escape pods, and now need to pick one to take. 
Some of them could be damaged but you don't have time to look. 
There's 5 pods, which one do you take?
'''            
)

the_end_winner=Room('the end winner',
'''
You jump into pod 2 and hit the eject button. The pod easily slides out into space heading to the planet below. 
As it flies to the planet, you look back and see your ship implode then explode like a bright star,
taking out the Gothon ship at the same time. You won!
'''
)

the_end_loser=Room('the end loser',
'''
You jump into a random pod and hit the eject button. 
The pod escapes out into the void of space, then implodes as the hull ruptures, crushing your body into jam jelly.
'''
)

#Connect rooms
thalia.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
    })
generic_death=Room('death', 'you are dead')

guress.add_paths({
    'throw the bomb':generic_death,
    'slowly place the bomb':thalia
})

guru.add_paths({
    '0132':guress,
    '*':generic_death
})

central_corridor.add_paths({
    'shoot':generic_death,
    'dodge':generic_death,
    'tell a joke':guru
})

START='central_corridor'

def load_room(name):
    '''
    There is a potential security problem here.
    Who gets to set name? Can that expose a variable?
    '''
    return globals().get(name)

def name_room(room):
    '''
    Same possible security problem. Can you trust room?
    What's a better solution than this globals lookup?
    '''
    for key, value in globals().items():
        if value==room:
            return key

######       
'''
Howerver, we have a few problems with our Room class and this map
-We have to add the text that was in the if-else clause that got printed b4 entering a room as part of each room
This means u cant shuffle the planisphere around
-There are parts in the original game where we ran code that determined
things like the bomb keypad code or the right pod. In this game we just
pick some defaults and go with it
-I have just made a generic_death ending for all of the bad decisions,
which you wll have to finish for me. You wll need to go back through and add
in all the original endings and make sure they work.
-I have got a new kind of transition labeled "*" that will be used for a
“catch-all” action in the engine.
'''        