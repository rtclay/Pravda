class Goal(object):
    '''
    Is an objective that people or groups work towards
    '''


    def __init__(self, name, description, progress_function):
        '''
        Constructor
        '''
        self.name = name
        self.description = description
        self.progress_function = progress_function
        
    def compare_worldstates(self, first_metrics, second_metrics):
        '''
        compare two scoresheets and determine how much better the first one is than the second, according to the goal
        returns:
        -1 first is very much worse than second
        -1 to 0 first is worse than second
        0 first is equal to second
        0 to 1 
        1 first is very much better than second
        
        '''
        
        pass
    
    def to_rules(self, world):
        
        pass
    
    
Goals = set()
Goals.add(
    Goal("Avoid Deaths","Avoid civilian deaths", )
    
    )
    
STAY_ALIVE = Goal("Stay Alive", "Remain living", 
                  lambda x: x.is_alive()
                  )
    