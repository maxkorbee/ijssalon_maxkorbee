from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    kortingsprijs = round(prijs * (1 - korting), 2)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {kortingsprijs} euro."

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag

    btw_bedrag = round(totaal * btw, 2)
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {bedrag} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])

print(aanbieding_1("aardbei", 20, .1))