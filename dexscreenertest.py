import requests
import time

API_URL = "https://api.dexscreener.com/token-profiles/latest/v1"
MAX_REQUESTS_PER_MIN = 60

for i in range(MAX_REQUESTS_PER_MIN):  # Make 60 requests
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list):  # Ensure data is a list
         for token in data:  # Loop through each token entry
            print("\n--- Token Profile ---")
            print(f"URL: {token.get('url', 'N/A')}")
            print(f"Chain ID: {token.get('chainId', 'N/A')}")
            print(f"Token Address: {token.get('tokenAddress', 'N/A')}")
            print(f"Description: {token.get('description', 'N/A')}")
           
    
    time.sleep(1)  # 1-second delay (60 requests per minute)










