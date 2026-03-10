from rembg import remove
from PIL import Image
from pathlib import Path

input_folder = Path("img_input")
output_folder = Path("img_output")

valid_extensions = (".png", ".jpg", ".jpeg")

def remover_fundo(input_path, output_path):
    img = Image.open(input_path)
    img_removed = remove(img)
    img_removed.save(output_path)

def processar_imagens():

    for file in input_folder.iterdir():

        if file.suffix.lower() in valid_extensions:

            output_path = output_folder / f"removed_{file.name}"

            print(f"Processando: {file.name}")

            remover_fundo(file, output_path)

    print("Todas as imagens foram processadas!")

if __name__ == "__main__":
    processar_imagens()