"""
use keyring to safely setup API keys locally, original usage is

import keyring
keyring.set_password("system", "username", "password")
keyring.get_password("system", "username")
"""

import keyring

setup = {
    'jans-third-source':  ('https://jans-third-source.openai.azure.com', '2024-02-15-preview'),  # Azure endpoint, API version
    'my-east-us-for-jan': ("https://my-east-us-for-jan.openai.azure.com/openai/deployments/gpt-4o-mini/chat/completions?api-version=2024-02-15-preview", 'xxx'),  # endpoint, place holder
    'storage-connection-string': ("storage-connection-string", 'xxx'),  # storage connection string
    'search-api-key': ("search-api-key", 'xxx'),  # search api key
}

def main():
    for source_info in setup.values():
        api_key = keyring.get_password(source_info[0], source_info[1])
        if api_key is not None:
            print(f'api key exists for {source_info[0]} and {source_info[1]}: {api_key}')
        else:
            api_key = input(f"API key for {source_info[0]} and {source_info[1]}: ")
            keyring.set_password(source_info[0], source_info[1], api_key)
    print('Finished setting up all API keys')


if __name__ == '__main__':
    main()