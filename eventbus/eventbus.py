__author__ = 'Xsank'
import thread
from multiprocessing.pool import ThreadPool
from threading import Condition

from event import Event
from listener import Listener
from util import Singleton
from exception import EventTypeError
from exception import ListenerTypeError
from exception import UnregisterError
from exception import ProcessException


def check_type(valid_type,exception):
    def decorator(func):
        def _decorator(obj,_type):
            if isinstance(_type,valid_type):
                func(obj,_type)
            else:
                raise exception
        return _decorator
    return decorator


check_event=check_type(Event,EventTypeError)
check_listener=check_type(Listener,ListenerTypeError)


class EventBus(object):
    __metaclass__=Singleton

    def __init__(self,pool_size=4):
        super(EventBus,self).__init__()
        self.pool=ThreadPool(pool_size)
        self.async_events=list()
        self.event_handlers=dict()
        self.con=Condition()
        self.init()

    def init(self):
        thread.start_new_thread(self.loop,())

    @check_listener
    def register(self,listener):
        self.event_handlers.update(listener.event_handlers)

    @check_listener
    def unregister(self,listener):
        try:
            for event in listener.event_handlers:
                del self.event_handlers[event]
        except Exception:
            raise UnregisterError

    def process(self,event):
        handlers=self.event_handlers[event.id()]
        if not handlers:
            raise ProcessException

        for handler in handlers:
            handler(event)

    @check_event
    def post(self,event):
        self.process(event)

    @check_event
    def async_post(self,event):
        self.con.acquire()
        self.async_events.append(event)
        self.con.notifyAll()
        self.con.release()

    def loop(self):
        while True:
            self.con.acquire()
            while not self.async_events:
                self.con.wait()
            self.pool.map(self.process,self.async_events)
            self.async_events=list()
            self.con.release()

    def destroy(self):
        self.event_handlers.clear()
        self.pool.close()