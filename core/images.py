from typing import Optional, Tuple

import pygame as pg


BASE_IMAGE_PATH = "data/images/"

def load_image(path: str, size: Optional[Tuple[int, int]] = None) -> pg.Surface:
    image = pg.image.load(file=BASE_IMAGE_PATH + path).convert()
    image.set_colorkey((0, 0, 0)) # make background transparent
    
    if size:
        image = pg.transform.scale(image, size)
        
    return image