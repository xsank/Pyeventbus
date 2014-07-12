__author__ = 'Xsank'


class EventTypeError(Exception):
    '''Event type is invalid!'''

    def __str__(self):
        return self.__doc__


class UnregisterError(Exception):
    '''No listener to unregister!'''

    def __str__(self):
        return self.__doc__