class NoSmallerFive(BaseException):
    def __init__(self,number):
        self.number=number
    def __str__(self):
        return str(self.number) + " ist nicht kleiner als Fünf!"
class Nozero(BaseException):
    def __init__(self, number):
        self.number=number
    def __str__(self):
        return "Nicht Zero eingeben!"

class SpassMitFünf:

    def __init__(self, number):
        if not(number<5):
            raise NoSmallerFive(number)
        if (number==0):
            raise Nozero(number)
        self.number=number

    def dasTeilVonEins(self):
        return 1/self.number



#Komplett Sinnbefreites Programm
#Wir habe eine Klasse Spass mit fünf, die einfach nur eine Zahl annimmt, und prüft, ob sie fünf ist. Ist sie es nicht, wird eine innere Ausnahmebehandlung ausgelöst und die Eingabe neu gestartet.
#Nach erfolgreicher Eingabe wird die Methode dasTeilVonEins aufgerufen
#BaseExeption fängt ab, was nicht durch die innere Prüfung abgefangen wird.
#Aufgabe: Gib 0 ein und schau was passiert.
#Erstelle eine neue Ausnahmeklasse und fange den Fehler, wenn man Null eingibt, so ab, dass die Eingabe automatisch erneut startet

try:
    while True:
        try:
            x=int(input("Zahl!:"))
            a=SpassMitFünf(x)
            print("Teil von Eins",a.dasTeilVonEins())
            break
        except (NoSmallerFive,Nozero) as e:
            print(e)
except BaseException as e:
    print("Oh fuck! Schwerer Fehler!!")
