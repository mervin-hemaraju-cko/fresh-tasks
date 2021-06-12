
import os
from freshtasks.task_utils import TaskUtils
from freshtasks.api import Api

class TestTaskUtils:

    def test_get_open_tasks_NormalData(self):
        # Arrange
        api_key = os.environ["ENV_FRESH_SERVICE_KEY_API_B64"]
        domain = "checkoutsupport.freshservice.com"
        ticket = "#CHN-7303"
        expected_size = 3

        # Act
        api = Api(api_key, domain)
        tasks = api.load_tasks(ticket)
        task_utils = TaskUtils(tasks)
        open_tasks = task_utils.get_open()
        result = len(open_tasks)
        
        # Assert
        assert result == expected_size
    
    def test_get_open_tasks_EmptyData(self):
        # Arrange
        tasks = []
        expected_size = 0

        # Act
        task_utils = TaskUtils(tasks)
        open_tasks = task_utils.get_open()
        result = len(open_tasks)
        
        # Assert
        assert result == expected_size

    def test_get_in_progress_tasks(self):
        # Arrange
        api_key = os.environ["ENV_FRESH_SERVICE_KEY_API_B64"]
        domain = "checkoutsupport.freshservice.com"
        ticket = "#CHN-7303"
        expected_size = 0

        # Act
        api = Api(api_key, domain)
        tasks = api.load_tasks(ticket)
        task_utils = TaskUtils(tasks)
        open_tasks = task_utils.get_in_progress()
        result = len(open_tasks)
        
        # Assert
        assert result == expected_size
    
    def test_get_in_progress_EmptyData(self):
        # Arrange
        tasks = []
        expected_size = 0

        # Act
        task_utils = TaskUtils(tasks)
        open_tasks = task_utils.get_in_progress()
        result = len(open_tasks)
        
        # Assert
        assert result == expected_size

    def test_get_completed_tasks(self):
        # Arrange
        api_key = os.environ["ENV_FRESH_SERVICE_KEY_API_B64"]
        domain = "checkoutsupport.freshservice.com"
        ticket = "#CHN-7303"
        expected_size = 1

        # Act
        api = Api(api_key, domain)
        tasks = api.load_tasks(ticket)
        task_utils = TaskUtils(tasks)
        open_tasks = task_utils.get_completed()
        result = len(open_tasks)
        
        # Assert
        assert result == expected_size

    def test_get_completed_EmptyData(self):
        # Arrange
        tasks = []
        expected_size = 0

        # Act
        task_utils = TaskUtils(tasks)
        open_tasks = task_utils.get_completed()
        result = len(open_tasks)
        
        # Assert
        assert result == expected_size