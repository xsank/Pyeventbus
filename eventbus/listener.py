__author__ = 'Xsank'


def add_event(valid_type):
    def decorate(func):
        setattr(func,'event',valid_type.__name__)
        return func
    return decorate


class Listener(object):
    '''This is the base class of all the listeners'''