import keyring

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import QueryType
from openai import AzureOpenAI

# Function to query the indexed data
def query_index(service_endpoint, index_name, api_key, query_text):
    search_client = SearchClient(endpoint=service_endpoint, index_name=index_name, credential=AzureKeyCredential(api_key))
    results = search_client.search(query_text, query_type=QueryType.SIMPLE)
    documents = [result['content'] for result in results][:2]
    return documents

# Function to generate a chat completion
def generate_chat_completion(openai_endpoint, openai_api_key, prompt):
    openai_client = AzureOpenAI(
        api_version="2024-02-15-preview",
        azure_endpoint=openai_endpoint,
        api_key=openai_api_key
    )
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": """You are a code generator. Always make a function call which is executable in python console. Don't describe the code."""},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()

# Usage
service_endpoint = "https://jansaisearch.search.windows.net"
index_name = "azureblob-index"
search_api_key = keyring.get_password("search-api-key", "xxx")
openai_endpoint = "https://jans-third-source.openai.azure.com"
openai_api_key = keyring.get_password("https://jans-third-source.openai.azure.com", "2024-02-15-preview")

query_text = "Find artists data."
documents = query_index(service_endpoint, index_name, search_api_key, query_text)
prompt = " ".join(documents) + "\n\n Call the artists function with random parameters"
completion = generate_chat_completion(openai_endpoint, openai_api_key, prompt)

print("Chat Completion:")
print(completion)