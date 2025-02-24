import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Função para ajustar um polinômio de grau 3
def ajustar_polinomio(x, y):
    coeficientes = np.polyfit(x, y, 3)  # Ajuste de um polinômio de grau 3
    return coeficientes

def gerar_polinomio(coefs, x):
    return np.polyval(coefs, x)

# Interface com Streamlit
st.title("Ajuste de Função do Terceiro Grau")

st.write("Insira os pares ordenados (x, y) abaixo.")

num_pontos = st.number_input("Número de pontos", min_value=2, value=4, step=1)

x_vals = []
y_vals = []

for i in range(num_pontos):
    col1, col2 = st.columns(2)
    x = col1.number_input(f"X{i+1}", value=float(i+1))
    y = col2.number_input(f"Y{i+1}", value=float(i+2))
    x_vals.append(x)
    y_vals.append(y)

if st.button("Calcular Função"):
    try:
        x = np.array(x_vals)
        y = np.array(y_vals)
        
        # Ajustar polinômio
        coeficientes = ajustar_polinomio(x, y)
        
        # Exibir a função encontrada
        st.write(f"Função encontrada: f(x) = {coeficientes[0]:.4f}x³ + {coeficientes[1]:.4f}x² + {coeficientes[2]:.4f}x + {coeficientes[3]:.4f}")
        
        # Gerar gráfico
        x_range = np.linspace(min(x) - 1, max(x) + 1, 100)
        y_range = gerar_polinomio(coeficientes, x_range)
        
        fig, ax = plt.subplots()
        ax.scatter(x, y, color='red', label='Pontos fornecidos')
        ax.plot(x_range, y_range, label='Ajuste cúbico', color='blue')
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()
        
        # Exibir gráfico no Streamlit
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Erro ao processar os dados: {e}")
