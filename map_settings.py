import requests

def map_setting(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        print('ERROR')
        return

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]

    toponym_coodrinates = toponym["Point"]["pos"]
    upper_corner = list(map(float, toponym["boundedBy"]["Envelope"]['upperCorner'].split()))
    lower_corner = list(map(float, toponym["boundedBy"]["Envelope"]['lowerCorner'].split()))
    points = [i for i in toponym_coodrinates.split()]
    spn = [str(upper_corner[0] - lower_corner[0]), str(upper_corner[1] - lower_corner[1])]
    map_params = {
        "l": "map",
        "pt": "{0},pm2dgl".format(','.join(points)),
        "ll": ','.join(points),
        "spn": ','.join(spn)
    }
    return map_params