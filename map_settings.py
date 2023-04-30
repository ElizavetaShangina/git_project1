import random
import requests

map_types = ['map', 'sat']

def map_setting(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        print('ERROR', response)
        return

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    point_toponym = list(toponym_coodrinates.split())
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
    address_ll = ','.join(point_toponym)
    search_params = {
        "apikey": api_key,
        "text": "достопримечательность",
        "lang": "ru_RU",
        "ll": address_ll,
        "type": "biz"}

    response = requests.get(search_api_server, params=search_params)
    json_response = response.json()
    map_params = []
    for i in range(4):
        map_type = map_types[random.randint(0, 1)]
        point = json_response["features"][i]["geometry"]["coordinates"]
        org_point = "{0},{1}".format(point[0], point[1])
        delta = "0.01"
        map_params.append({
            "ll": org_point,
            "spn": ",".join([delta, delta]),
            "l": map_type})
    return map_params
