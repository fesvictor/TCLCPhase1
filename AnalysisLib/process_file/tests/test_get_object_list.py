import pytest
from TCLCPhase1.AnalysisLib.process_file.get_object_list import get_object_list
def test_1():
    # it should throw error if the object_type passed in is unrecognizable
    with pytest.raises(Exception):
        object_type = "hello"
        get_object_list(object_type)

def test_2():
    object_type = "party"
    result = get_object_list(object_type)
    print(result[0])
