#In this pyhon script,we use a library called urllib to download a list of words
print('\n#Reading Python scripts')
import random
from urllib.request import urlopen
import sys

WORD_URL='http://learncodethehardway.org/words.txt'
WORDS=[]
PHRASES={
    'class %%%(%%%)':'make a class named %%% that is-a %%%', #is-a=phrase to say something inherited from another
    'class %%%(object):\n\tdef _init_(self,***)':'class %%% has-a _init_ that takes self and *** parameters.', #has-a=phrase to say something composed of other thibgs
    'class %%%(object):\n\tdef ***(self,@@@)':'class %%% has-a function named *** that takes self amd @@@ parameters.',
    '***=%%%()':'set *** to an instance of class %%%',
    '***.***(@@@)':'from *** get the *** function and call it with parameters self,@@@.',
    "***.***='***'":"from *** get the *** attribute and set it to '***'."
    }

#Drill phrases
PHRASES_FIRST=False                             #sys.argv contains command-line arguments passed in a python script
if len(sys.argv)==2 and sys.argv[1]=='english': #sys.argv[0]=sript name, sys.argv[1]=1st command line argument,sys.argv[2]
    PHRASES_FIRST=True                          #argv=argument variable and it is a list that contains the name of the script being executed as its first element, followed by any command-line arguments that were provided after the script name.

#Load(add) up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet,phrase):
    class_names=[w.capitalize() for w in random.sample(WORDS,snippet.count('%%%'))]
    other_names=[random.sample(WORDS,snippet.count('***'))]
    results=[]
    param_names=[]

    for i in range(0,snippet.count('@@@')):
        param_count=random.randint(1,3)
        param_names.append('.'.join(random.sample(WORDS,param_count)))
    for sentence in snippet, phrase:
        result = sentence[:]   

