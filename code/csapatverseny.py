def megold():
    
    sor = input().split()
    csapatok_szama = int(sor[0])
    meccsek_szama = int(sor[1])

    gyozelmek = [[] for _ in range(csapatok_szama + 1)]
    veresegek = [[] for _ in range(csapatok_szama + 1)] 
    
    jatekosok = set()
    
    for p in range(meccsek_szama):
        meccs_eredmeny = input().split()
        
        if not meccs_eredmeny:
             break
             
        nyertes = int(meccs_eredmeny[0])
        vesztes = int(meccs_eredmeny[1])
        
        gyozelmek[nyertes].append(vesztes)
        veresegek[vesztes].append(nyertes)
        
        jatekosok.add(nyertes)
        jatekosok.add(vesztes)
        
    csapat_a_talalt = -1
    csapat_b_talalt = -1
    
    for i in range(1, csapatok_szama + 1):
        for j in gyozelmek[i]:
            if i in gyozelmek[j]:
                if i < j:
                    csapat_a_talalt = i
                    csapat_b_talalt = j
                    break 
        if csapat_a_talalt != -1:
            break

        
    legyozhetetlenek = []
    
    for i in sorted(list(jatekosok)):
        if not veresegek[i]:
            legyozhetetlenek.append(str(i))
            
        
    ciklus_tag = -1
    allapot = [0] * (csapatok_szama + 1) 

    def keres_ciklust(u):
        nonlocal ciklus_tag
        if ciklus_tag != -1:
            return 
            
        allapot[u] = 1 
        
        for v in gyozelmek[u]:
            if allapot[v] == 1:
                ciklus_tag = min(u, v)
                return
            
            if allapot[v] == 0:
                keres_ciklust(v)
            
            if ciklus_tag != -1:
                return
        
        allapot[u] = 2 
        
    for i in range(1, csapatok_szama + 1):
        if allapot[i] == 0:
            keres_ciklust(i)
        if ciklus_tag != -1:
            break
            
    if csapat_a_talalt != -1:
        print(f"{csapat_a_talalt} {csapat_b_talalt}")
    else:
        print() 
    
    print(" ".join(legyozhetetlenek))
    
    if ciklus_tag != -1:
        print(ciklus_tag)
    else:
        print()

megold()