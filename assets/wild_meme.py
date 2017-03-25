import os
import os.path as path
import itertools
import random #random.shuffle

from shutil import rmtree as rm_rf
from PIL import Image


#os.listdir()
#os.mkdir()

def crop_box(box_pixel_size, x_start, y_start):
    return (box_pixel_size * x_start,
            box_pixel_size*y_start,
            box_pixel_size * (1 + x_start),
            box_pixel_size * (1 + y_start))


def crop_list(px_size, x_divisions, y_divisions):
    return [crop_box(px_size, x, y)
            for x, y
            in itertools.product(range(x_divisions),
                                 range(y_divisions))]


def slice_to_pieces(image_obj, px_size, ver_pieces, hor_pieces):
    crop_boxes = crop_list(px_size, ver_pieces, hor_pieces)
    return [image_obj.crop(crop_box) for crop_box in crop_boxes]


def build_from_pieces(pieces_list, size=(500, 375), pixel_size=125):
    frame = Image.new('RGBA', size, (255, 255, 255))
    locations = crop_list(pixel_size,
                          size[0] // pixel_size,
                          size[1] // pixel_size)

    image = frame
    for piece, location in zip(pieces_list, locations):
        image.paste(piece, location)

    image.show()
    return image


class LeftBeef:
    def clean():
        rm_rf('left-beef')

    def observe_meme():
        meme_root = 'left-beef'
        if os.path.exists(meme_root):
            rm_rf(meme_root)

        image = Image.open('./assets/meat-left.jpg').convert('RGBA')
        pieces = slice_to_pieces(image, 125, 4, 3)

        string_heads = [x for x in range(len(pieces))]
        random.shuffle(string_heads)

        os.mkdir('./left-beef')
        for piece, head in zip(pieces, string_heads):
            piece.save('left-beef/{}-left-beef.jpg'.format(head))

        return "A meaty meme has been observed in 'left-beef/' directory, enjoy!"

    def capture(path_list):
        pieces = [Image.open(file) for file in path_list]

        build_from_pieces(pieces)

        return path_list
