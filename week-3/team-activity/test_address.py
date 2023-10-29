from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    """Verify that the extract_city function returns correct results.
    Parameters: none
    Return: nothing
    """
    assert extract_city("123 Main St., Chicago, IL 60654") == "Chicago" 
    
pytest.main(["-v", "--tb=line", "-rN", __file__])