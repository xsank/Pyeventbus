__author__ = 'Xsank'
from eventbus.listener import Listener
from eventbus.listener import check_event

from myevent import GreetEvent
from myevent import ByeEvent


class MyListener(Listener):
    @check_event(GreetEvent)
    def greet(self,event=None):
        print 'hello',event.name

    @check_event(ByeEvent)
    def goodbye(self,event=None):
        print 'bye',event.name

