'''
Created on Sep 30, 2018

@author: cat_t
'''

class Location(object):
    '''
    classdocs
    '''


    def __init__(self, name = ""):
        '''
        Constructor
        '''
        self.name = name
        
    def __eq__(self, other):
        try:
            if self.name == other.name:
                return True
            else:
                return False
        except AttributeError:
            return False
    
        return False
    
    def __ne__(self, o):
        return not self == o
    
    def __hash__(self):
        return hash(self.name)