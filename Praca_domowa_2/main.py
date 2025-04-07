import datetime

rok = datetime.datetime.now().year
imie = input("Prosze podaj imie: ")
rok_urodzenia = int(input("Podaj rok urodzenia"))
wiek = rok - rok_urodzenia
wiadomosc = input("Prosze podaj spersonalizowana wiadomosc")
imie_nadawcy = input("Prosze podaj swoje imie: ")

print(f"{imie} wszystkiego najlepszego z okazji {wiek} urodzin. \n {wiadomosc} \n {imie_nadawcy}")