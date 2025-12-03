def megold():
    elso_sor = input().split()
    tanulok = int(elso_sor[0])
    versenyek = int(elso_sor[1])


    min_pontok = []
    if len(elso_sor) > 2:
        min_pontok = list(map(int, elso_sor[2:2 + versenyek]))

    while len(min_pontok) < versenyek:
        min_pontok += list(map(int, input().split()))

    gyoztesek = set()

    for i in range(versenyek):
        sor = input().split()
        indulok = int(sor[0])
        adatok = sor[1:]

        
        while len(adatok) < 2 * indulok:
            adatok += input().split()

        
        pontok = []
        index = 0
        for j in range(indulok):
            tanulo = int(adatok[index])
            pont = int(adatok[index + 1])
            index += 2
            pontok.append((tanulo, pont))

        
        minimalis = min_pontok[i]
        jogosultak = [(t, p) for (t, p) in pontok if p >= minimalis]

        
        if not jogosultak:
            continue

        
        max_pont = -1
        for _, p in jogosultak:
            if p > max_pont:
                max_pont = p

        
        for t, p in jogosultak:
            if p == max_pont:
                gyoztesek.add(t)

    gyoztes_lista = sorted(gyoztesek)
    print(len(gyoztes_lista), *gyoztes_lista)
megold()