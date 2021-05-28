from .utils import constants as Const

class TaskUtils:

    def __init__(self, task_list) -> None:
        self.tasks = task_list

    def get_open(self):
        return list(filter(lambda t: t.status == Const.VALUE_API_TASK_STATUS_OPEN, self.tasks))
    
    def get_in_progress(self):
        return list(filter(lambda t: t.status == Const.VALUE_API_TASK_STATUS_IPROG, self.tasks))
    
    def get_completed(self):
        return list(filter(lambda t: t.status == Const.VALUE_API_TASK_STATUS_COMPLETED, self.tasks))