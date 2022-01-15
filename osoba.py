class Osoba:
    def __init__(self, imie: str, nazwisko: str, wiek: int) -> None:
        self._imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek

    def __str__(self):
        return f'Imię: {self.imie} \nNazwisko: {self.nazwisko} \nWiek:  {self.wiek} \n'

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def wiek(self) -> int:
        return self._wiek


class Dietetyk(Osoba):
    def __init__(self, imie: str, nazwisko: str, wiek: int, poziom: str) -> None:
        super().__init__(imie, nazwisko, wiek)
        self._poziom = poziom

    def __str__(self) -> str:
        return f'{super().__str__()}Poziom: {self.poziom}'

    @property
    def poziom(self) -> str:
        return self._poziom


class Pacjent(Osoba):
    def __init__(self, imie: str, nazwisko: str, wiek: int, bmi: int) -> None:
        super().__init__(imie, nazwisko, wiek)
        self._bmi = bmi

    def __str__(self) -> str:
        return f'{super().__str__()}BMI: {self.bmi}'

    @property
    def bmi(self) -> int:
        return self._bmi
