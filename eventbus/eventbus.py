__author__ = 'Xsank'
import thread
from multiprocessing.pool import ThreadPool
from threading import Condition

from event import Event
from taskpool import TaskPool
from listener import Listener
from util import Singleton
from exception import EventTypeError
from exception import ListenerTypeError
from exception import UnregisterError
from exception import ProcessException
from exception import TaskFullException


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

    def __init__(self,pool_size=4,task_size=100):
        super(EventBus,self).__init__()
        self.pool=ThreadPool(pool_size)
        self.async_events=TaskPool(task_size)
        self.event_handlers=dict()
        self.con=Condition()
        self.init()

    def init(self):
        thread.start_new_thread(self.loop,())

    @check_listener
    def register(self,listener):
        '''
        Use this method to register your listener to the eventbus
        and please before you post.
        :param listener: The listener have to be inheritanced from the Listener.
        :return: None
        '''
        self.event_handlers.update(listener.event_handlers)

    @check_listener
    def unregister(self,listener):
        '''
        This method will remove the listener from the eventbus so
        that your listener will not process the event.
        :param listener: The listener have to be inheritanced from the Listener.
        :return: None
        '''
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
        '''
        Post your event when you need. The listener you registed will process it.
        And this is a sync method. It will not return until it complete.
        :param event: The event have to be inheritanced from the Event.
        :return: None
        '''
        self.process(event)

    @check_event
    def async_post(self,event):
        '''
        Post your event when you need. The listener you registed will process it.
        And this is a async method. You just post the event and it will not hold on
        your main thread.
        :param event: The event have to be inheritanced from the Event.
        :return: None
        '''
        with self.con:
            self.async_events.add_task(event)
            self.con.notifyAll()

    def loop(self):
        while True:
            with self.con:
                while self.async_events.isempty():
                    self.con.wait()
                if self.async_events.isfull():
                    raise TaskFullException
                else:
                    self.pool.map(self.process,self.async_events.tasks)
                    self.async_events.remove_task()

    def destroy(self):
        '''
        If you don't want to use it anymore. Use this method to release the resource.
        :param: None
        :return: None
        '''
        self.event_handlers.clear()
        self.pool.close()
        self.async_events.destroy()