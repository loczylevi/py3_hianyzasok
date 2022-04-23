#N�v;Oszt�ly;Els� nap;Utols� nap;Mulasztott �r�k
#Balogh P�ter;6a;1;1;5

class Hianyzasok:
  def __init__(self,sor):
    nev,osztaly,elso_nap,utolso_nap,mulasztott = sor.strip().split(";")
    self.nev = nev
    self.osztaly = osztaly
    self.elso_nap = int(elso_nap)
    self.utolso_nap = int(utolso_nap)
    self.mulasztott = int(mulasztott)

with open("szeptember.csv","r",encoding="latin2") as f:
  fejlec = f.readline()
  lista = [Hianyzasok(sor) for sor in f]

#2

mulasztott_orak = sum([sor.mulasztott for sor in lista])

print(f"""2.feladat
     Összes mulasztott órák száma: {mulasztott_orak} óra.""")

okes_nap = False
#3
nap = int(input("""3.feladat:
     Kérem adjon meg egy napot: """))
if 1 <= nap <= 30:
  okes_nap = True
else:
  okes_nap = False

tanulo_nev = input("     Tanuló neve: ")