from firma import FirmaSpozywcza, FirmaTransportowa
from pojazd import Pojazd
from odcinek import Odcinek
from kurs import Kurs
from datetime import date

ft = FirmaTransportowa('Polska', 'Bytom', 'MariuszeX', 'Kozacka 69', '123456', 'Mariusz Xavier')
fs = FirmaSpozywcza('Niemcy', 'Berlin', 'Studentenmix', '00567 Halbauer Weg 21', '555555', 'bakaliowa')
o1 = Odcinek('Radzymin','Kłobuck', 367.6789, 'P1', False)
o2 = Odcinek('Kłobuck','Berlin', 8888, 'P2', True)
p = Pojazd('Volkswagen', 'Golf', 2009, 1000000, 'Staszek Jurewski')
k = Kurs()
k.pojazd = p
k.odcinki = [o1,o2]
k.data = date(2021,1,1)
k.firma_sp = fs
k.firma_tr = ft

print(k)
print(k.suma_odl())
print(k.dejmarke())