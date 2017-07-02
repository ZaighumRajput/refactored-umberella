import json
'''
TODO:
    - should data be indexed by quotes, or authors?

'''
class quote(object):
    '''Interface between back-end(data storage) to front-end
    TODO: connect to database
    `
    EXAMPLE
    ---------------
    quote_about_money = quote("Time is money, when it comes to mine take it in blood",
                              "Nas",
                              ["Cicero", "Seneca"]
                              )

    '''
    def __init__(self, quote, author, related_authors):
        self.quote           = quote 
        self.author          = author 
        self.related_authors = related_authors 

    def to_json(self):
        ''' Use to create javascript objects
        '''
        return None

class author(object):
    '''
    Author object

    EXAMPLE
    ---------------
    author   = author("Warren", "Buffet", 1946-0-1) 


    '''

    def __init__(self):
        self.first_name    = ""
        self.last_name     = ""
        self.alias         = None 
        self.date_of_birth = ""
        self.years_active  = ""

        self.image_source  = ""

    def to_json(self):
        ''' Use to create javascript objects
        '''
        return None
