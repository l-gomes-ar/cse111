from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make_full_name function works properly
    Parameters: None
    Returns: Nothing
    """
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Stephanie Samo", "Gonzalez" ) == "Gonzalez; Stephanie Samo"
    assert make_full_name("Jonah", "Torres-Gomes") == "Torres-Gomes; Jonah"
    assert make_full_name("", "") == "; "
    
def test_extract_family_name():
    """Verify that the extract_family_name functions works properly
    Parameters: None
    Returns: Nothing.
    """
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Gonzalez; Stephanie Samo") == "Gonzalez"
    assert extract_family_name("Torres-Gomes; Jonah") == "Torres-Gomes"
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    """Verfiy that the extract_given_name function works properly
    Parameters: None
    Returns: Nothing
    """
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Gonzalez; Stephanie Samo") == "Stephanie Samo"
    assert extract_given_name("Torres-Gomes; Jonah") == "Jonah"
    assert extract_given_name("; ") == ""



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])