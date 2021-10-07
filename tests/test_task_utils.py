
import os
from freshtasks.task_utils import TaskUtils
from freshtasks.api import Api

class TestTaskUtils:

    api_key = os.environ["ENV_FRESH_SERVICE_KEY_API_B64"]
    domain = os.environ["ENV_VALUE_DOMAIN_FRESHSERVICE_CKO"]
    ticket = "#CHN-7"

    def test_get_open_tasks_NormalData(self):
        # Arrange
        expected_size = 3

        # Act
        api = Api(self.api_key, self.domain)
        tasks = api.load_tasks(self.ticket)
        task_utils = TaskUtils(tasks)
        open_tasks = task_utils.get_open()
        result = len(open_tasks)
        
        # Assert
        assert result == expected_size

    def test_get_open_tasks_ClosedTasksOnly(self):
        # Arrange
        expected_size = 0
        ticket = "#CHN-8"

        # Act
        api = Api(self.api_key, self.domain)
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
        expected_size = 0

        # Act
        api = Api(self.api_key, self.domain)
        tasks = api.load_tasks(self.ticket)
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
        expected_size = 1

        # Act
        api = Api(self.api_key, self.domain)
        tasks = api.load_tasks(self.ticket)
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

    def test_get_completed_tasks_ClosedTasksOnly(self):
        # Arrange
        expected_size = 2
        ticket = "#CHN-8"

        # Act
        api = Api(self.api_key, self.domain)
        tasks = api.load_tasks(ticket)
        task_utils = TaskUtils(tasks)
        open_tasks = task_utils.get_completed()
        result = len(open_tasks)
        
        # Assert
        assert result == expected_size

    def test_matchxact_one_by_keyword_Existing(self):
        # Arrange
        keyword = "My-Change"
        expected_title = "My-Change"

        # Act
        api = Api(self.api_key, self.domain)
        tasks = api.load_tasks(self.ticket)
        task_utils = TaskUtils(tasks)
        filtered_task = task_utils.matchxact_one_by_keyword(keyword)
        result = filtered_task.title

        # Assert
        assert result == expected_title

    def test_matchxact_one_by_keyword_NonExisting(self):
        # Arrange
        keyword = "My-Changes"
        expected_result = None

        # Act
        api = Api(self.api_key, self.domain)
        tasks = api.load_tasks(self.ticket)
        task_utils = TaskUtils(tasks)
        result = task_utils.matchxact_one_by_keyword(keyword)

        # Assert
        assert result == expected_result

    def test_matchword_one_by_keyword_Existing(self):
        # Arrange
        keyword = "my-change"
        expected_title = "my-change"

        # Act
        api = Api(self.api_key, self.domain)
        tasks = api.load_tasks(self.ticket)
        task_utils = TaskUtils(tasks)
        filtered_task = task_utils.matchword_one_by_keyword(keyword)
        result = filtered_task.title

        # Assert
        assert result == expected_title

    def test_matchword_one_by_keyword_NonExisting(self):
        # Arrange
        keyword = "mychange"
        expected_result = None

        # Act
        api = Api(self.api_key, self.domain)
        tasks = api.load_tasks(self.ticket)
        task_utils = TaskUtils(tasks)
        result = task_utils.matchword_one_by_keyword(keyword)

        # Assert
        assert result == expected_result
    
    def test_matchxact_all_by_keyword_Existing(self):
        # Arrange
        keyword = "my-change"
        expected_size = 1

        # Act
        api = Api(self.api_key, self.domain)
        tasks = api.load_tasks(self.ticket)
        task_utils = TaskUtils(tasks)
        filtered_taks = task_utils.matchxact_all_by_keyword(keyword)
        result = len(filtered_taks)

        # Assert
        assert result == expected_size
    
    def test_matchxact_all_by_keyword_NonExisting(self):
        # Arrange
        keyword = "mychange"
        expected_size = 0

        # Act
        api = Api(self.api_key, self.domain)
        tasks = api.load_tasks(self.ticket)
        task_utils = TaskUtils(tasks)
        filtered_taks = task_utils.matchxact_all_by_keyword(keyword)
        result = len(filtered_taks)

        # Assert
        assert result == expected_size
    
    def test_matchword_all_by_keyword_Existing(self):
        # Arrange
        keyword = "my-change"
        expected_size = 2

        # Act
        api = Api(self.api_key, self.domain)
        tasks = api.load_tasks(self.ticket)
        task_utils = TaskUtils(tasks)
        filtered_taks = task_utils.matchword_all_by_keyword(keyword)
        result = len(filtered_taks)

        # Assert
        assert result == expected_size
    
    def test_matchword_all_by_keyword_NonExisting(self):
        # Arrange
        keyword = "mychange"
        expected_size = 0

        # Act
        api = Api(self.api_key, self.domain)
        tasks = api.load_tasks(self.ticket)
        task_utils = TaskUtils(tasks)
        filtered_taks = task_utils.matchword_all_by_keyword(keyword)
        result = len(filtered_taks)

        # Assert
        assert result == expected_size