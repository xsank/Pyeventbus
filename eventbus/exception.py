__author__ = 'Xsank'


class EventbusException():
    def __str__(self):
        return self.__doc__


class EventTypeError(EventbusException):
    '''Event type is invalid!'''


class RegisterError(EventbusException):
    '''Unknow listener to register!'''


class UnregisterError(EventbusException):
    '''No listener to unregister!'''


class ProcessException(EventbusException):
    '''Post message but no listener related regist'''


class InstanceException(EventbusException):
    '''The class can only be instantiated once!'''