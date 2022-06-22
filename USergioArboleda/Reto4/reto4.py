
def repetidos(lista):
    rep = []
    defe = 0

    for z in lista:
        if z not in rep:
            rep.append(z)
        else:
            defe += 1

    return defe

numBaldosas, memoriaSensor = input().split()
numBaldosas = int(numBaldosas)
memoriaSensor = int(memoriaSensor)

baldosas = input().split()
defectuosasCarrete = 0
defectuosasTotal = 0

carrete = [0]*(memoriaSensor + 1)

defectuosasTotal = repetidos(baldosas)

if (memoriaSensor+1) < numBaldosas:
    for i in range(len(baldosas)):
        if i >= memoriaSensor:
            j = i
            k = 0

            for k in range(memoriaSensor, -1, -1):
                carrete[k] = baldosas[j]
                j -= 1
        
            defectuosasCarrete += repetidos(carrete)

if defectuosasCarrete > defectuosasTotal:
    defectuosasCarrete = defectuosasTotal

print(defectuosasTotal, defectuosasCarrete, numBaldosas)