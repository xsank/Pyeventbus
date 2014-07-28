__author__ = 'Xsank'
import time
from eventbus.eventbus import EventBus

from myevent import GreetEvent
from myevent import ByeEvent
from mylistener import MyListener


if __name__=="__main__":
    eventbus=EventBus()
    eventbus.register(MyListener())
    ge=GreetEvent('world')
    be=ByeEvent('world')
    eventbus.async_post(be)
    eventbus.post(ge)
    time.sleep(0.1)
    eventbus.unregister(MyListener())
    eventbus.destroy()