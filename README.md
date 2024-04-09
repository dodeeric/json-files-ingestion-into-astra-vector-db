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