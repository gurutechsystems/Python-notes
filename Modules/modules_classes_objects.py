#Modules are simple python files that can be used in another python file or program just by referencing it.
#-write the python file(module)
#-import the file
#-Access the file contents

#EXAMPLE-1
print('\n#Simple module example')
def guru():
    print('God is Good')

#=>import a MODULE and access the module content
import modules_classes_objects #module=filename
modules_classes_objects.guru() #accessing or reading file content

#adding a variable to the module
def guru():
    print('God is Good')
guress='my husband in whom i am well pleased'
#accessing the variable in the module
import modules_classes_objects
modules_classes_objects.guru()
print(modules_classes_objects.guress)

#=>A class is a way to take groups of functions and data and place inside a container so that u can access them at anytime uisng the '.' operator
#Classes helps u to construct your software in a particular way
#=>Classes are mini-modules
print('\n#example-1 of classes and objects')
class guru(object):      #create a class called "guru"
    def __init__(self):  #The class has an initializer method (__init__) that initializes an instance variable. 
        self.thalia='God is good' #self.thalia to the string 'God is good' initialiezed by the initializer

    def aliana(self):   #"aliana" is another function/method of the class
        print('my first fruit') 

#=>Objects are mini-imports.Objects are imports for Classes
# When u create a class,what u get is called an object
obase=guru() #where "obase" is the object of class "guru"
obase.aliana() #imoprting the "aliana" function into class guru() with obase as object
print(obase.thalia)  

#================================================================================================

#===>EXAMPLE-2
print('\n#example-2 of classes and objects')
class song(object): #this is a class definition for a "song" object       
    def __init__(self, lyrics): #the class has an initializer and one instance variable "lyrics"

        self.lyrics=lyrics  

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

birthday=song(['Happy birthday to you.....',
               'Happy birthday to you ...',
               'many more years to you...']) 

parade=song(['Gingle bell...', 
             'gingle bell...', 
             'gingle all the way'])

birthday.sing_me_a_song()
parade.sing_me_a_song()

#==================================================================================

#===>EXAMPLE-3 "is-a"(this is a phrase to say something inherited from another)

#Is-a = persons,anaimals
print('\n#Example of Is-a phrase')
class animal(object):   #this is a class definition for an "animal" object
    pass                #The "pass" statement is used as a placeholder, indicating that the class definition is empty
#
class dog(animal):     #dog Is-a object i.e dog Is-a animal
    def __init__(self,name):
        self.name=name
#
class cat(animal):
    def __init__(self,name):
        self.name=name
#
class person(object):
    def __init__(self,name):
        self.name=name    

#Has-a = ownership
class employee(person): #represents a python class "employee" that inherits from another class "person"
    def __init__(self, name, salary): #the "employee" class has 2 instance variables "name" and "salary"
        super(employee,self).__init__(name) # the "super" function is used to call the __init__ method od the superclass "person"
        self.salary=salary                  #passing the name parameter to ensure the "name" instance variable is set correctly for the "employee" object

#TREE OF CLASSES
print('\n#Tree of classes')        
class scene(object):  #This code defines a Python class named "scene" which does not have any attributes/method 
    def enter(self):  #or method defined in it
        pass          #The "pass" statement is used as a placeholder, indicating that the class definition is empty 
                      #and does not contain any code.          
class engine(object):
    def __init__(self,scene_map):
        pass

    def play(self):
        pass  

class death(scene):
    def enter(self):
        pass
class centralcorridor(scene):
    def enter(self):
        pass
class guru(scene):
    def enter(self):
        pass
class guress(scene):
    def enter(self):
        pass
class thalia(scene):
    def enter(self):
        pass

class map(object):
    def __init__(self,start_scene):
        pass
    def next_scene(self,scene_name):
        pass                    
    def opening_scene(self):
        pass

a_map=map('central_corridor')
a_game=engine(a_map)
a_game.play()    

#===================================================================================

#Breaking the "tree of classes" file into sections
print('\#Breaking the file into sections')
from sys import exit
from random import randint

'''
class scene(object):  
    def enter(self): 
        pass
'''
class scene(object):
    def enter(self):
        print('This scene isnot yet configured,subclass the scene and implement enter() function')
        exit(1)   

'''
class engine(object):
    def __init__(self,scene_map):
        pass

    def play(self):
        pass    
'''
class engine(object):
    def __init__(self,scene_map):
        self.scene_map=scene_map

    def play(self):
        current_scene=self.scene_map.opening_scene() 
        last_scene=self.scene_map.next_scene('finished')  

        while current_scene != last_scene:
            
            next_scene_name=current_scene.enter()
            current_scene=self.scene_map.next_scene(next_scene_name)
'''
class death(scene):
    def enter(self):
        pass
'''
class death(scene):
    msg=[
        'you tried and did ur best'
        'your family is gonna be proud'
        'Never give up guru'
        'u are a conqouror'
    ]        
    def enter(self):
        print(death.msg[randint(0, len(self.msg)-1)])
        exit(1)
