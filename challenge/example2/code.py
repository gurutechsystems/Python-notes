'''
-The below code creates a class "lexicon" with 3 methods i.e __init__,go and add_path
-The __init__ function of the class creates the name,description and paths attributes of the lexicon
-The 'go' function takes a direction parameter and return the values of the corresponding directions in "paths" of the lexicon and if the direction is not in the "paths" attribute,it returns None
-The "add_paths" function takes the paths parameter and updates the "paths" attribute of the lexicon with the given paths
'''
class lexicon():
    def __init__(self, name, description):
        self.name=name
        self.description=description
        self.paths={}

    def go(self, direction):
        return self.paths.get(direction,None)

    def add_paths(self,paths):
        return self.paths.update(paths)    