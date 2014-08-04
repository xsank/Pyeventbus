__author__ = 'Xsank'


class Event(object):
    '''This is the baseclass of all the events'''
    @classmethod
    def id(cls):
        return cls.__name__
