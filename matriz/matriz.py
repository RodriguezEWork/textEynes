import random

matriz = [[random.randint(1,2) for i in range (5)] for j in range(5)]

for b in range(5):
    for c in range(5):
        print(matriz[b][c], end = ' ')
    print()

for f in range(5):
    for d in range(2):
        if(matriz[f][d] == matriz[f][d+1] and matriz[f][d] == matriz[f][d+2] and matriz[f][d] == matriz[f][d+3]):
            print ("Se repite en una linea horizontal empezando desde " , f, d , "hasta " , f, d+3)
        if(matriz[d][f] == matriz[d+1][f] and matriz[d][f] == matriz[d+2][f] and matriz[d][f] == matriz[d+3][f]):
            print ("Se repite en una linea vertical empezando desde " , f , d , "hasta " , f , d+3)


    