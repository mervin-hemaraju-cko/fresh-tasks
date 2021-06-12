import requests, json
from .task import Task
from .utils import constants as Const

class Api():

    __ticket_dict = {
        "#SR" : "tickets",
        "#INC": "tickets",
        "#CHN": "changes",
        "#PRB": "problems"
    }

    # Initialize the Instance class
    def __init__(self, api_key, domain) -> None:
        self. api_key = api_key
        self.domain = domain

    def __create_url(self, ticket_type, ticket_number) -> str:
        return Const.API_URL_TEMPLATE.format(
            self.domain, 
            self.__ticket_dict.get(ticket_type),
            ticket_number
        )

    def __load_raw_tasks(self, ticket):

        # Split to get ticket type and number
        ticket_params = ticket.split(Const.FLAG_TICKET_SEPARATOR)

        # Check if split was successful
        if(len(ticket_params) != 2):
            raise IndexError(Const.EXCEPTION_FORMAT_TICKET)

        # Fetch params    
        ticket_type = ticket_params[0]
        ticket_number = ticket_params[1]

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

        raw_tasks = self.__load_raw_tasks(ticket)
        tasks = []

        for raw_task in raw_tasks:
            tasks.append(Task(raw_task))
        
        return tasks
