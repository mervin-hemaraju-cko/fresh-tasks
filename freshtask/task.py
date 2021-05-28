from .utils import constants as Const

class Task:

    def __init__(self, json) -> None:
        self.id  = json[Const.KEYWORD_API_TASK_ID]
        self.title = json[Const.KEYWORD_API_TASK_TITLE]
        self.description = json[Const.KEYWORD_API_TASK_DESCRIPTION]
        self.agent_id = json[Const.KEYWORD_API_TASK_AGENT_ID]
        self.status = json[Const.KEYWORD_API_TASK_STATUS]