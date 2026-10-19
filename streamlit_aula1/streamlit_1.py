import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Atacadao",
    page_icon="🛒",
    layout="centered"
)

st.title("Meu primeiro dash")
st.subheader("Victor Josias Parreiras Peluzo")

st.divider()

st.write("Olá, mundo")

nome_usuario = "Victor Josias"
idade_usuario = 17 
st.write(f"Usuário conectado: {nome_usuario} | Idade: {idade_usuario} anos")

st.divider()

df = pd.DataFrame({
    'Matérias': ['Português', 'Matemática', 'Python', 'Frame'],
    'Notas': [5, 9, 7, 10]
})

st.write("Visualização dos dados obtidos:")
st.dataframe(df) 

st.divider()

st.subheader("Caixa de Supermercado")

produtos_disponiveis = {
    "Arroz 5kg": 26.90,
    "Feijão 1kg": 7.50,
    "Café 500g": 18.20,
    "Leite 1L": 5.49
}

col1, col2 = st.columns(2)

with col1:
    item_escolhido = st.selectbox(
        "Escolha um item para comprar:",
        options=list(produtos_disponiveis.keys())
    )

with col2:
    quantidade = st.number_input("Digite a quantidade desejada:", min_value=1, value=1, step=1)

def calcular_preco_total(item, qtd):
    preco_unitario = produtos_disponiveis[item]
    return preco_unitario * qtd

valor_total = calcular_preco_total(item_escolhido, quantidade)

st.metric(label="Total da Compra", value=f"R$ {valor_total:.2f}")

st.divider()

st.subheader("Calculadora de Troco")

valor_pago = st.number_input("Digite o valor entregue pelo cliente (R$):", value=0.0, step=1.0)

if st.button("Calcular", type="primary"):
    if valor_pago < valor_total:
        st.error(f"Valor insuficiente! O total da compra é R$ {valor_total:.2f} e faltam R$ {(valor_total - valor_pago):.2f}.")
    else:
        troco = valor_pago - valor_total
        st.success(f"**Resultado:** Troco a devolver: R$ {troco:.2f}")