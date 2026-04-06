import requests
from rest_framework.exceptions import ValidationError

def get_place_from_api(external_id: int):
    url = f"https://api.artic.edu/api/v1/artworks/{external_id}"
    responce = requests.get(url)

    if responce.status_code !=200:
        raise ValidationError("Place not found in external API")
    
    data = responce.json().get("data")

    if not data:
        raise ValidationError("Invalid API response")
    
    return data
