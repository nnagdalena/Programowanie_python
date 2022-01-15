class Dieta:
    def __init__(self, nazwa: str, kcal: int, wersja: str, cena: float) -> None:
        self._nazwa = nazwa
        self._kcal = kcal
        self._wersja = wersja
        self._cena = cena

    def __str__(self) -> str:
        return f'Nazwa: {self.nazwa} \nWersja: {self.wersja} \nKaloryczność: {self.kcal} kcal \nCena: {self.cena}'

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def kcal(self) -> int:
        return self._kcal

    @property
    def cena(self) -> float:
        return self._cena

    @property
    def wersja(self) -> str:
        return self._wersja
