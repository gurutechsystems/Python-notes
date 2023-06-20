'''
#A
#Install flask(pip install flask).This is a web application framework
from flask import Flask #The 'Flask' class is part of the flask web framework
app=Flask(__name__) #"__name__" is a python variable representing the name of the current module which is the filename withouth py e.g(setup)

 #In the flask framework, @app.route() associates a URL with a python function.
 #Allowing the functions to handle requests sent to the URL
 #here,the URL path is '/' representing the root URL of the application.This means that when a user visits the base URL
 #e.g(http://example.com/), the function associated with @app.route('/) will be called
@app.route('/') 
def hello_world():
    return 'Hello, World'

if __name__=='__main__':
    app.run() #u can change the port number your flask app is running on e.g app.run(8080) cuz the default port is 5000

#run script to get the URL and enter URL to web browser. check firewall and proxy server settings if u cannot access on browser

#B
#==>Altering(adding) the web content of the application
from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route('/')
def index():
    greeting='Hello Guru Da Ghostman' 
    return render_template('index.html',greeting=greeting) 
if __name__=='__main__':
    app.run() 


#==>From the index.html file
#{% %} marks pieces of codes to be excecuted, while {{ }} marks variables to be converted to text in html output
#This index.html file is a template that contains the web content served to users using http or https protocol
#Any palce use see {% greeting %} or $greeting, will be a variable u will pass to alter the web content    
#Export the index.html file to the python file with the application code

#C
#==>Getting user input from a browser using "forms"
from flask import Flask
from flask import render_template
from flask import request
app=Flask(__name__)

@app.route("/hello")  #this URL will be http://localhost:5000/hello
def index():
    name=request.args.get('name','Guru') #"request.args" is used to get data from the browser
    #greet=request.args.get('greet','hello') #example of another parameter on the URL cuz we are not restricted to just one
    if name:
        greeting=f'Hello,{name}'
        #greeting=f'{greet},{name}'     #This is the 2nd parameter we can use
    else:
        greeting='Hello Guru'
    return render_template('index.html', greeting=greeting)
if __name__=='__main__':
    app.run() 

#For a user to 'input' data into the browser he/she uses the URL e.g http://localhost:5000/hello?name=BENBELLA
# Hence multiple users can enter their individual inputs    
'''

#D
#Creating an HTML "POST form" with a tag in it to collect user details and send to the web application
from flask import Flask
from flask import render_template
from flask import request
app=Flask(__name__)

@app.route('/hello', methods=['POST','GET'])
def index():
    greeting='Hello Guru'

    if request.method=='POST':
        name=request.form['name']
        greet=request.form['greet']
        greeting=f'{greet},{name}'
        return render_template('index.html', greeting=greeting)
    else:
        return render_template('hello_form.html') #create the hello_form.html file in the templates directory
                                                  #the hello_form.html contains the "Form" configurations
if __name__=="__main__":
    app.run()

'''
Also notice that instead of just a GET method inside class index, I have another method called POST. 
The application works as follows:
1)The request goes to the index() function and the "if-condition" checks the request method for either POST or GET
This is how the browser tells the app that a request is either form submission or URL parameters
2)If the request method is POST,the app will return the message already filled out and submitted
But If the request method is anything else, the app will return the form for user to fill out
'''