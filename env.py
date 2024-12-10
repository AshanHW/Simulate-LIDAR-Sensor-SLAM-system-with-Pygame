import math
import pygame

from utils import *
from constants import *



class Environment:
    def __init__(self, map_path, map_dims):
        pygame.init()

        self.pointCloud = [] # Store detected obstacle point cordinates

        self.externalMap = pygame.image.load(map_path) # loading the external map (image)
        self.mapW, self.mapH = map_dims

        self.mapWindowName = "Lidar Simulator"
        pygame.display.set_caption(self.mapWindowName)

        self.map = pygame.display.set_mode((self.mapW, self.mapH)) # making the main map
        self.map.blit(self.externalMap, (0,0)) # Overlay the external map on main map

        self.infomap = None # To show the sensor data
        
        # To show sensor data
        self.featuremap = pygame.Surface((self.mapW, self.mapH), pygame.SRCALPHA)
        self.featuremap.fill((0, 0, 0, 0))


    def process_raw_data(self, sensor_data):
        '''
        Takes sensor data[[distance, angle, position], ] as a parameter &
        get the coordinates of the detected points & append it to the
        pointCloud array
        '''
        if sensor_data != False:
            for record in sensor_data:
                # get the coords of the obstacle point
                point = get_cartesian_coords(record[0], record[1], record[2])

                if point not in self.pointCloud:
                    self.pointCloud.append(point)

    def show_sensor_data(self, color):

        # Place detected points on infomap
        for point in self.pointCloud:
            self.infomap.set_at( (int(point[0]), int(point[1])), color )

    def show_cluster_data(self, labels, clusters):

        self.colour_Map =  {}
        for label in clusters:
            if label == -1:
                self.colour_Map[label] = RED
            else:
                self.colour_Map[label] = random_colour()
        

        for i, point in enumerate(self.pointCloud):

            label = labels[i]
            colour  = self.colour_Map[label]

            self.featuremap.set_at((int(point[0]), int(point[1])), colour)
