from TCLCPhase1.AnalysisLib.Party import Party


def test_constructor():
    x = Party("Barisan National")
    assert x.name == "Barisan National"
    assert x.negative == 0
    assert x.positive == 0

def test_get_name():
    x = Party("Rocket")
    assert x.get_name() == "Rocket"

def test_incre_negative():
    x = Party("MCA")
    x.incre_negative()
    assert x.negative == 1

def test_incre_positive():
    x = Party("MCA")
    x.incre_positive()
    assert x.positive == 1

def test_str():
    x = Party("UTAR")
    assert x.__str__() == f"\nname=UTAR\nnegative=0\npositive=0\n"