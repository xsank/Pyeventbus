Pyeventbus
====================


Pyeventbus is designed to process the traditional event more easilly.You need only write your event message and your
listeners and post the event at the right time. The event message will be process well.The Pyeventbus support simple 
synchronous and asynchronous event handling.

License: MIT (see LICENSE)

Installation and Dependencies
-----------------------------

Install Pyeventbus 

git clone https://github.com/xsank/Pyeventbus

python setup.py install


Example
-------

.. code-block:: python

    from eventbus.eventbus import EventBus
    #now create a eventbus,the default pool size is 4
    eventbus=EventBus()
    
    
    #add the listener to eventbus so it will use the right handler to process the event
    eventbus.register(Listener())
    
    
    #now the event message were sent,eventbus will process
    eventbus.async_post(GreetEvent())
    
    
    #remove the listener
    eventbus.unregister(Listener())
    
    

Information
-----------
1.Your event must inherit from the Event
2.Your listener must inherit from the Listener
3.When you write your own listeners,You would better note the event message type so the eventbus will use the right handler to process it.
    
You can see the complete example in the example directory.
