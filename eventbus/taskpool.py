__author__ = 'Xsank'


class TaskPool(object):
    '''
    This pool contain all the task the eventbus should be handled.
    '''
    def __init__(self,max_size=100):
        self.max_size=max_size
        self.task_list=list()

    def isempty(self):
        return len(self.tasks)==0

    def add_task(self,task):
        self.tasks.append(task)

    @property
    def task_num(self):
        return len(self.tasks)

    @property
    def tasks(self):
        return self.task_list

    def remove_task(self):
        del self.tasks[:]

    def isfull(self):
        return self.task_num>=self.max_size

    def destroy(self):
        self.remove_task()