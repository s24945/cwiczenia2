print("-Pytanie: Jak masz na imię i nazwisko?")
name = input("Odpowiedź: ")

print("-Pytanie: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: ")
print("1) oglądanie telewizji/filmów/seriali")
print("2) słuchanie muzyki")
print("3) czytanie książek")
print("4) uprawianie sportu")
print("5) inne, jakie?")
odp1 = int(input("Wybierz odpowiednią cyfrę (1-5): "))
if odp1 == 5:
    odp11 = input("Jakie: ")

if odp1 == 1:
    o1 = "oglądanie telewizji/filmów/seriali"
elif odp1 == 2:
    o1 = "słuchanie muzyki"
elif odp1 == 3:
    o1 = "czytanie książek"
elif odp1 == 4:
    o1 = "uprawianie sportu"
else:
    o1 = odp11

print("-Pytanie: W jakich okolicznościach czytasz książki najczęściej?")
print("1) podczas podróży")
print("2) w wolnym czasie")
print("3) w ogóle nie czytam")
print("4) inne, jakie?")
odp2 = int(input("Wybierz odpowiednią cyfrę (1-4): "))
if odp2 == 4:
    odp22 = input("Jakie: ")

if odp2 == 1:
    o2 = "podczas podróży"
elif odp2 == 2:
    o2 = "w wolnym czasie"
elif odp2 == 3:
    o2 = "w ogóle nie czytam"
else:
    o2 = odp22

print("-Pytanie: Po książki w jakiej formie sięgasz najczęściej?")
print("1) papierowej")
print("2) e-booki na komputerze")
print("3) e-booki na tablecie/telefonie")
print("4) e-booki na specjalnym czytniku")
odp3 = int(input("Wybierz odpowiednią cyfrę (1-4): "))

if odp3 == 1:
    o3 = "papierowej"
elif odp3 == 2:
    o3 = "e-booki na komputerze"
elif odp3 == 3:
    o3 = "e-booki na tablecie/telefonie"
else:
    o3 = "e-booki na specjalnym czytniku"

print("-Pytanie: W jakim języku książki czytasz? ")
print("1) polskim")
print("2) angielskim")
print("3) niemieckim")
print("4) rosyjskim")
print("5) hiszpanskim")
print("6) francuskim")
print("7) innym, jakim?")
odp4 = int(input("Wybierz odpowiednią cyfrę (1-7): "))
if odp4 == 7:
    odp44 = input("Jakim: ")

if odp4 == 1:
    o4 = "polskim"
elif odp4 == 2:
    o4 = "angielskim"
elif odp4 == 3:
    o4 = "niemieckim"
elif odp4 == 4:
    o4 = "rosyjskim"
elif odp4 == 5:
    o4 = "hiszpanskim"
elif odp4 == 6:
    o4 = "francuskim"
else:
    o4 = odp44

print("-Pytanie: Jak często wypożyczasz książki w bibliotece?")
print("1) nigdy")
print("2) raz w roku")
print("3) raz na pół roku")
print("4) raz na miesiąc")
print("5) czesciej")
odp5 = int(input("Wybierz odpowiednią cyfrę (1-5): "))

if odp5 == 1:
    o5 = "nigdy"
elif odp5 == 2:
    o5 = "raz w roku"
elif odp5 == 3:
    o5 = "raz na pół roku"
elif odp5 == 4:
    o5 = "raz na miesiąc"
else:
    o5 = "czesciej"
print("////////////// Twoje odpowiedzi ////////////////")

print("-Pytanie: Jak masz na imię i nazwisko?")
print("Odpowiedź:", name)
print("-Pytanie: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
print("Odpowiedź:", o1)
print("-Pytanie: W jakich okolicznościach czytasz książki najczęściej?")
print("Odpowiedź:", o2)
print("-Pytanie: Po książki w jakiej formie sięgasz najczęściej?")
print("Odpowiedź:", o3)
print("-Pytanie: W jakim języku książki czytasz?")
print("Odpowiedź:", o4)
print("-Pytanie: Jak często wypożyczasz książki w bibliotece?")
print("Odpowiedź:", o5)
