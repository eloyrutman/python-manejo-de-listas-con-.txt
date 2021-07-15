n1 = n2 = n3 = 0
prom = 0.0
nota = " "
genero = estatus = " "
archivo = open("notas.txt")
registro = " "
genero2 = genero3 = 0
divi = divi2 = 0
gen1 = gen2 = 0
band = 0
mnom = " "
mnom1 = " "
nprom = band = 0

print("Nombre       Nota     Estatus")
for registro in archivo:
    campos = registro.split(",")
    nom = campos[0]
    genero = campos[1]
    n1 = int(campos[2])
    n2 = int(campos[3])
    n3 = int(campos[4])
    prom = (n1 + n2 + n3)/3
    mprom = prom
    if prom >= 9.5:
        estatus = "aprobado"
    else:
        estatus = "reprobado"
    print ("{0:10}   {1:3.2f}   {2:3}".format(nom,prom,estatus))
    if genero == "M":
        genero2 +=1
    if genero == "M" and prom >=9.5:
        gen1 += 1
    if genero == "F":
        genero3 += 1
    if genero == "F" and prom >=9.5:
        gen2 += 1
    if (band == 0):
        nprom = prom
        mnom = nom
        band = 1
    elif nprom < prom:
        nprom = prom
        mnom = nom
        mnom1 = " "
    elif nprom == prom:
        mnom1 = nom


        
divi = (gen1/genero2)*100
divi2 =(gen2/genero3)*100
print("Alumno con mas nota: ",mnom)
print("Porcentaje de hombres que aprobaron: ",divi)
print("Porcentaje de mujeres que aprobaron: ",divi2)

        


    
