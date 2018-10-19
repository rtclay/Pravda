'''
Created on Sep 30, 2018

@author: cat_t
'''

class Edge(object):
    '''
    classdocs
    '''


    def __init__(self, start, end, cost = 1):
        '''
        Constructor
        '''
        self.start = start
        self.end = end
        self.cost = cost
    