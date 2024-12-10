import math
import pygame
import numpy as np

from utils import *
from constants import *

class LidarSensor:
    def __init__(self, range, map, noise):
        self.range = range  # range of the sensor

        self.sigma = np.array([noise[0], noise[1]]) # Noise

        self.position = (0,0) # position

        self.map = map
        self.W, self.H = pygame.display.get_surface().get_size() # map dims


    def detect_obstacle(self, detection_color, angle_rate = ANGLE_RATE, sample_rate = SAMPLE_RATE ):
        data = []

        x1, y1 = self.position[0], self.position[1]

        # Rotating the sensor
        for angle in np.linspace(0, 2*math.pi, angle_rate, False): # False flag avoid 2 same angles
            # (x2, y2) is the endpoint of the sensor's range
            x2 = x1 + self.range * math.cos(angle)
            y2 = y1 + self.range * math.sin(angle)

            # Sampling the line from self position to range endpoint
            for i in range(sample_rate):
                # interpolation for sampling
                u = i/sample_rate

                x = int(x2 * u + x1 * (1-u))
                y = int(y2 * u + y1 * (1-u))

                if 0<x<self.W and 0<y<self.H: # within the map
                    colour = self.map.get_at((x,y)) # get the colour of the sample point
                    
                    if (colour[0], colour[1], colour[2]) == detection_color: # set as a color of an obstacle. Change accordingly
    
                        distance = euclidean_distance((self.position), (x,y))

                        output = add_noise(distance, angle, self.sigma)
                        # output is [distance, angle]
                        output.append(self.position)
                        # output is [distance from self.pos , angle from self.pos , self position]
                        data.append(output)
                        break # Laser do not detect past the obstacle
        if len(data) > 0:
            return data
        else:
            # no detection
            return False
