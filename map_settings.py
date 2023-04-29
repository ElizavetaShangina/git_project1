import requests
from distanse import lonlat_distance

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
    search_params = {
        "apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3",
        "text": "аптека",
        "lang": "ru_RU",
        "ll": ','.join(point_toponym),
        "type": "biz"
    }
    response2 = requests.get("https://search-maps.yandex.ru/v1/", params=search_params)
    if not response2:
        print('ERROR2', response2)
        return

    json_response = response2.json()
    organization = json_response["features"][0]
    org_name = organization["properties"]["CompanyMetaData"]["name"]
    org_address = organization["properties"]["CompanyMetaData"]["address"]
    org_time = organization["properties"]["CompanyMetaData"]["Hours"]['text']
    point = list(map(str, organization["geometry"]["coordinates"]))
    print(org_name, org_address, org_time,lonlat_distance(map(float, point_toponym), map(float, point)) , sep='\n')
    map_params = {
        "l": "map",
        "pt": "{0},pm2dgl~{1},pmntl".format(','.join(point_toponym), ','.join(point))}
    return map_params
