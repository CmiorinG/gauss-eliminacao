import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.sidebar.title("Seleção de Sistema Linear")

genre = st.sidebar.radio(
    "Qual sistema linear você deseja calcular?",
    ('Gauss', 'Gauss - Seidel'))

num_rows = st.sidebar.number_input("Número de linhas e colunas da matriz", min_value=2, value=4)
rows = int(num_rows)
cols = rows

if genre == 'Gauss':
    st.write('Você selecionou Gauss.')
else:
    st.write("Você selecionou Gauss - Seidel")

st.write(f"Número de linhas e colunas selecionadas: {rows}")

data = [[st.sidebar.number_input(f"Valor [{i+1},{j+1}]", key=f"value_{i}_{j}", value=0) for j in range(cols)] for i in range(rows)]
st.write("Adicione os números que deseja calcular:")
df = pd.DataFrame(data, index=range(1, rows + 1), columns=range(1, cols + 1))
edited_df = st.experimental_data_editor(df)

data = edited_df.values

# Construindo a matriz
matriz = np.array(data)

# Exibindo a matriz
st.write("Matriz que será calculada:")
mt = pd.DataFrame(matriz, index=range(1, rows + 1), columns=range(1, cols + 1))
st.write(mt)

if st.sidebar.button("Calcular"):
    
    def eliminacao_gauss(matriz):
        n = len(matriz)
        
        for i in range(n):
            pivo = matriz[i][i]
            
            if pivo == 0:
                raise ValueError("A diagonal não pode ser 0")
            
            matriz[i] = matriz[i] / pivo
            
            st.write(f"Matriz intermediária após a normalização da linha {i + 1}:")
            st.write(matriz)
            
            for j in range(i+1, n):
                multiplicador = matriz[j][i]
                matriz[j] = matriz[j] - multiplicador * matriz[i]
            
            st.write(f"Matriz intermediária após a atualização das linhas abaixo do pivô {i + 1}:")
            st.write(matriz)
        
        return matriz     

    resultado = eliminacao_gauss(matriz)


def gaussSeidel(A, b, vetorSolucao, iteracoes):
    iteracao = 0
    while iteracao < iteracoes:
        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if i != j:
                    x -= A[i][j] * vetorSolucao[j]
            x /= A[i][i]
            vetorSolucao[i] = x
        iteracao += 1

    st.write(vetorSolucao)

if genre == 'Gauss - Seidel':
    st.write("Matriz que será calculada no seidel:")
    mt = pd.DataFrame(matriz, index=range(1, rows + 1), columns=range(1, cols + 1))
    st.write(mt)

    b = np.zeros(len(matriz))
    for i in range(len(matriz)):
        b[i] = matriz[i][-1]

    vetorSolucao = np.zeros(len(matriz))
    iteracoes = st.sidebar.number_input("Número de iterações para Gauss-Seidel", min_value=1, value=10)

    gaussSeidel(matriz, b, vetorSolucao, iteracoes)
    