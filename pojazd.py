#Pojazd (marka, model, rocznik, przebieg, kierowca)

class Pojazd:
    def __init__(self, marka: str, model: str, rocznik: int, przebieg: float, kierowca: str) -> None:
        self._marka = marka
        self._model = model
        self._rocznik = rocznik
        self._przebieg = przebieg
        self._kierowca = kierowca

    def __str__(self) -> str:
        return f'Pojazd {self.marka}  {self.model} rocznik {self.rocznik}; \nPrzebieg (w km): {self.przebieg}; \nKierowca: {self.kierowca} '

    @property
    def marka(self) -> None:
        return self._marka

    @marka.setter
    def marka(self, value: str) -> None:
        self._marka = value

    @property
    def model(self) -> None:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        self._model = value

    @property
    def rocznik(self) -> None:
        return self._rocznik

    @rocznik.setter
    def rocznik(self, value: int) -> None:
        self._rocznik= value

    @property
    def przebieg(self) -> None:
        return self._przebieg

    @przebieg.setter
    def przebieg(self, value: float) -> None:
        self._przebieg = value

    @property
    def kierowca(self) -> None:
        return self._kierowca

    @kierowca.setter
    def kierowca(self, value: str) -> None:
        self._kierowca = value