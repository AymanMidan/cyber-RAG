from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import glob

all_docs = []

# Chercher tous les PDFs dans data/
pdfs = glob.glob("data/*.pdf")
print(f"PDFs trouvés : {pdfs}")

for pdf in pdfs:
    loader = PyPDFLoader(pdf)
    docs = loader.load()
    all_docs.extend(docs)
    print(f"  {pdf} → {len(docs)} pages chargées")

# Découper en chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(all_docs)
print(f"\nNombre total de chunks : {len(chunks)}")