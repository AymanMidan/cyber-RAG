from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import glob

# Etape 1 : charger les PDFs
all_docs = []
pdfs = glob.glob("data/*.pdf")
print(f"PDFs trouvés : {pdfs}")

for pdf in pdfs:
    loader = PyPDFLoader(pdf)
    docs = loader.load()
    all_docs.extend(docs)

# Etape 2 : découper en chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(all_docs)
print(f"{len(chunks)} chunks prêts")

# Etape 3 : vectoriser et stocker
print("Génération des embeddings... patience 10-15 min")

embedding_model = OllamaEmbeddings(model="nomic-embed-text")

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="vectordb"
)

print("TERMINÉ ! Vector DB prête dans vectordb/")