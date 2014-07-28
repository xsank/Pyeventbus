__author__ = 'Xsank'
import inspect
import thread
from multiprocessing.pool import ThreadPool
from threading import Condition
from threading import Thread

from listener import Listener
from util import Singleton
from exception import RegisterError
from exception import UnregisterError


class EventBus(object):
    __metaclass__=Singleton

    def __init__(self,pool_size=4):
        super(EventBus,self).__init__()
        self.listeners=dict()
        self.pool=ThreadPool(pool_size)
        self.events=list()
        self.con=Condition()
        self.init()

    def init(self):
        thread.start_new_thread(self.loop,())

    def loop(self):
        while True:
            self.con.acquire()
            while not self.events:
                self.con.wait()
            self.pool.map(self.process,self.events)
            self.events=list()
            self.con.release()

    def register(self,listener):
        if not isinstance(listener,Listener):
            raise RegisterError
        self.listeners[listener.__class__.__name__]=listener

    def unregister(self,listener):
        try:
            self.listeners.pop(listener.__class__.__name__)
        except Exception:
            raise UnregisterError

    def process(self,event):
        for listener in self.listeners.values():
            for name,func in inspect.getmembers(listener,predicate=inspect.ismethod):
                func(event)

    def post(self,event):
        self.process(event)

    def async_post(self,event):
        self.con.acquire()
        self.events.append(event)
        self.con.notifyAll()
        self.con.release()

    def destroy(self):
        self.listeners.clear()
        self.pool.close()