'''
class centralcorridor(scene):
    def enter(self):
        pass      
'''
class centralcorridor(scene):
    def enter(self):
        print ("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
        print ("your entire crew. You are the last surviving member and your last")
        print ("mission is to get the neutron destruct bomb from the Weapons Armory,")
        print ("put it in the bridge, and blow the ship up after getting into an ")
        print ("escape pod.")
        print ("\n")
        print ("You're running down the central corridor to the Weapons Armory when")
        print ("a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
        print ("flowing around his hate filled body. He's blocking the door to the")
        print ("Armory and about to pull a weapon to blast you.")

        action=input('>')

        if action=="shoot":
            print('''
            Quick on the draw you yank out your blaster and fire it at the Gothon.
            His clown costume is flowing and moving around his body, which throws
            off your aim. Your laser hits his costume but misses him entirely. 
            completely ruins his brand new costume his mother bought him, which
            This makes him fly into a rage and blast you repeatedly in the face until
            you are dead. Then he eats you.
            ''')
            return 'death'


        elif action=='dodge':
            print('''
            Like a world class boxer you dodge, weave, slip and slide right"
            as the Gothon's blaster cranks a laser past your head."
            In the middle of your artful dodge your foot slips and you"
            bang your head on the metal wall and pass out."
            You wake up shortly after only to die as the Gothon stomps on"
            your head and eats you.
            ''')
            return 'death'
        
        elif action=='tell a joke':
            print('''
            Lucky for you they made you learn Gothon insults in the academy."
            You tell the one Gothon joke you know:"
            Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            While he's laughing you run up and shoot him square in the head"
            putting him down, then jump through the Weapon Armory door."
            ''')
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
'''
class guru(scene):
    def enter(self):
        pass            
'''
class guru(scene):
    def enter(self):
        print('''
        You do a dive roll into the Weapon Armory, crouch and scan the room"
        for more Gothons that might be hiding. It's dead quiet, too quiet."
        You stand up and run to the far side of the room and find the"
        neutron bomb in its container. There's a keypad lock on the box"
        and you need the code to get the bomb out. If you get the code"
        wrong 10 times then the lock closes forever and you can't"
        get the bomb. The code is 3 digits."
        ''')

        code="%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
             print('BZZZZEDDD')
             guesses += 1
             guess = input("[keypad]> ")

        if guess == code:
            print('''
            The container clicks open and the seal breaks, letting gas out."
            You grab the neutron bomb and run as fast as you can to the"
            bridge where you must place it in the right spot."
            ''')
            return 'the_bridge'
        else:
            print('''
            The lock buzzes one last time and then you hear a sickening"
            melting sound as the mechanism is fused together."
            You decide to sit there, and finally the Gothons blow up the"
            ship from their ship and you die."
            ''')
            return 'death'
'''        
class guress(scene):
    def enter(self):
        pass        
'''
class guress(scene):
    def enter(self):
        print('''
        You burst onto the Bridge with the neutron destruct bomb"
        under your arm and surprise 5 Gothons who are trying to"
        take control of the ship. Each of them has an even uglier"
        clown costume than the last. They haven't pulled their"
        weapons out yet, as they see the active bomb under your"
        arm and don't want to set it off."
        ''')

        action=input('>')

        if action == "throw the bomb":
            print('''
            In a panic you throw the bomb at the group of Gothons"
            and make a leap for the door. Right as you drop it a"
            Gothon shoots you right in the back killing you."
            As you die you see another Gothon frantically try to disarm"
            the bomb. You die knowing they will probably blow up when"
            it goes off."
            ''')
            return('death')
        elif action == "slowly place the bomb":
            print('''
            You point your blaster at the bomb under your arm"
            and the Gothons put their hands up and start to sweat."
            You inch backward to the door, open it, and then carefully"
            place the bomb on the floor, pointing your blaster at it."
            You then jump back through the door, punch the close button"
            and blast the lock so the Gothons can't get out."
            Now that the bomb is placed you run to the escape pod to"
            get off this tin can."
            ''')
            return 'escape_pod'
        else:
            print('DOES NOT COMPUTE!')
            return  'the_bridge'
'''        
class thalia(scene):
    def enter(self):
        pass        
'''
class thalia(scene):
    def enter(self):
        print('''
        You rush through the ship desperately trying to make it to"
        the escape pod before the whole ship explodes. It seems like"
        hardly any Gothons are on the ship, so your run is clear of"
        interference. You get to the chamber with the escape pods, and"
        now need to pick one to take. Some of them could be damaged"
        but you don't have time to look. There's 5 pods, which one"
        do you take?"
        ''')
        
        good_pod=randint(1,5)
        guess=input("[pod #]>")

        if int(guess) != good_pod:
            print('''
            You jump into pod %s and hit the eject button." % guess
            The pod escapes out into the void of space, then"
            implodes as the hull ruptures, crushing your body"
            into jam jelly."
            ''')
            return 'death'
        else:
            print('''
            You jump into pod %s and hit the eject button." % guess
            The pod easily slides out into space heading to"
            the planet below. As it flies to the planet, you look"
            back and see your ship implode then explode like a"
            bright star, taking out the Gothon ship at the same"
            time. You won!"
            ''')
            return 'finished'
        
class Finished(scene):
    def enter(self):
        print('You won, Good job') 
        return 'finished'       
'''
class map(object):
    def __init__(self,start_scene):
        pass
    def next_scene(self,scene_name):
        pass                    
    def opening_scene(self):
        pass
'''
class map(object):
    scenes=   {
        'central_corridor':'centralcorridor()',
        'guru':'guru()',
        'guress':'guress()',
        'thalia':'thalia()',
        'death':'death()',
        'Finished':'finished()',
    } 
    def __init__(self,start_scene):
        self.start_scene=start_scene

    def next_scene(self, scene_name):
        val=map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene) 
       
a_map=map('central_corridor')
a_game=engine(a_map)
a_game.play()