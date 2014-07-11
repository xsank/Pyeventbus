__author__ = 'Xsank'


class EventTypeError(Exception):
    '''Event type is invalid!'''


class UnregisterError(Exception):
    '''No listener to unregister!'''