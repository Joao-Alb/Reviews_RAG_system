import requests
from datetime import datetime, timedelta
from unix import get_last_month_first_day_unix
import json


def get_reviews(place_id, cut_off, api_key):
    """Get reviews for a place ID using the Outscraper API."""
    endpoint_url = 'https://api.app.outscraper.com/maps/reviews-v2'
    headers = {
        'X-API-KEY': api_key
    }
    params = {
        'query': place_id,
        'cutoff': str(cut_off),
        'async':'false',
        "reviewsLimit":0
    }
    response = requests.get(endpoint_url, headers=headers, params=params)
    data = response.json().get('data', [])
    if not data:
        return []
    reviews = data[0].get('reviews_data', [])
    print(len(reviews))
    return reviews

def get_last_month_reviews(api_key,place_id)->list:
    month = get_last_month_first_day_unix()
    return get_reviews(place_id,month,api_key)

def export_last_month_reviews(api_key,place_id):
    reviews = get_last_month_reviews(api_key,place_id)
    with open("avaliacoes.json", "w") as f:
        json.dump({"avaliacoes_maps":reviews},f)