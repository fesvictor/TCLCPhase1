from TCLCPhase1.AnalysisLib.BaseObject import BaseObject

def test_constructor():
    x = BaseObject("Barisan National")
    assert x.name == "Barisan National"
    assert x.negative == 0
    assert x.positive == 0

def test_get_name():
    x = BaseObject("Rocket")
    assert x.get_name() == "Rocket"

def test_incre_negative():
    x = BaseObject("MCA")
    x.incre_negative()
    assert x.negative == 1

def test_incre_positive():
    x = BaseObject("MCA")
    x.incre_positive()
    assert x.positive == 1

def test_str():
    x = BaseObject("UTAR")
    assert x.__str__() == f"\nname=UTAR\nnegative=0\npositive=0\n"