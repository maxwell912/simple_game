from os import listdir
from os import path
from os.path import isfile, join

import pygame


def get_all_images(mypath) -> list[str]:
    paths = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
    return paths


def make_pygame_image(image_path, cell_size: int):
    cube_image = pygame.image.load(image_path)
    return pygame.transform.scale(cube_image, (cell_size, cell_size))


class ImageRepo:
    def __init__(self, image_path: path, cell_size: int):
        images = get_all_images(image_path)
        self.pygame_images = dict()
        for im in images:
            self.pygame_images[path.basename(im)] = make_pygame_image(im, cell_size)

    def get_image(self, name: str):
        if name not in self.pygame_images:
            raise RuntimeError('Изображение ' + name + ' не найденов списке ' + str(list(self.pygame_images.keys())))
        return self.pygame_images[name]
