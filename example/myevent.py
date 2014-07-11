__author__ = 'Xsank'
from eventbus.event import Event


class MyEvent(Event):
    def __init__(self,name):
        super(MyEvent,self).__init__()
        self.name=name