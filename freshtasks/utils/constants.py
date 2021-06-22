
###############################################################
############## All constants values resides here ##############
###############################################################

API_URL_TEMPLATE = "https://{}/api/v2/{}/{}/tasks"

FLAG_TICKET_SEPARATOR = "-"

KEYWORD_API_TASKS = "tasks"
KEYWORD_API_TASK_ID = "id"
KEYWORD_API_TASK_TITLE = "title"
KEYWORD_API_TASK_DESCRIPTION = "description"
KEYWORD_API_TASK_STATUS = "status"
KEYWORD_API_TASK_AGENT_ID = "agent_id"

VALUE_API_TASK_STATUS_OPEN = 1
VALUE_API_TASK_STATUS_IPROG = 2
VALUE_API_TASK_STATUS_COMPLETED = 3

EXCEPTION_FORMAT_TICKET = "Incorrect ticket format provided. Please read the docs"
EXCEPTION_HTTP_API = "An HTTP error occured with the provided API URL"
EXCEPTION_HTTP_API_UPDATE = "An HTTP error occured when trying to update the task"

# Dictionary Templates

# List of possible ticket ops
ticket_dict = {
    "#SR" : "tickets",
    "#INC": "tickets",
    "#CHN": "changes",
    "#PRB": "problems"
}

DICT_API_TASK_CLOSE = {"status": 3}

def require_api_headers_template(api_key):
    return {"Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Basic {api_key}"}