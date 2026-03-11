from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, HTMLResponse
import uuid
from pathlib import Path
from app.remover import remover_fundo

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    with open("app/templates/index.html", encoding="utf-8") as f:
        return f.read()

input_folder = Path("img_input")
output_folder = Path("img_output")

input_folder.mkdir(exist_ok=True)
output_folder.mkdir(exist_ok=True)


@app.post("/remover-fundo")
async def remover(file: UploadFile = File(...)):

    nome_original = Path(file.filename).stem

    input_path = input_folder / file.filename
    output_path = output_folder / f"{nome_original}_fundo_removido.png"

    with open(input_path, "wb") as buffer:
        buffer.write(await file.read())

    remover_fundo(input_path, output_path)

    return FileResponse(output_path)