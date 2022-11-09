import pytest
from extra_espacios import EliminatedSpaces

def test_compare_last_char():
    string = "abc  de fg h i  jkl   mn   ño  q    r"
    a = EliminatedSpaces(string)
    
    assert a.compare_last_char() == [4,15,20,21,25,26,30,33,34,35]

def test_clean_clone_text():
    string = "abc  de fg h i  jkl   mn   ño  q    r"
    a = EliminatedSpaces(string)
    
            


    