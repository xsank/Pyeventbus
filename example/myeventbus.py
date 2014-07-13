__author__ = 'Xsank'
import time
from eventbus.eventbus import EventBus

from myevent import GreetEvent
from myevent import ByeEvent
from mylistener import MyListener


if __name__=="__main__":
    eventbus=EventBus()
    eventbus.register(MyListener())
    eventbus.start()
    ge=GreetEvent('world')
    be=ByeEvent('world')
    eventbus.post(ge)
    eventbus.async_post(be)
    time.sleep(1)
    eventbus.unregister(MyListener())