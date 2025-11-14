import requests
import os

api_key = "sk_live_nvxiPPLqreB-o-c11d89i-Qg7rwjIFgHxSW3K5JqXh8"
base_url = "https://backend.miragic.ai"

def clean_path(p):
    return p.strip().replace('"', '').replace("'", "")

def virtualtryon():
    human_path = clean_path(input("Enter path of human image: "))
    cloth_path = clean_path(input("Enter path of cloth image: "))
    garment_type = input("Enter garment type (upper_body / lower_body / full_body): ").strip()

    url = f"{base_url}/api/v1/virtual-try-on"

    files = [
        ('humanImage', (os.path.basename(human_path), open(human_path, 'rb'), 'image/jpeg')),
        ('clothImage', (os.path.basename(cloth_path), open(cloth_path, 'rb'), 'image/jpeg'))
    ]

    headers = {
        "X-API-Key": api_key
    }

    print("\nUploading... please wait...\n")

    response = requests.post(url, headers=headers, data={"garmentType": garment_type}, files=files)

    print("STATUS:", response.status_code)
    print(response.text)

if __name__ == "__main__":
    virtualtryon()
