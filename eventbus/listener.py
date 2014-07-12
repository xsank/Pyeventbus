__author__ = 'Xsank'
from event import Event
from exception import EventTypeError


def check_event(valid_type):
    def decorate(func):
        def _decrator(obj,param):
            if isinstance(param,valid_type):
                func(obj,param)
            elif not isinstance(param,Event):
                raise EventTypeError
        return _decrator
    return decorate


class Listener(object):
    '''This is the base class of all the listeners'''
    pass