import sys
import pygame
import requests
from map_settings import map_setting
import random


def show_picture(i, map_params):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params[i % len(map_params)])

    if not response:
        print("Ошибка выполнения запроса:")
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()


cities = ['Москва', 'Париж', 'Нью-Йорк', 'Нью-Дэли']
city = cities[random.randint(0, 3)]
map_params = map_setting(city)

if not map_params:
    print('ERROR with map')
    exit()

i, c, fps = -1, -1, 1
pygame.init()
screen = pygame.display.set_mode((600, 450))
clock = pygame.time.Clock()
for event in pygame.event.get():
    if event.type == pygame.QUIT: pygame.quit()
    else:
        i += 1
        show_picture(i, map_params)
        clock.tick(fps)
