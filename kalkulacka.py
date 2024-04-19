class Kalkulacka():
    
    def __init__(self):
        self._horni_radek = ""
        self._vysledek_radek = ""
    
    # vrátí výsledek horniho radku
    def vypocitej(self):
        return eval(self._horni_radek)
    
    def tlacitko_plus(self):
        self._horni_radek = self._horni_radek + "+"
    
    def tlacitko_minus(self):
        self._horni_radek = self._horni_radek + "-"
    
    def tlacitko_deleno(self):
        self._horni_radek = self._horni_radek + "/"
    
    def tlacitko_krat(self):
        self._horni_radek = self._horni_radek + "*"
    
    def tlacitko_rovna_se(self):
        self._vysledek_radek = self.vypocitej()
    
    def tlacitko_cislo(self, cislo):
        self._horni_radek = self._horni_radek + str(cislo)