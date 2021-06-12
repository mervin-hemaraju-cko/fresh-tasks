import pytest
import os
from requests.exceptions import HTTPError
from freshtasks.api import Api

class TestApi:

    testdata = [
        ("#CHN","1234", "https://checkoutsupport.freshservice.com/api/v2/changes/1234/tasks"),
        ("#CHN","12345", "https://checkoutsupport.freshservice.com/api/v2/changes/12345/tasks"),
        ("#CHN","123456", "https://checkoutsupport.freshservice.com/api/v2/changes/123456/tasks"),
        ("#CHN","1234567", "https://checkoutsupport.freshservice.com/api/v2/changes/1234567/tasks"),
        ("#PRB","1234", "https://checkoutsupport.freshservice.com/api/v2/problems/1234/tasks"),
        ("#PRB","12345", "https://checkoutsupport.freshservice.com/api/v2/problems/12345/tasks"),
        ("#PRB","123456", "https://checkoutsupport.freshservice.com/api/v2/problems/123456/tasks"),
        ("#PRB","1234567", "https://checkoutsupport.freshservice.com/api/v2/problems/1234567/tasks"),
        ("#INC","1234", "https://checkoutsupport.freshservice.com/api/v2/tickets/1234/tasks"),
        ("#INC","12345", "https://checkoutsupport.freshservice.com/api/v2/tickets/12345/tasks"),
        ("#INC","123456", "https://checkoutsupport.freshservice.com/api/v2/tickets/123456/tasks"),
        ("#INC","1234567", "https://checkoutsupport.freshservice.com/api/v2/tickets/1234567/tasks"),
        ("#SR","1234", "https://checkoutsupport.freshservice.com/api/v2/tickets/1234/tasks"),
        ("#SR","12345", "https://checkoutsupport.freshservice.com/api/v2/tickets/12345/tasks"),
        ("#SR","123456", "https://checkoutsupport.freshservice.com/api/v2/tickets/123456/tasks"),
        ("#SR","1234567", "https://checkoutsupport.freshservice.com/api/v2/tickets/1234567/tasks"),
    ]
    @pytest.mark.parametrize("ticket_type,ticket_number,expected_result", testdata)
    def test_create_url_NormalData(self,ticket_type,ticket_number,expected_result):
        # Arrange
        api_key = "null"
        domain = "checkoutsupport.freshservice.com"

        # Act
        api = Api(api_key, domain)
        result = api._Api__create_url(ticket_type, ticket_number)
            
        # Assert
        assert result == expected_result
    
    def test_load_raw_tasks_NormalData(self):
        # Arrange
        api_key = os.environ["ENV_FRESH_SERVICE_KEY_API_B64"]
        domain = "checkoutsupport.freshservice.com"
        ticket = "#CHN-7303"
        expected_size = 4

        # Act
        api = Api(api_key, domain)
        raw_tasks = api._Api__load_raw_tasks(ticket)
        result = len(raw_tasks)
        
        # Assert
        assert result == expected_size
    
    def test_load_raw_tasks_AbnormalData1Of2(self):
        # Arrange
        api_key = os.environ["ENV_FRESH_SERVICE_KEY_API_B64"]
        domain = "checkoutsupport.freshservice.com"
        ticket = "#CHN7303"
        expected_result = "Incorrect ticket format provided. Please read the docs"

        # Act
        try:
            api = Api(api_key, domain)
            raw_tasks = api._Api__load_raw_tasks(ticket)
            result = len(raw_tasks)

            result = "FAILED"
        except IndexError as e:
            result = str(e)
        
        # Assert
        assert result == expected_result
    
    def test_load_raw_tasks_AbnormalData2Of2(self):
        # Arrange
        api_key = os.environ["ENV_FRESH_SERVICE_KEY_API_B64"]
        domain = "checkoutsupport.freshservice.com"
        ticket = "#CHN-CHN"
        expected_result = "An HTTP error occured with the provided API URL"

        # Act
        try:
            api = Api(api_key, domain)
            raw_tasks = api._Api__load_raw_tasks(ticket)
            result = len(raw_tasks)

            result = "FAILED"
        except HTTPError as e:
            result = str(e)
        
        # Assert
        assert result == expected_result

    def test_load_tasks_NormalData(self):
        # Arrange
        api_key = os.environ["ENV_FRESH_SERVICE_KEY_API_B64"]
        domain = "checkoutsupport.freshservice.com"
        ticket = "#CHN-7303"
        expected_size = 4

        # Act
        api = Api(api_key, domain)
        tasks = api.load_tasks(ticket)
        result = len(tasks)
        
        # Assert
        assert result == expected_size