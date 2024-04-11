# json-files-ingestion-into-astra-vector-db
Ingest JSON files into a DataStax Astra Vector DB (serverless). Each "chunk" is one JSON item.

Create a .env file with the following credentials:

ASTRA_DB_APPLICATION_TOKEN="AstraCS:xxxxxx"

ASTRA_DB_API_ENDPOINT="https://xxxxxx.apps.astra.datastax.com"

OPENAI_API_KEY="sk-xxxxxx"

Edit app.py to add the JSON file path and the Astra Vector DB Collection name:

file_path = "myfile.json"

collection_name = "mycollection"

Run these two commands:

pip install -r requirements.txt

python app.py

Remarks: 

- If the collection does not exist, it will be created.
- Go to https://astra.datastax.com to display the collection (json items and vectors).
- The `JSONLoader` class from the `langchain_community.document_loaders` library is designed to load data from JSON files into Document objects. This is particularly useful in contexts where structured JSON data needs to be transformed into a format that's more conducive to processing or analysis, typically in natural language processing (NLP) or data retrieval applications.

