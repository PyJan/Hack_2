from openai import AzureOpenAI
import keyring

# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
    # https://learn.microsoft.com/azure/ai-services/openai/reference#rest-api-versioning
    api_version="2024-02-15-preview",
    # https://learn.microsoft.com/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint="https://jans-third-source.openai.azure.com",
    api_key = keyring.get_password("https://jans-third-source.openai.azure.com", "2024-02-15-preview")
)

completion = client.chat.completions.create(
    model="gpt-4o",  # e.g. gpt-35-instant
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
    max_tokens=1000,
    temperature=0.5,
    top_p=0.5,
)
print(completion.choices[0].message.content)