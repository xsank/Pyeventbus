__author__ = 'Xsank'
import inspect


def add_event(valid_type):
    def decorate(func):
        setattr(func,'event',valid_type.__name__)
        return func
    return decorate


class Listener(object):
    '''This is the base class of all the listeners'''
    def __init__(self):
        self.event_handlers=dict()
        self.init_event_handlers()

    def init_event_handlers(self):
        for name,func in self.get_handlers():
            if func.event in self.event_handlers:
                self.event_handlers[func.event].append(func)
            else:
                self.event_handlers[func.event]=[func]

    def get_handlers(self):
        funcs=inspect.getmembers(self,predicate=inspect.ismethod)
        return [(name,func) for name,func in funcs if hasattr(func,'event')]