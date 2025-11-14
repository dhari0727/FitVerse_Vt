import requests

api_key = 'sk_live_nvxiPPLqreB-o-c11d89i-Qg7rwjIFgHxSW3K5JqXh8' # ← Replace with your actual API key
job_id = "1df9542e-a524-4ca4-b8aa-858b1b5ecb81"
url = f"https://backend.miragic.ai/api/v1/virtual-try-on/{job_id}"

headers = {
    "X-API-Key": api_key
}
response = requests.get(url, headers=headers)

# Print status code and response JSON
print("Status Code:", response.status_code)
print("Response:", response.json())