__author__ = 'Xsank'
from eventbus.event import Event


class GreetEvent(Event):
    def __init__(self,name):
        self.name=name


class ByeEvent(Event):
    def __init__(self,name):
        self.name=name