import os
import requests


def sanitize_query(query):
    allowed_chars = 'qwertyuiopasdfghjklçzxcvbnm'
    allowed_chars += allowed_chars.upper()
    allowed_chars += '0123456789'
    allowed_chars += ',;- '
    allowed_chars = set(allowed_chars)

    if len(query) > 128:
        query = query[:128]

    sanitized_query = ''.join([char for char in query
                               if char in allowed_chars])
    return sanitized_query


def request_weather_api(query):
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    api_url = 'http://api.openweathermap.org/data/2.5/weather'
    payload = {'q': query, 'appid': api_key}

    r = requests.get(api_url, params=payload)
    return r.json()


if __name__ == '__main__':
    pass
