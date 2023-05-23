import numpy as np
import matplotlib as mt


def eliminacao_gauss(matriz):
    n = len(matriz) #define linhas e colunas contudo que ela seja quadrada
    
    for i in range(n): # esse for vai percorrer as linhas da matriz 
        pivo = matriz[i][i] # esse elemento vai obter o pivo (diagonal da matriz)
        
        if pivo == 0: #tratamento do erro se o pivo for == 0 
            raise ValueError("Ops, verifique o valor do pivô indicado")
        
        matriz[i] = matriz[i] / pivo #verifica a linha do array em sequancia dividindo pelo pivo
        
        print("Matriz intermediária após a normalização da linha", i + 1)
        print(matriz)
        print()
        
        for j in range(i+1, n): #percorre a linha abaixo do pivo
            multiplicador = matriz[j][i] #definição do multiplicador (abaixo do pivo)
            matriz[j] = matriz[j] - multiplicador * matriz[i] # 
        
        print("Matriz intermediária após a atualização das linhas abaixo do pivô", i + 1)
        print(matriz)
        print()
    
    return matriz

matriz = np.array([[7, 3, 1, 4],
                   [1, 4, 2, 1],
                   [3, 2, -3, -2],
                   [5, 2, 5, 10]])  #matriz para teste

resultado = eliminacao_gauss(matriz)
print("Matriz resultante:")
print(resultado)

#n = matriz 
#i = numero
#j = alterar numero