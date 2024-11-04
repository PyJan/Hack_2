import keyring
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient, SearchIndexerClient
from azure.search.documents.indexes.models import SearchField, SimpleField, SearchIndex, SplitSkill, SearchIndexer, SearchIndexerDataSourceConnection, SearchIndexerDataContainer, SearchIndexerDataSourceType, SearchIndexerSkillset, InputFieldMappingEntry, OutputFieldMappingEntry


def create_search_index(service_endpoint, api_key, index_name):
    credential = AzureKeyCredential(api_key)
    index_client = SearchIndexClient(endpoint=service_endpoint, credential=credential)
    fields = [
        SimpleField(name="id", type="Edm.String", key=True, searchable=True),
        SearchField(name="content", type="Edm.String", searchable=True)
    ]
    index = SearchIndex(name=index_name, fields=fields)
    index_client.create_index(index)


def index_blob_data(service_endpoint, api_key, index_name, container_name, connection_string):
    credential = AzureKeyCredential(api_key)
    indexer_client = SearchIndexerClient(endpoint=service_endpoint, credential=credential)
    data_source_connection = SearchIndexerDataSourceConnection(
        name="blob-datasource",
        type=SearchIndexerDataSourceType.AZURE_BLOB,
        connection_string=connection_string,
        container=SearchIndexerDataContainer(name=container_name)
    )
    indexer_client.create_data_source_connection(data_source_connection)

    skillset = SearchIndexerSkillset(
        name="blob-skillset",
        skills=[
            SplitSkill(
                name="text-split-skill",
                description="Split text content into smaller chunks",
                text_split_mode="pages",
                maximum_page_length=4000,
                inputs=[InputFieldMappingEntry(name="text", source="/document/content")],
                outputs=[OutputFieldMappingEntry(name="textItems", target_name="splitText")]
            )
        ]
    )
    indexer_client.create_skillset(skillset)

    indexer = SearchIndexer(
        name="blob-indexer",
        data_source_name="blob-datasource",
        target_index_name=index_name,
        skillset_name="blob-skillset"
    )
    indexer_client.create_indexer(indexer)

# Usage
ai_search_service_endpoint = "https://jansaisearch.search.windows.net"
search_api_key = keyring.get_password("search-api-key", "xxx")
index_name = "my-search-index"
connection_string = keyring.get_password("storage-connection-string", "xxx")
container_name = "api-container"
create_search_index(ai_search_service_endpoint, search_api_key, index_name)
index_blob_data(ai_search_service_endpoint, search_api_key, index_name, container_name, connection_string)
print('Finished')