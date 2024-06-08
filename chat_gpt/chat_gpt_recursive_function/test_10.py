import requests

def get_city_description(city_name):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{city_name}"
    response = requests.get(url)
    data = response.json()
    if 'extract' in data:
        return data['extract']
    else:
        return "Description not available"

city_name = "Paris"
description = get_city_description(city_name)
print(description)
