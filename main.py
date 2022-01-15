from osoba import Dietetyk, Pacjent
from dieta import Dieta
from zamowienie import Zamowienie

d = Dietetyk('Magda', 'Bogacz', 22, 'mid')
p = Pacjent('Mirek', 'Mirowski', 33, 120)
dd1 = Dieta('DASH', 1500, 'wege', 2234.666)
dd2 = Dieta('DASH', 1200, 'vegan', 1800)
dd3 = Dieta('Intermittent fasting', 1500, 'standard', 1600.88)

z = Zamowienie()
z.dieta = [dd1, dd2, dd3]
z.pacjent = p
z.dietetyk = d
z.id = 123

print(z)
print(z.ladnacena)
print(z.ladnekcal)
