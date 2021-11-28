#Firma (kraj, miasto, nazwa, adres, nrtel)

class Firma:
    def __init__(self, kraj: str, miasto: str, nazwa: str, adres: str, nr_tel: str) -> None:
        self._kraj = kraj
        self._miasto = miasto
        self._nazwa = nazwa
        self._adres = adres
        self._nr_tel = nr_tel

    def __str__(self) -> str:
        return f'Firma {self.nazwa}; \nKraj {self.kraj}; \nMiasto: {self.miasto}; \nAdres: {self.adres}; \nNrtel: {self.nr_tel} '

    @property
    def kraj(self) -> None:
        return self._kraj

    @kraj.setter
    def kraj(self, value: str) -> None:
        self._kraj = value

    @property
    def miasto(self) -> None:
        return self._miasto

    @miasto.setter
    def miasto(self, value: str) -> None:
        self._miasto = value

    @property
    def nazwa(self) -> None:
        return self._nazwa

    @nazwa.setter
    def nazwa(self, value: str) -> None:
        self._nazwa = value

    @property
    def adres(self) -> None:
        return self._adres

    @adres.setter
    def adres(self, value: str) -> None:
        self._adres = value

    @property
    def nr_tel(self) -> None:
        return self._nr_tel

    @nr_tel.setter
    def nr_tel(self, value: str) -> None:
        self._nr_tel = value



class FirmaTransportowa(Firma):
    def __init__(self, kraj: str, miasto: str, nazwa: str, adres: str, nr_tel: str, wlasciciel: str) -> None:
        super().__init__(kraj, miasto, nazwa, adres, nr_tel)
        self._wlasciciel = wlasciciel

    def __str__(self) -> None:
        return f'{super().__str__()}; \nWłaściciel: {self.wlasciciel}'

    @property
    def wlasciciel(self) -> None:
        return self._wlasciciel

    @wlasciciel.setter
    def wlasciciel(self, value: str) -> None:
        self._wlasciciel = value



class FirmaSpozywcza(Firma):
    def __init__(self, kraj: str, miasto: str, nazwa: str, adres: str, nr_tel: str, branza: str) -> None:
        super().__init__(kraj, miasto, nazwa, adres, nr_tel)
        self._branza = branza

    def __str__(self) -> None:
        return f'{super().__str__()}; \nBranża: {self.branza}'

    @property
    def branza(self) -> None:
        return self._branza

    @branza.setter
    def branza(self, value: str) -> None:
        self._branza = value

























