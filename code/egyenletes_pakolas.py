def megold():
    
    sor = input().split()
    N = int(sor[0])
    K = int(sor[1])

    s_szoveg = input().split()
    S = []
    for s_ertek in s_szoveg:
        suly = int(s_ertek) 
        S.append(suly)

    elotag_osszeg = [0] * (N + 1)
    jelenlegi_osszeg = 0
    for i in range(N):
        jelenlegi_osszeg += S[i]
        elotag_osszeg[i+1] = jelenlegi_osszeg

    also_hatar = max(S) 
    felso_hatar = elotag_osszeg[N] 
    legjobb_max_terheles = felso_hatar
    
    def ellenoriz(max_terheles):
        
        szukseges_kamionok = 1
        jelenlegi_terheles = 0
        
        for suly in S:
            if jelenlegi_terheles + suly <= max_terheles:
                jelenlegi_terheles += suly
            else:
                szukseges_kamionok += 1
                jelenlegi_terheles = suly
        
        return szukseges_kamionok

    while also_hatar <= felso_hatar:
        kozep = (also_hatar + felso_hatar) // 2
        
        kamion_szam = ellenoriz(kozep)
        
        if kamion_szam <= K:
            legjobb_max_terheles = kozep
            felso_hatar = kozep - 1
        else:
            also_hatar = kozep + 1

    
    kezdo_kontener_sorszamok = []
    jelenlegi_kontener_index = 0 
    
    for p in range(K):
        kezdo_kontener_sorszamok.append(jelenlegi_kontener_index + 1)
        
        if p == K - 1:
            break
            
        legjobb_kovetkezo_index = -1
        
        for i in range(jelenlegi_kontener_index, N):
            
            kovetkezo_terheles = elotag_osszeg[i + 1] - elotag_osszeg[jelenlegi_kontener_index]
            
            if kovetkezo_terheles <= legjobb_max_terheles:
                legjobb_kovetkezo_index = i + 1 
            else:
                break
        
        if legjobb_kovetkezo_index == -1:
             legjobb_kovetkezo_index = N

        jelenlegi_kontener_index = legjobb_kovetkezo_index


    print(legjobb_max_terheles)
    print(" ".join(map(str, kezdo_kontener_sorszamok)))

if __name__ == "__main__":
    megold()