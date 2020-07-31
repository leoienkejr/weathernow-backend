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
    if r.status_code != 200:
        raise RuntimeError('HTTP error: ' + str(r.status_code))
    return r.json()


def treat_response(json_response):
    clean_response = {'weather_id': None,
                      'main_weather': '',
                      'description': '',
                      'icon': '',
                      'temp': None,
                      'city': '',
                      'country': ''}

    clean_response['response_code'] = '200'
    clean_response['weather_id'] = json_response['weather'][0]['id']
    clean_response['main_weather'] = json_response['weather'][0]['main']
    clean_response['description'] = json_response['weather'][0]['description']
    clean_response['icon'] = json_response['weather'][0]['icon']
    clean_response['temp'] = json_response['main']['temp']
    clean_response['city'] = json_response['name']
    clean_response['country'] = json_response['sys']['country']

    return clean_response


if __name__ == '__main__':
    pass

