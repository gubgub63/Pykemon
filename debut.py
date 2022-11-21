import pygame
from pytmx.util_pygame import load_pygame
from pygame.locals import *
 
pygame.init()
fenetre = pygame.display.set_mode((480, 480))#,RESIZABLE)
 
MAP = load_pygame("Pellet Town.tmx")
 
def Affichage_MAP(Couche):
    for Ligne in range(15):
        for Colonne in range(15):
            Cellule = MAP.get_tile_image(Colonne, Ligne, Couche)
            Axe_X = Colonne * 12
            Axe_Y = Ligne * 12
            fenetre.blit(Cellule, (Axe_X, Axe_Y))
    pygame.display.flip()
 
Affichage_MAP(0)
