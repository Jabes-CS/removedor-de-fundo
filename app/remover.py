from rembg import remove
from PIL import Image


def remover_fundo(input_path, output_path):

    img = Image.open(input_path)
    img_removed = remove(img)
    img_removed.save(output_path)