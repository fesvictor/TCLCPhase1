""" 
NOTE : To run pytest on this file, you have to be in the parent directory of this file
"""

import pytest
from TCLCPhase1.AnalysisLib.process_file.get_object_list import get_object_list
from TCLCPhase1.AnalysisLib.Party import Party

def test_1():
    # it should throw error if the object_type passed in is unrecognizable
    with pytest.raises(Exception):
        object_type = "hello"
        get_object_list(object_type, "")

def test_party():
    result = get_object_list("party", "../tests/sample_data/target")
    expected = [
        Party("amanah"),
        Party("bn"),
        Party("dap"),
    ]
    assert result == expected

