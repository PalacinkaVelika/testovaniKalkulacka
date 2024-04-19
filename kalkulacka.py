class Kalkulacka():
    
    def __init__(self):
        self._horni_radek = ""
        self._vysledek_radek = ""
    
    # vrátí výsledek horniho radku
    def vypocitej(self):
        return eval(self._horni_radek)