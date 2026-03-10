from rembg import remove
from PIL import Image

input_path = 'img_input/favicon.png'
output_path = 'img_output/img_removed.png'

img = Image.open(input_path)
img_removed = remove(img)

img_removed.save(output_path)