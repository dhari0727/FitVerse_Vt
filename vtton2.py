import requests

API_KEY = "cHcOCC5oXMBu2PIpHY1zrpnZ"     # use the key shown in your Tryona dashboard

url = "https://api.tryona.com/v1/tryon/simple"

headers = {
    "accept": "application/json",
    "tokenapi": API_KEY
}

files = {
    "person_file": (
        "person.jpg",
        open(r"C:\Users\HP\Desktop\m2.jpg", "rb"),
        "image/jpeg"
    ),
    "garment_file": (
        "garment.jpg",
        open(r"C:\Users\HP\Fitverse-main\media\product_images\Linen_Pants.jpg", "rb"),
        "image/jpeg"
    ),
}

print("⏳ Sending request to Tryona...")

resp = requests.post(url, headers=headers, files=files)

print("Status:", resp.status_code)
print(resp.text)

if resp.status_code == 200:
    data = resp.json()
    print("\n✅ Try-on generated!")
    print("TUID:", data.get("tuid"))
    print("Image URL:", data.get("tryonImageUrl"))
