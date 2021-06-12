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