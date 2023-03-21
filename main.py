#zadanie1

#zadanie2
a = int(input("Podaj pierwszą liczbe: "))
b = int(input("Podaj drugą liczbe: "))
znak = input("Podaj znak: ")

if znak == "+":
    rownanie = a+b
elif znak == "-"  :
    rownanie = a-b
elif znak == "*":
    rownanie = a*b
elif znak == "/":
    rownanie = a/b
else:
    print("Podano zly znak")
    rownanie = "---"

print(a,znak,b,"=",rownanie)

#zadanie3