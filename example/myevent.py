__author__ = 'Xsank'
from eventbus.event import Event


class GreetEvent(Event):
    def __init__(self,name):
        super(GreetEvent,self).__init__()
        self.name=name


class ByeEvent(Event):
    def __init__(self,name):
        super(ByeEvent,self).__init__()
        self.name=name