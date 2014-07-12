__author__ = 'Xsank'
import inspect

from listener import Listener
from exception import RegisterError
from exception import UnregisterError


class EventBus(object):
    def __init__(self):
        self.listeners=dict()

    def register(self,listener):
        if not isinstance(listener,Listener):
            raise RegisterError
        self.listeners[listener.__class__.__name__]=listener

    def unregister(self,listener):
        try:
            self.listeners.pop(listener.__class__.__name__)
        except Exception:
            raise UnregisterError

    def post(self,event):
        for listener in self.listeners.values():
            for name,func in inspect.getmembers(listener,predicate=inspect.ismethod):
                func(event)

    def destroy(self):
        self.listeners.clear()