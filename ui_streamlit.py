import streamlit as st
import requests

st.title("Cybersecurity RAG Assistant")

# Initialiser l'historique
if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input("Pose ta question ici")

if st.button("Ask"):
    if question:
        with st.spinner("Recherche en cours..."):
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"question": question}
            )
            data = response.json()

            # Sauvegarder dans l'historique
            st.session_state.history.append({
                "question": question,
                "answer": data["answer"],
                "sources": data["sources"]
            })

    else:
        st.warning("Écris une question d'abord !")

# Afficher tout l'historique
for exchange in st.session_state.history:
    st.markdown(f"**Question :** {exchange['question']}")
    st.markdown(f"**Réponse :** {exchange['answer']}")
    st.markdown("**Sources :**")
    for source in exchange["sources"]:
        st.write(f"📄 {source}")
    st.divider()