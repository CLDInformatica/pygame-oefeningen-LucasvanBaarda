'''
Het programma vraagt om een toetscijfer (float voor kommagetallen!), zorg dat je programma checkt dat het een geldig toetscijfer is! 
(dus bijv. geen 11 of een -1)

Als het een geldig cijfer is print dan `dankjewel`. Als het een ongeldig cijfer, print dan `Dat is geen geldig cijfer...`

Als het cijfer boven de 8 is, print dan `Wow, dat is heel hoog`.
Als het cijfer onder de 8 maar boven de 5.5 is, print dan `Prima, een voldoende!`.
Als het cijfer onder de 5.5 maar boven de 3 is, print dan `Kon slechter maar mag wel beter de volgende keer...`.
Als het cijfer onder de 3 is, print dan `Wat ging hier mis?`.

Als je niet meer weet hoe alles werkt, zoek het dan even op!
'''

toetscijfer = float(input("Geef een cijfer:"))
if toetscijfer > 1 and toetscijfer <10:
        print("dankjewel")
else:
    print("Dat is geen geldig toetscijfer. Probeer het opnieuw. ")


if toetscijfer > 8:
    print("Wow! Dat is echt heel hoog")


if toetscijfer > 5.5 and toetscijfer <8:
     print("[Prima, een voldoende!]")


if toetscijfer > 3 and toetscijfer < 5.5:
     print ("Oei, een onvoldoende. Nog werk aan de winkel")


if toetscijfer < 3:
     print("volgend jaar praktijkonderwijs.")