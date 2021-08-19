crivo = []

crivo.append(True)
crivo.append(False)

for i in range(0, 2, 1):
    if (crivo[i] == True):
        print("Crivo %d é True = %s" %(i, crivo[i]))
    else:
        print("Crivo %d é False = %s" %(i, crivo[i]))
print(crivo)
