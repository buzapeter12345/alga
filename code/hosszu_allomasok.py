elso_sor = input().split()
N = int(elso_sor[0])
K = int(elso_sor[1])

hosszu_szakasz_szamlalo = 0

for i in range(N):
    adatok = input().split()
    tavolsag = int(adatok[0])

    if tavolsag > K:
        hosszu_szakasz_szamlalo += 1

print(hosszu_szakasz_szamlalo)