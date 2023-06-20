print('\n#App Testing')

#===>A
import unittest
from myapplication.setup import app

class TestHello(unittest.TestCase):    #setUp method is used to create a clean env for each test case
    def setUp(self): #"setUp method" is used to setup the test client for the Flask Application
        self.app=app.test_client()
    #Each Test method verifies a different aspect of the routes taken to access the /hello app    
    #1-Test that /hello app route returns a form when accesed with a GET request
    def test_hello_form(self):
        response=self.app.get('/hello') #when the request method is get,app will return form for user to fill
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Fill Out The Form',response.data)
    
    #2-Test that /hello app route returns a greetings when access with a POST request
    def test_hello_post(self):
        data={'name':'Guru', 'greet':'hello'}
        response=self.app.post('/hello', data=data) #if request methos is post,the app will will return a message already filled out and submitted
        self.assertEqual(response.status_code, 200)  
        self.assertIn(b'Hello, Guru', response.data)  

    #3-Test that /hello app route returns an error message when POST request is missing required params
    def test_hello_post_missing_params(self):
        data={'name':'Guru'}
        response=self.app.post('/hello',data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Bad Request', response.data)    

if __name__=="__main__":
    unittest.main()            
'''
#===>B(This does not use the setUp method)
import unittest
from app import app

class TestApp(unittest.TestCase):
    app.config['TESTING'] = True
    client = app.test_client() 

    def test_index(self):
        # Test if the form is displayed correctly
        response = self.client.get('/hello', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Fill Out This Form", response.data)

        # Test if the form submission works correctly
        data = {'name': 'John', 'greet': 'Hi'}
        response = self.client.post('/hello', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hi, John", response.data)

    def test_not_found(self):
        # Test if a non-existing resource returns a 404 error
        response = self.client.get('/non-existing-url', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
'''
