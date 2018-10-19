'''
Created on Sep 26, 2018

@author: cat_t
'''
from Pravda import Status

class World(object):
    '''
    contains all game state information
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.people
        self.people_locations
        self.locations
        self.groups
        self.people_statuses
        
    def get_living(self):
        return [person for person in self.people if Status.ALIVE in self.people_statuses[person]]
    
    def get_dead(self):
        return [person for person in self.people if Status.DEAD in self.people_statuses[person]]
    
    