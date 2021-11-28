#Kurs (pojazd, odcinki, kierowca_nowy, data, czy_przyspieszony)
from pojazd import Pojazd
from odcinek import Odcinek
from datetime import date
from firma import FirmaSpozywcza, FirmaTransportowa

class Kurs:
    def __init__(self) -> None:
        self._pojazd = None
        self._odcinki= None
        self._data = None
        self._firma_sp = None
        self._firma_tr = None


    def __str__(self) -> str:
        for x in range(len(self._odcinki)):
            print(f'Odcinek {x+1}')
            print(self._odcinki[x])
            print('\n')
        return f'Pojazd: {self.pojazd}; \nData: {self.data};\n \nFirma spożywcza: {self.firma_sp};\n \nFirma transportowa: {self.firma_tr} \n'

    @property
    def pojazd(self) -> None:
        return self._pojazd

    @pojazd.setter
    def pojazd(self, value: Pojazd) -> None:
        self._pojazd= value

    @property
    def odcinki(self) -> None:
        return self._odcinki

    @odcinki.setter
    def odcinki(self, value: list[Odcinek]) -> None:
        self._odcinki = value

    @property
    def data(self) -> None:
        return self._data

    @data.setter
    def data(self, value: date) -> None:
        self._data= value

    @property
    def firma_sp(self) -> None:
        return self._firma_sp

    @firma_sp.setter
    def firma_sp(self, value: FirmaSpozywcza) -> None:
        self._firma_sp = value

    @property
    def firma_tr(self) -> None:
        return self._firma_tr

    @firma_tr.setter
    def firma_tr(self, value: FirmaTransportowa) -> None:
        self._firma_tr = value


    def suma_odl(self) -> float:
        wynik = 0
        for x in range(len(self._odcinki)):
            wynik = wynik+self._odcinki[x]._odleglosc
        return round(wynik,2)


    def dejmarke(self) -> str:
        return self._pojazd._marka