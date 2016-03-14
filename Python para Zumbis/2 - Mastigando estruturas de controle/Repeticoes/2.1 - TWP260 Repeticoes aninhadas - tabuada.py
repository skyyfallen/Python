#Imprima as tabuadas de 1 a 10

tabuada = 1
while tabuada <= 10:    
    print ('Tabuada de %d' %tabuada)
    n = 1
    while n <= 10:
        print ('%d x %d = %d' %(tabuada, n, tabuada * n))
        n = n + 1
    tabuada = tabuada + 1
