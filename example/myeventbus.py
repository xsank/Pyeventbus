__author__ = 'Xsank'
from eventbus.eventbus import EventBus

from myevent import GreetEvent
from myevent import ByeEvent
from mylistener import MyListener


if __name__=="__main__":
    eventbus=EventBus()
    eventbus.register(MyListener())
    ge=GreetEvent('world')
    be=ByeEvent('world')
    eventbus.post(ge)
    eventbus.async_post(be)
    eventbus.unregister(MyListener())