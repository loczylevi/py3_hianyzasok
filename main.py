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

kereso = [sor for sor in lista if tanulo_nev == sor.nev and 0 < sor.mulasztott]

if len(kereso) > 0:
  print("""4.feladat
     A tanuló hiányzott szeptemberben""")
else:
  print("""4.feladat
     A tanuló nem hiányzott szeptemberben""") 


#5
hianyzott_e = [sor for sor in lista if okes_nap == True and sor.elso_nap <= nap <= sor.utolso_nap]

if okes_nap == True:
  print(f"5.feladat: Hiányzók 2017.09.{nap}.-n:")
else:
  print(f"5.feladat: Hiányzók 2017.09. [] --> nem 1 és 30 között volt a bekért szám")

if len(hianyzott_e) > 0:
  [print(f"     {sor.nev} ({sor.osztaly})") for sor in hianyzott_e]
else:
  print("     Nem volt hiányzó!")