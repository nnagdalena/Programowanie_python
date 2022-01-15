from osoba import Dietetyk, Pacjent
from dieta import Dieta


class Zamowienie:
    def __init__(self) -> None:
        self._dieta = None
        self._dietetyk = None
        self._pacjent = None
        self._id = None

    def __str__(self) -> str:
        for x in self.dieta:
            print(x)
            print('\n')
        return f'Dietetyk: {self.dietetyk}\n \nPacjent: {self.pacjent}\n \nId zamowienia:  {self.id}\n'

    @property
    def dieta(self) -> list:
        return self._dieta

    @dieta.setter
    def dieta(self, value: list[Dieta]) -> None:
        self._dieta = value

    @property
    def dietetyk(self) -> Dietetyk:
        return self._dietetyk

    @dietetyk.setter
    def dietetyk(self, value: Dietetyk) -> None:
        self._dietetyk = value

    @property
    def pacjent(self) -> Pacjent:
        return self._pacjent

    @pacjent.setter
    def pacjent(self, value: Pacjent) -> None:
        self._pacjent = value

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def suma_kcal(self) -> int:
        wynik = 0
        for d in self.dieta:
            wynik = wynik + d.kcal
        return wynik

    @property
    def suma_cena(self) -> float:
        wynik = 0
        for d in self.dieta:
            wynik = wynik + d.cena
        return round(wynik, 2)

    @property
    def ladnacena(self) -> str:
        return f"Całkowita wartość zamówienia: {self.suma_cena} zł."

    @property
    def ladnekcal(self) -> str:
        return f"Wartość energetyczna zamówienia: {self.suma_kcal} kcal/dzień."
