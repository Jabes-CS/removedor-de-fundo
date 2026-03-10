from rembg import remove
from PIL import Image
import os

input_folder = "img_input"
output_folder = "img_output"

# percorre todos os arquivos da pasta
for file in os.listdir(input_folder):

    input_path = os.path.join(input_folder, file)
    output_path = os.path.join(output_folder, f"removed_{file}")

    print(f"Processando: {file}")

    img = Image.open(input_path)
    img_removed = remove(img)

    img_removed.save(output_path)

print("Todas as imagens foram processadas!")