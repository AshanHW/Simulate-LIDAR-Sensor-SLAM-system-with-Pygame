import math
import numpy as np
import pygame

from utils import *
from dbScan import Feature_Extraction
from sensor import LidarSensor
from env import Environment
from constants import *


features = Feature_Extraction(epsilon=10, min_samples=20)
environment = Environment('map3.png', (800,800))
originalMap = environment.map.copy()
sensor = LidarSensor(RANGE, originalMap, noise=(0.5, 0.01) )

environment.map.fill(BLACK)
environment.infomap = environment.map.copy()


running = True
Feature_Detection = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        # Press SPACE BAR to start feature extraction
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            Feature_Detection = True

    if not Feature_Detection:
        if pygame.mouse.get_focused():
        
            position = pygame.mouse.get_pos()
            sensor.position = position
            sensor_data = sensor.detect_obstacle(BLACK)
            environment.process_raw_data(sensor_data)
            environment.show_sensor_data(WHITE)

    elif Feature_Detection:
        
        features.pointCloud = environment.pointCloud
        labels, clusters = features.extract_features()
        environment.show_cluster_data(labels, clusters)


        Feature_Detection = False

    environment.map.blit(environment.infomap, (0,0))
    environment.map.blit(environment.featuremap, (0,0))
    pygame.display.update()