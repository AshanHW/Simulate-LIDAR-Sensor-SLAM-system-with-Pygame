from env import Environment
from constants import *
from sensor import LidarSensor

import math
import pygame

environment = Environment('map1.png', (1152,720))
originalMap = environment.map.copy()

lidar = LidarSensor(RANGE, originalMap, noise=(0.5, 0.01))

environment.map.fill(BLACK)
environment.infomap = environment.map.copy()


running = True

while running:
    sensorON = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_focused():
            sensorON = True
        elif not pygame.mouse.get_focused():
            sensorON = False

    if sensorON:
        position = pygame.mouse.get_pos()
        lidar.position = position
        sensor_data = lidar.detect_obstacle()
        environment.process_raw_data(sensor_data)
        environment.show_sensor_data()

    # Displaying the infomap on main map
    environment.map.blit(environment.infomap, (0,0))
    pygame.display.update()

