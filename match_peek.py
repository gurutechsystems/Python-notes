#==>MATCH and PEEK(Now we are using list of tuples to create sentences)
#Peeking words from a list and matching the words to create a sentence
#when naming classes, we capitalize the initials of every word in the class name and we don't use underscore(_) unlike variables and functions where everything is in small letters
#This is the pascal naming convention

#Classes are used to define new data types(int,string,float,boolean,none,list,dictionaries etc) to model real concepts
#Class defines the template for creating an object while an object is an instance created based on the template

#EXAMPLE-1
class Point:
    def move(self):
        print('move')
    def draw(self):
        print('draw')


point1=Point() #creating an object(point1) from the class(Point)
point1.draw()

#EXAMPLE-2(Constructor)  
class Point:
    def __init__(self, x, y): # the __init__ method is a constructor used to construct or create an object
        self.x=x
        self.y=y   
    def move(self):
        print('move')
    def draw(self):
        print('draw')


point2=Point(10,20)
#point2.x=11(this will change the value of x)
print(point2.x)

#EXAMPLE-3(Define a new class call "person with "name" attribute and "talk" method) 
class Person:
    def __init__(self, name):
        self.name=name
    def talk(self):
        print('talk')


guru=Person("guru obase")
print(guru.name) #result= guru obase
guru.talk() # result = talk        

#OR
class Person:
    def __init__(self, name):
        self.name=name
    def talk(self):
        print(f'Hi, i am {self.name}')


guru=Person("guru obase")
guru.talk() 

guress=Person('guress benis')
guress.talk()






class ParserError(Exception):  #create the parserError class with "exception" needed for the parsing error
    pass

class Sentence(object):   #create the sentence class with "object" to take tuples and convert them
    def __init__(self, subject, verb, obj): #N.B double undercover for init
        self.subject = subject[1]           #[1] represents the index of the 2nd element in subject variable
        self.verb = verb[1]
        self.object = obj[1]       #[0] in peek function represnts the index of the 1st element in word_list
    

def peek(word_list):  #create a function that can peek a list of words and return what type of word it is
    if word_list:     #this function help us to make decisions on the kind of sentence we want to make based on 
        word=word_list[0] #what the next word is.The we call another function to consume the word and carry on
        return word[0]    
    else:
        return None  

def match(word_list, expecting): #To consume a word we use match function.It confirms that the expected word is     
    if word_list:                #the right type,takes it off the list and return the word.If not,it returns None
        word=word_list.pop(0) #pop(0) means to remove the first word of word_list and return the removed word
        if word[0]==expecting:
            return word
        else:
            return None
    else:
        return None 

def skip(word_list,word_type):        #create a function to skip words not needed in the semtence
    while peek(word_list)==word_type: #skip doesnt skip just one word,it skips as amny words as it finds
        match(word_list,word_type) 
                   
#Parsing the sentence verb
def parse_verb(word_list):
    skip(word_list,'stop')            #skipping the "stop" word 

    if peek(word_list)=='verb':       #and go ahead to peek the "verb" in the next word
        return match(word_list,'verb') #if its a verb,it takes it of the list and "match" it
    else:
        raise ParserError('expected a verb next') # if not a verb,it raises the parserError message
#Parsing the sentence objects
def parse_object(word_list):
    skip(word_list,'stop')         #skipping the "stop" word 
    next_word=peek(word_list)      #peeking next word from word_list

    if next_word=="noun":
        return match(word_list,'noun')
    elif next_word=="directionn":
        return match(word_list,'direction')
    else:
        return ParserError('expected a noun or direction next')
#parsing a sentence subject    
def parse_subject(word_list):
    skip(word_list,'stop')
    next_word=peek(word_list)

    if next_word=='noun':
        return match(word_list,'noun')
    elif next_word=='verb':
        return match('noun','player')
    else:
        raise ParserError('Expected a verb next')
#Final sentence function
def parse_sentence(word_list):
    subject=parse_subject(word_list)
    verb=parse_verb(word_list)
    object=parse_object(word_list)

    return Sentence(subject,verb,object)    

#To get the results of this script
word_list=[('noun', 'players'), ('verb', 'go'), ('direction', 'south')]
result=parse_sentence(word_list)

print(result.subject)
print(result.verb)
print(result.object)

'''
class ParserError(Exception): 
    pass

class Sentence(object):
    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)

word_list = [('noun', 'players'), ('verb', 'go'), ('direction', 'south')]
result = parse_sentence(word_list)

print(result.subject)
print(result.verb)
print(result.object)
'''
