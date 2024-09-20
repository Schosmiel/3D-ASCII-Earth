import pygame as pg
import numpy as np
from math import pi, sin, cos

# Initialisation de Pygame
pg.init()

# Configuration de l'affichage
WIDTH, HEIGHT = 800, 800
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('ASCII 3D EARTH')

# Configuration du temps
clock = pg.time.Clock()
FPS = 30

# Paramètres de la sphère
R = 250
MAP_WIDTH = 40
MAP_HEIGHT = 20

class Projection:
    def __init__(self):
        self.background = (10, 10, 60)
        self.surfaces = {}

    def addSurface(self, name, surface):
        self.surfaces[name] = surface

    def display(self):
        screen.fill(self.background)

        for surface in self.surfaces.values():
            for node in surface.nodes:
                pg.draw.circle(screen, (255, 255, 255), (WIDTH // 2 + int(node[1]), HEIGHT // 2 + int(node[2])), 2, 0)

    def rotateAll(self, theta):
        c, s = np.cos(theta), np.sin(theta)
        matrix = np.array([[c, -s, 0, 0],
                           [s, c, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])

        for surface in self.surfaces.values():
            center = surface.findCentre()
            surface.rotate(center, matrix)

class Object:
    def __init__(self, nodes):
        self.nodes = np.hstack((nodes, np.ones((len(nodes), 1))))

    def findCentre(self):
        return self.nodes.mean(axis=0)

    def rotate(self, center, matrix):
        self.nodes = center + np.dot(self.nodes - center, matrix.T)

# Préparation des coordonnées de la sphère
xyz = [(round(R * sin(lat) * cos(lon), 2),
        round(R * sin(lat) * sin(lon), 2),
        round(R * cos(lat), 2))
       for lat in np.linspace(0, pi, MAP_HEIGHT + 1)
       for lon in np.linspace(0, 2*pi, MAP_WIDTH + 1)]

# Initialisation des objets
pv = Projection()
globe = Object(np.array(xyz))
pv.addSurface('globe', globe)

spin = 0
running = True
while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pv.rotateAll(spin)
    pv.display()

    pg.display.flip()
    spin += 0.05

pg.quit()
