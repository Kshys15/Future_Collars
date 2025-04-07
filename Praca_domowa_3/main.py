liczba_paczek = 0
liczba_kilogramow = 0
suma_pustych = 0
max_puste = 0
max_paczka_index = 0
current_weight = 0
current_paczka_index = 1

liczba_elementow = int(input("Ile paczek chcesz wysłać? "))

for i in range(liczba_elementow):
    waga = int(input(f"Podaj wagę elementu {i+1}: "))

    if waga < 1 or waga > 10:
        break

    if current_weight + waga > 20:
        liczba_paczek += 1
        suma_pustych += 20 - current_weight
    if 20 - current_weight > max_puste:
        max_puste = 20 - current_weight
        max_paczka_index = current_paczka_index

        current_weight = 0
        current_paczka_index += 1

        current_weight += waga
        liczba_kilogramow += waga

    if current_weight > 0:
        liczba_paczek += 1
        suma_pustych += 20 - current_weight
    if 20 - current_weight > max_puste:
        max_puste = 20 - current_weight
        max_paczka_index = current_paczka_index

print("\nPodsumowanie:")
print(f"Wysłano {liczba_paczek} paczek")
print(f"Wysłano {liczba_kilogramow} kg")
print(f"Suma pustych kilogramów: {suma_pustych} kg")
print(f"Najwięcej pustych kilogramów ma paczka {max_paczka_index} ({max_puste} kg)")