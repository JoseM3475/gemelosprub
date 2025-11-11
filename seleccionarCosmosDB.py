from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient, PartitionKey

import json

# Configura tus valores
endpoint = "https://josemcosmosdb2.documents.azure.com:443/"
database_name = "fanogar"
container_name = "temperaturas"

# 1️⃣ Credencial AAD (no usa claves)
credential = DefaultAzureCredential()

# 2️⃣ Crear cliente de Cosmos DB autenticado con AAD
client = CosmosClient(endpoint, credential)

# 3️⃣ Obtener referencias a base de datos y contenedor
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# query = "SELECT * FROM c WHERE NOT IS_DEFINED(c.ciudad)"

query = "SELECT * FROM c WHERE c.id = '2-antonio'"

item = container.read_item(item="2-antonio", partition_key="Toledo")
item["temperatura"] = 21
container.replace_item(item=item, body=item)

items = container.query_items(
    query=query,
    enable_cross_partition_query=True  # necesario si tienes múltiples particiones
)

# Iterar y mostrar resultados
for item in items:
    print(json.dumps(item, indent=4, ensure_ascii=False))
    
