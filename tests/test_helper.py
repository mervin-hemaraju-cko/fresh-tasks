import pytest
import freshtasks.utils.helper as Helper

class TestApi:

    testdata = [
        ("#CHN-12", "#CHN-12"),
        ("CHN-12", "#CHN-12"),
        ("#SR-12", "#SR-12"),
        ("SR-12", "#SR-12"),
        ("#PRB-12", "#PRB-12"),
        ("PRB-12", "#PRB-12"),
        ("#INC-12", "#INC-12"),
        ("INC-12", "#INC-12"),
    ]
    @pytest.mark.parametrize("ticket_number,expected_result", testdata)
    def test_reformat_ticket_number(self,ticket_number,expected_result):

        # Act
        result = Helper.reformat_ticket_number(ticket_number)
            
        # Assert
        assert result == expected_result
    
        
    testdata = [
        ("#CHN-1","#CHN", "1"),
        ("#INC-12","#INC", "12"),
        ("#PRB-34","#PRB", "34"),
        ("#SR-1234","#SR", "1234"),
    ]
    @pytest.mark.parametrize("ticket,expected_type,expected_number", testdata)
    def test_ticket_extract(self,ticket,expected_type,expected_number):
        # Arrange

        # Act
        result_type,result_number = Helper.ticket_extract(ticket)
            
        # Assert
        assert result_type == expected_type
        assert result_number == expected_number