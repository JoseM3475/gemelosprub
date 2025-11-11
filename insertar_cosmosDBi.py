from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient, PartitionKey

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

# 4️⃣ Insertar un nuevo ítem con clave de partición "/ciudad"
item = {
    "id": "2-anabel",
    "ciudad": "Granada",
    "temperatura": 218,
    "fecha": "2025-11-10",
    "coordenadas" : [8, 415, 234]
}

container.create_item(body=item)
print("✅ Ítem insertado correctamente.")