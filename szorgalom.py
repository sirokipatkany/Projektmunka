jegy=int(input("Add meg az osztályzatod"))
osztályzat=jegy
if osztályzat == 1:
    szorgalom = "rossz"
elif osztályzat ==2:
    szorgalom ="hanyag"
elif osztályzat ==3:
    szorgalom = "változó"
elif osztályzat ==4:
    szorgalom = "jó"
elif osztályzat ==5:
    szorgalom = "példás"
else:
    szorgalom = "nincs ilyen "

print(f"osztalyzat: {osztályzat}, szorgalom: {szorgalom}")