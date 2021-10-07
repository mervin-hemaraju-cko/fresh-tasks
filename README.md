# Freshtasks

Freshtasks is a python library that facilitates the manipulation of tasks associated with [Freshservice](https://freshservice.com/) tickets


# Getting Started

Assuming that you have Python and virtualenv installed, set up your environment and install the required dependencies using pip:

```
pip install freshtasks
```

# Using Freshtasks

After installing freshtasks

You need to import the main Api object and instantiate it to create a connection to freshservice:

```
from freshtasks.api import Api

api = Api(api_key, domain)
```

Here,

`api_key` is your [freshservice api key](https://support.freshservice.com/support/solutions/articles/50000000306-where-do-i-find-my-api-key-) already converted to [Base 64](https://en.wikipedia.org/wiki/Base64).

`domain` is your freshservice domain in the format domain.freshservice.com

When the connection has been initiated, laoding the task is only one line away. Below is the full code to load all tasks:

```
from freshtasks.api import Api

api = Api(api_key, domain)
tasks = api.load_tasks(ticket)
```

```
ticket here is the freshservice ticket number in the following format `#SR-1234` or `SR-2134`
```

# Task Model

Tasks are returned using freshtasks custom made models.

The following attributes are available for a specific task returned:

- id - The unique ID of the freshservice task
- title - The title of the freshservice task
- description - The description of the freshservice task
- agent - The agent assigned to the task
- status - The status of the task, 1-Open, 2-In Progress, 3-Completed

# Task Utils

You can control the outcome of the tasks return in several ways using the Task Utils model in freshtasks.

### Using Task Utils

Below is a sample code on how to use Task Utils:

```
from freshtasks.task_utils import TaskUtils

task_utils = TaskUtils(tasks)

```

Here `tasks` is a list of Task models returned usign the Api model.

Using the `task_utils` object, you can manipulate the outcome in several ways. Below is the full sample on how to return only `open tasks`:

```
from freshtasks.task_utils import TaskUtils

api = Api(self.api_key, self.domain)
tasks = api.load_tasks(self.ticket)
task_utils = TaskUtils(tasks)
open_tasks = task_utils.get_open()

```
The available filters are defined below:

1. Get Open Tasks

    > This filter will extract only open tasks

    > `Function Name` - get_open()

2. Get In Progress Tasks

    > This filter will extract only in progress tasks

    > `Function Name` - get_in_progress()

3. Get Completed Tasks

    > This filter will extract only completed tasks

    > `Function Name` - get_completed()

4. Match Exactly One Keyword in Task Title

    > This filter will match a provided keyword exactly against a task title and will return this task.

    > This method returns ONLY ONE task

    > `Function Name` - matchxact_one_by_keyword()

5. Match Exactly All Keyword in Task Title

    > This filter will match a provided keyword exactly against a task title and will return all tasks matched.

    > `Function Name` - matchxact_all_by_keyword()

6. Match One Keyword in Task Title

    > This filter will match a provided keyword case insensitive against a task title and will return this task.

    > This method returns ONLY ONE task

    > `Function Name` - matchword_one_by_keyword()

7. Match All Keyword in Task Title

    > This filter will match a provided keyword case insensitive against a task title and will return all tasks matched.

    > `Function Name` - matchword_all_by_keyword()


# Closing a task

You can also close a task using freshtasks inbuilt functions. You need to provide the two parameters below for a successful call:

- `ticket` - The freshservice ticket number in the following format `#SR-1234` or `SR-2134`

- `task_id` - The freshservice task id

Below is a full code sample:

```
from freshtasks.api import Api

api = Api(..., ...)
api.close_task(TICKET_HERE, TASK_ID_HERE)
```


# Running Tests
You can run the tests by following the steps below:

1. Clone or download the project to a folder
2. Create a file named `secret.env`
3. Add the following variables as follows in the env file:

```
export ENV_FRESH_SERVICE_KEY_API_B64="YOUR_API_KEY"
export ENV_VALUE_DOMAIN_FRESHSERVICE_CKO="domain.freshservice.com"
```
4. Run the tests using the command `./run_test.sh`

# License
```
Copyright Mervin Hemaraju
```