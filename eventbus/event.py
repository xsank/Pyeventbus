__author__ = 'Xsank'


class Event(object):
    '''
    This is the baseclass of all the events.
    Your event have to be inheritanced from it. Otherwise the eventbus
    will throw the EventtypeError exception when post it.
    '''
    @classmethod
    def id(cls):
        '''
        Use this method to get event ID.
        :param: None
        :return: str
        '''
        return cls.__name__
