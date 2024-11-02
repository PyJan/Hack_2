from openai import AzureOpenAI
import keyring, os
from create_sample_apis import return_db_samples

def call_azure(data, source):
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
                "role": "system",
                "content": """You are a python code generator assistant. You create only code-related content.
                           Your task is to generate one single data loading function which filters and aggregates
                           the data. Use a very specific function name which contains description of what it does. Be creative with the function body. Assume that provided data sample
                            is stored in an SQLite database. Include one sample call of the function immediately
                            at the end of the code. Do not include ```python at the beginning of your answer. Your answer
                            should be directly executable in python console.
                            """
            },
            {
                "role": "user",
                "content": f"""Create loader function for data stored in data/chinook.db in table {source}. Sample is this:
                {data}
                """,
            },
        ],
        max_tokens=1000,
        temperature=0.5,
        top_p=0.5,
    )
    return completion.choices[0].message.content

def save_to_file(content, filename):
    os.makedirs('generated_api', exist_ok=True)
    with open(os.path.join('generated_api', filename), 'w') as file:
        file.write(content)

if __name__ == '__main__':
    db_samples = return_db_samples()
    for source, data in db_samples.items():
        try:
            returned_api = call_azure(data, source)
            exec(returned_api)
            save_to_file(returned_api, f"{source}_api.py")
        except Exception as e:
            print(f"source: {source} failed")
            continue

