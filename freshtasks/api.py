import requests, json
from .task import Task
from .utils import constants as Const
from freshtasks.utils.helper import ticket_extract

class Api():

    # Initialize the Instance class
    def __init__(self, api_key, domain) -> None:
        self. api_key = api_key
        self.domain = domain

    def __create_url(self, ticket_type, ticket_number) -> str:

        # Create the URL template
        return Const.API_URL_TEMPLATE.format(
            self.domain, 
            Const.ticket_dict.get(ticket_type),
            ticket_number
        )

    def __load_raw_tasks(self, ticket):

        # Retrieve ticket params
        ticket_type, ticket_number = ticket_extract(ticket)

        # Construct ticket URL
        ticket_url = self.__create_url(ticket_type, ticket_number)

        # Build headers for FreshService call
        headers = Const.require_api_headers_template(self.api_key)

        # Get tasks from API FreshService
        response = requests.get(ticket_url, headers=headers)

        # Checks if GET call is successfull
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(Const.EXCEPTION_HTTP_API)

        # Format and load tasks
        return json.loads(response.content)[Const.KEYWORD_API_TASKS]

    def load_tasks(self, ticket):

        # Load the tasks
        raw_tasks = self.__load_raw_tasks(ticket)

        # Iterate through all tasks and append to empty task list
        # Return the task list
        return [Task(rt) for rt in raw_tasks]
    
    def close_task(self, ticket, task_id):
        # Retrieve ticket params
        ticket_type, ticket_number = ticket_extract(ticket)

        # Construct ticket URL
        ticket_url = self.__create_url(ticket_type, ticket_number)

        # Construct task update URL
        task_update_url = f"{ticket_url}/{task_id}"

        # Update the ticket status
        response = requests.put(
            task_update_url, 
            headers=Const.require_api_headers_template(self.api_key), 
            data=json.dumps(Const.DICT_API_TASK_CLOSE)
        )

        # Checks if update is successfull
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(Const.EXCEPTION_HTTP_API_UPDATE)