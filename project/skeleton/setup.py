try:
    from setuptools import setup #setup function is defined in the setuptools module
except ImportError:
    from distutils.core import setup

config={
    'description':'my project',
    'author':'Benbella',
    'url':'URL to get it at.',
    'download_url':'where to download it from.',
    'authore_mail':'ngembane25@gmail.com',
    'version':'0.1',
    'install_requires':['nose'],#a list of other Python packages that must be installed for this package to work properly.
    'packages':['NAME'],# a list of the package's subdirectories that contain Python code that should be included in the distribution.
    'scripts':[],#a list of scripts that should be installed along with the package.
    'name':'MyProject' #the name of the package.
    }
setup(**config) #'**config':syntax used to pass a dictionary of the config options to the setup function
#setup(**config):this is a function called in the setup.py file used to configure and package the python project
