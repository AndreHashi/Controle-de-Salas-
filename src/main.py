import streamlit as st 

st.title('Controle de Acesso às Salas Nexxo') 

LIMITES_SALAS = {
                'Nexxo 1': 50,
                'Nexxo 2': 50
}

if 'ocupacao' not in st.session_state:
     st.session_state.ocupacao = {sala: [] for sala in LIMITES_SALAS}

sala = st.selectbox('Escolha uma sala', list(LIMITES_SALAS.keys()))
nome = st.text_input('')

if st.button('Reservar Sala'):
    ocupantes = st.session_state.ocupacao[sala]
    limite = LIMITES_SALAS[sala]
        
    if len(ocupantes) >= limite:
        st.error("❌ Limite de pessoas atingido!")
    elif nome.strip() == "":
        st.warning("⚠️ Digite um nome válido.")
    elif nome in ocupantes:
        st.warning("⚠️ Essa pessoa já reservou essa sala.")
    else:
        ocupantes.append(nome)
        st.success(f"✅ {nome} reservou a {sala} com sucesso!")

st.subheader("📊 Ocupação Atual:")
for nome_sala, limite in LIMITES_SALAS.items():
    ocupantes = st.session_state.ocupacao[nome_sala]
    ocupados = len(ocupantes)
    st.write(f"🔹 {nome_sala}: {ocupados}/{limite} pessoas")
    st.progress(ocupados / limite if limite else 0)







    