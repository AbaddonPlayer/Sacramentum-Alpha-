import pygame
from csv import reader
from os import walk

def import_csv_layout(path):
    trn_map = []
    with open(path) as level_map:
        layout  = reader(level_map,delimiter = ',')
        for row in layout:
            trn_map.append(list(row))
        return trn_map

def import_folder(path):
    srf_list = []
    
    for _,__,img_fil in walk(path):
        for image in img_fil:
            full_path = path + '/' + image
            img_srf = pygame.image.load(full_path).convert_alpha()
            srf_list.append(img_srf)

    return srf_list
    