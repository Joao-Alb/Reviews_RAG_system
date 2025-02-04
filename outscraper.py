import requests
from datetime import datetime, timedelta
from unix import get_last_month_first_day_unix
import json

DEFAULT_PARAMS = {
    "async": "false",
    "reviewsLimit": 0
}

def call_api(endpoint_url, headers, params=None):
    params = params or {}
    try:
        response = requests.get(endpoint_url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API call failed: {e}")
        return {}

def get_reviews(place_id, cut_off, api_key):
    """Get reviews for a place ID using the Outscraper API."""
    endpoint_url = 'https://api.app.outscraper.com/maps/reviews-v2'
    headers = {
        'X-API-KEY': api_key
    }
    params = {
        'query': place_id,
        'cutoff': str(cut_off),
        'async':DEFAULT_PARAMS["async"],
        "reviewsLimit":DEFAULT_PARAMS['reviewsLimit']
    }
    response = call_api(endpoint_url, headers, params)
    data = response.get('data', [])
    if not data:
        return []
    reviews = data[0].get('reviews_data', [])
    print(F"Number of reviews returned: {len(reviews)}")
    return reviews

def get_last_month_reviews(api_key,place_id)->list:
    month = get_last_month_first_day_unix()
    return get_reviews(place_id,month,api_key)

def export_last_month_reviews(api_key, place_id):
    reviews = get_last_month_reviews(api_key, place_id)
    if reviews:
        with open("avaliacoes.json", "w", encoding="utf-8") as f:
            json.dump({"avaliacoes_maps": reviews}, f, ensure_ascii=False, indent=2)
