import pytest
from kalkulacka import Kalkulacka  # Replace 'your_module_name' with the actual name of your module

@pytest.fixture
def kalkulacka():
    return Kalkulacka()

def test_vypocitej(kalkulacka):
    kalkulacka._horni_radek = "2+3"
    assert kalkulacka.vypocitej() == 5

def test_tlacitko_plus(kalkulacka):
    kalkulacka.tlacitko_plus()
    assert kalkulacka._horni_radek == "+"

def test_tlacitko_minus(kalkulacka):
    kalkulacka.tlacitko_minus()
    assert kalkulacka._horni_radek == "-"

def test_tlacitko_deleno(kalkulacka):
    kalkulacka.tlacitko_cislo(2)
    kalkulacka.tlacitko_deleno()
    kalkulacka.tlacitko_cislo(2)

    assert kalkulacka.vypocitej() == 1
# Write similar test functions for other methods

if __name__ == "__main__":
    pytest.main()
