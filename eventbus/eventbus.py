__author__ = 'Xsank'
import inspect
import thread
from multiprocessing.pool import ThreadPool
from threading import Condition

from event import Event
from listener import Listener
from util import Singleton
from exception import EventTypeError
from exception import RegisterError
from exception import UnregisterError
from exception import ProcessException


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

    def register(self,listener):
        if not isinstance(listener,Listener):
            raise RegisterError

        for name,func in EventBus.get_listener_handlers(listener):
            if func.event in self.event_handlers:
                self.event_handlers[func.event].append(func)
            else:
                self.event_handlers[func.event]=[func]

    def unregister(self,listener):
        try:
            for name,func in EventBus.get_listener_handlers(listener):
                del self.event_handlers[func.event]
        except Exception:
            raise UnregisterError

    def process(self,event):
        handlers=self.event_handlers[event.__class__.__name__]
        if not handlers:
            raise ProcessException

        for handler in handlers:
            handler(event)

    def post(self,event):
        if not isinstance(event,Event):
            raise EventTypeError
        self.process(event)

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

    @staticmethod
    def get_listener_handlers(listener):
        return inspect.getmembers(listener,predicate=inspect.ismethod)

    def destroy(self):
        self.event_handlers.clear()
        self.pool.close()