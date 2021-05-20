from pprint import pprint
import requests

search_location_api_url = "https://api.neshan.org/v1/search"

# Authentication API token
api_key = "service.GDwNbS3U7svILS8SwBIYqpH5PpL3rrq2Fz9v3kK8"

params = {
    'term': 'اکبر',
    'lat': 36.2880443,
    'lng': 59.615743,
}

resp = requests.get(search_location_api_url, params=params,
                    headers={'Api-key': api_key})
pprint(resp.json())
