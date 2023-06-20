from nose.tools import * #'*' will import all functions(names) from the nose.tools module into the cureent namespace
import NAME

def setup():
    print('setup')

def teardown():
    print('tear down')

def test_basic():
    print('basic test')    