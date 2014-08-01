__author__ = 'Xsank'
from eventbus.listener import Listener
from eventbus.listener import add_event

from myevent import GreetEvent
from myevent import ByeEvent


class MyListener(Listener):
    @add_event(GreetEvent)
    def greet(self,event=None):
        print 'hello',event.name

    @add_event(ByeEvent)
    def goodbye(self,event=None):
        print 'bye',event.name


