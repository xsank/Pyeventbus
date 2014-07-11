__author__ = 'Xsank'
from eventbus.listener import Listener
from eventbus.exception import EventTypeError

from myevent import MyEvent


def check_event(valid_type):
    def decorate(func):
        def _decrator(obj,param):
            if isinstance(param,valid_type):
                func(obj,param)
            else:
                raise EventTypeError
        return _decrator
    return decorate


class MyListener(Listener):
    @check_event(MyEvent)
    def greet(self,event=None):
        print 'hello',event.name