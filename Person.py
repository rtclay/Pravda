'''
Created on Sep 26, 2018

@author: cat_t
'''
from Pravda import Speech

class Person(object):
    '''
    classdocs
    '''
    identifier = 0

    def __init__(self, params):
        '''
        Constructor
        '''
        self.TrueName = ""
        self.aliases ={}
        self.location
        self.goals ={}
        self.interest_checks = {}
        self.identifier = Person.identifier
        Person.identifier += 1
        
        self.consumption_rate = 1
        
    def pick_action(self, action_score_tuples):
        raise NotImplementedError
    
    def get_actions(self):
        raise NotImplementedError
    
    def score_actions(self):
        raise NotImplementedError
        
    def score_action(self, action, scoring_function):
        outcome = self.expected_worldstate_after_action(action)
        return self.trivial_score(outcome)
        #return scoring_function(self.goals, outcome)
    
    def generate_rules_from_goals(self):
        self.interest_checks = [goal.to_rules(self) for goal in self.goals]
    
    
    def expected_worldstate_after_action(self, action):
        pass

    def trivial_score(self, world):
        score = 0
        score += self.is_alive(world)
    
    def make_statement(self, statement, medium ):
        pass
    
    def take_document(self):
        pass
    
    def put_document(self):
        pass
    
    def move(self, destination):
        pass
    
    def is_alive(self, world):
        return self in world.get_living_people()