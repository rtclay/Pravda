'''
Created on Sep 26, 2018

@author: cat_t
'''
from Pravda import LeadershipMechanism


class AbsoluteDictatorship(LeadershipMechanism):
    '''
    classdocs
    '''


    def __init__(self, params, person):
        '''
        Constructor
        '''
        self.participants = [person]
    
    