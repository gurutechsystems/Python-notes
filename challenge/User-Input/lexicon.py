#A==>Group of allowable words(lexicon)
lexicon={
 'direction words':['north','south','east','west','up','down','left','right','back'],
 'verbs':['go','stop','kill','eat'],
 'stop words':['the','in','of','from','at','it'],
 'nouns':['door','bear','princess','cabinet'],
 'numbers':[0,1,2,3,4,5,6,7,8,9]
}
#B==>with the lexicon of words,we can use the words to construct a sentence and even break up a sentence into words
stuff=input('>')
words=stuff.split() 
 
#C==>TUPLES:To construct a sentence from words or breakup a sentence into words,we use tuples
#Tuple is data that cannot be modified
#This creates a pair(TYPE,WORD)
#example-1
first_word=('verb','go')
second_word=('direction','north')
third_word=('direction','west')
sentence=[first_word,second_word,third_word]

#example-2
first_word=('stop words','from')
second_word=('direction','north')
third_word=('verbs','go')
forth_word=('direction','south')
firth_word=('nouns','princess')
sentence=[first_word,second_word,third_word,forth_word,firth_word]

#D==>MATCH and PEEK(Now we are using list of tuples to create sentences)
#Peeking words from a list and matching the words to create a sentence
class parserError(Exception):  #create the parserError class with "exception" needed for the parsing error
    pass

class sentence(object):   #create the sentence class with "object" to take tuples and convert them
    def _init_(self, subject, verb, obj):
        self.subject=subject[1]
        self.verb=verb[1]
        self.object=obj[1]

def peek(word_list):  #create a function that can peek a list of words and return what type of word it is
    if word_list:     #this function help us to make decisions on the kind of sentence we want to make based on 
        word=word_list[0] #what the next word is.The we call another function to consume the word and carry on
        return word[0]
    else:
        return None  

def match(word_list, expecting): #To consume a word we use match function.It confirms that the expected word is 
    if word_list:                #the right type,takes it off the list and return the word
        word=word_list.pop(0)
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
        raise parserError('expected a verb next') # if not a verb,it raises the parserError message
#Parsing the sentence objects
def parse_object(word_list):
    skip(word_list,'stop')         #skipping the "stop" word 
    next_word=peek(word_list)      #peeking next word from word_list

    if next_word=="noun":
        return match(word_list,'noun')
    elif next_word=="directionn":
        return match(word_list,'direction')
    else:
        return parserError('expected a noun or direction next')
#parsing a sentence subject    
def parse_subject(word_list):
    skip(word_list,'stop')
    next_word=peek(word_list)

    if next_word=='noun':
        return match(word_list,'noun')
    elif next_word=='verb':
        return match('noun','player')
    else:
        raise parserError('Expected a verb next')
#Final sentence function
def parse_sentence(word_list):
    subj=parse_subject(word_list)
    verb=parse_verb(word_list)
    obj=parse_object(word_list)

    return sentence(subj,verb,obj)    

#E==>SCANNING USER INPUT(we use the input())
#This scanner will take raw input from user and return to the user a sentence composed of list of tuples with (TOKEN,WORD)pairings
#However if the WORD is not part of the lexicon,the scanner will return the WORD snd set the TOKEN to an error token
   #example
description=input('sentence')
print(f'Hello,{description}')   

#F==>EXCEPTIONS(these are alarms a program(function) raises when it encounters and error )
#We handle exceptions using the "key" and "except keywords"

def convert_numbers(s):
    try:
        return int(s) #"try block" contains the code we want to try
    except ValueError: #"except block" contains the code that handles the exception if it occurs
        return None    
#example1(success)
number_string='42'
number=convert_numbers(number_string)

if number is not None:
    print(f'The integer value of {number_string} is {number}')
else:
    print(f'{number_string} cannot be converted to integer')    

#example2(failure)
number_string='foo'
number=convert_numbers(number_string)

if number is not None:
    print(f'The integer value of {number_string} is {number}')
else:
    print(f'{number_string} cannot be converted to integer')    
    