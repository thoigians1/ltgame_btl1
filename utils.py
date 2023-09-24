import pygame
import os

# Utility variables and functions
# Globle variables
SCREEN_WIDTH    = 640
SCREEN_HEIGHT   = 480
FPS             = 60
C_BLACK         = (0, 0, 0)
"""
    Function for loading images
    @dir_path is image's directory path
    @return sheets is list of all loaded images
"""
def load_images(dir_path: str):
    sheets = []
    print(sorted(os.listdir(dir_path), key=len))
    for file_name in sorted(os.listdir(dir_path), key=len):
        sheets.append(pygame.image.load(os.path.join(dir_path,file_name)))
    return sheets
