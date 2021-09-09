geel = input('Is de kaas geel? [Y/N]: ').lower()
if geel == "y":
    gaten = input('Zitten er gaten in? [Y/N]: ').lower()
    if gaten == "y":
        prijs = input('Is de kaas belachelijk duur? [Y/N]: ').lower()
        if prijs == "y":
            print('Emmenthaler')
        else:
            print('Leerdammer')
    else:
        steen = input('Is de kaas hard als steen? [Y/N]: ').lower()
        if steen == "y":
            print('Panmigiano Reggiano')
        else:
            print('Goudse kaas')
else:
    schimmel = input('Heeft de kaas blauwe schimmels? [Y/N]: ').lower()
    if schimmel == "y":
        korst1 = input('heeft de kaas een korst? [Y/N]: ').lower()
        if korst1 == "y":
            print('Bleu de Rochbaron')
        else:
            print("Foume d'Ambert")
    else:
        korst2 = input('heeft de kaas een korst? [Y/N]: ').lower()
        if korst2 == "y":
            print("Camembert")
        else:
            print("Mozzarella")    