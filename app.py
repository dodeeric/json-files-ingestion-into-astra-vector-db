import os
import jq
from dotenv import load_dotenv
from langchain_community.document_loaders import JSONLoader
from langchain_openai import OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore

load_dotenv()

ASTRA_DB_APPLICATION_TOKEN = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT = os.environ.get("ASTRA_DB_API_ENDPOINT")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

Google Colab:

os.environ["ASTRA_DB_APPLICATION_TOKEN"] = getpass("ASTRA_DB_APPLICATION_TOKEN = ")
os.environ["ASTRA_DB_API_ENDPOINT"] = input("ASTRA_DB_API_ENDPOINT = ")
os.environ["OPENAI_API_KEY"] = getpass("OPENAI_API_KEY = ")

from google.colab import drive
drive.mount('/content/drive')

-

loader = JSONLoader(file_path="balat-ds1b-wcc-cheerio-ex_2024-04-06_09-05-15-262.json", jq_schema=".[]", text_content=False)
documents = loader.load()

embeddings = OpenAIEmbeddings()

1. Specify the embeddings model, database, and collection to use. If the collection does not exist, it is created automatically.

astravstore = AstraDBVectorStore(
    embedding=embeddings,
    collection_name="bmae-test",
    token=os.environ["ASTRA_DB_APPLICATION_TOKEN"],
    api_endpoint=os.environ["ASTRA_DB_API_ENDPOINT"],
)

INFO: 2. Load a small dataset of philosophical quotes with the Python dataset module.

philo_dataset = load_dataset("datastax/philosopher-quotes")["train"]
print("An example entry:")
print(philo_dataset[16])

INFO: 3. Process metadata and convert to ***LangChain documents***.

docs = []
for entry in philo_dataset:
    metadata = {"author": entry["author"]}
    if entry["tags"]:
        # Add metadata tags to the metadata dictionary
        for tag in entry["tags"].split(";"):
            metadata[tag] = "y"
    # Add a LangChain document with the quote and metadata tags
    doc = Document(page_content=entry["quote"], metadata=metadata)
    docs.append(doc)

INFO: 4. Compute embeddings for each document and store in the database.

inserted_ids = astravstore.add_documents(docs)
print(f"\nInserted {len(inserted_ids)} documents.")

INFO: 5. Show quotes that are similar to a specific quote.

results = astravstore.similarity_search("Our life is what we make of it", k=3)
for res in results:
    print(f"* {res.page_content} [{res.metadata}]")

pinecone = PineconeVectorStore.from_documents(documents, embeddings, index_name=index_name)
astra = astravstore.add_documents(documents)

