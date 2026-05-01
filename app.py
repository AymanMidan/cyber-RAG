from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma

app = FastAPI()

# Charger la Vector DB déjà créée
embedding_model = OllamaEmbeddings(model="nomic-embed-text")

vector_db = Chroma(
    persist_directory="vectordb",
    embedding_function=embedding_model
)

# Retriever : cherche les 3 chunks les plus proches
retriever = vector_db.as_retriever(search_kwargs={"k": 3})

# Le LLM qui génère la réponse
llm = ChatOllama(model="qwen2.5:3b")

# Structure de la requête
class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):

    docs = retriever.invoke(query.question)
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""You are a cybersecurity assistant.
Answer ONLY based on the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query.question}
"""
    response = llm.invoke(prompt)

    # Extraire les sources depuis les métadonnées des chunks
    sources = list(set([
        doc.metadata.get("source", "unknown") for doc in docs
    ]))

    return {
        "answer": response.content,
        "sources": sources
    }