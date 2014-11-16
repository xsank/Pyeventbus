__author__ = 'Xsank'


class EventbusException():
    '''This is the base exception of the Eventbus.'''
    def __str__(self):
        return self.__doc__


class EventTypeError(EventbusException):
    '''Event type is invalid!'''


class ListenerTypeError(EventbusException):
    '''Listener type is invalid!'''


class UnregisterError(EventbusException):
    '''No listener to unregister!'''


class ProcessException(EventbusException):
    '''Post message but no listener related register!'''


class InstanceException(EventbusException):
    '''The class can only be instantiated once!'''


class TaskFullException(EventbusException):
    '''Too many tasks to finished!'''