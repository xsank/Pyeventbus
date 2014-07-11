__author__ = 'Xsank'
from eventbus.eventbus import EventBus

from myevent import MyEvent
from mylistener import MyListener


if __name__=="__main__":
    eventbus=EventBus()
    eventbus.register(MyListener())
    me=MyEvent('world')
    eventbus.post(me)
    eventbus.unregister(MyListener())