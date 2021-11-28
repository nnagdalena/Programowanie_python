#Odcinek (punktA, punktB, odleglosc, priorytet, miedzynarodowy)

class Odcinek:
    def __init__(self, punktA: str, punktB: str, odleglosc: float, priorytet: str, miedzynarodowy: bool) -> None:
        self._punktA = punktA
        self._punktB = punktB
        self._odleglosc = odleglosc
        self._priorytet = priorytet
        self._miedzynarodowy = miedzynarodowy

    def __str__(self) -> str:
        return f'Punkt A: {self.punktA}, Punkt B:  {self.punktB}, odległość: {self.odleglosc}; \nPriorytet: {self.priorytet}; Kurs międzynarodowy: {self.miedzynarodowy} '

    @property
    def punktA(self) -> None:
        return self._punktA

    @punktA.setter
    def punktA(self, value: str) -> None:
        self._punktA= value

    @property
    def punktB(self) -> None:
        return self._punktB

    @punktB.setter
    def punktB(self, value: str) -> None:
        self._punktB = value

    @property
    def odleglosc(self) -> None:
        return self._odleglosc

    @odleglosc.setter
    def odleglosc(self, value: float) -> None:
        self._odleglosc = value

    @property
    def priorytet(self) -> None:
        return self._priorytet

    @priorytet.setter
    def priorytet(self, value: str) -> None:
        self._priorytet = value

    @property
    def miedzynarodowy(self) -> None:
        return self._miedzynarodowy

    @miedzynarodowy.setter
    def miedzynarodowy(self, value: str) -> None:
        self._miedzynarodowy = value