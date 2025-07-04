from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import UploadFile, File

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/hello/{name}")
def greet(name: str):
    return {"greeting": f"Hello, {name}!"}

# POST endpoint with a Pydantic model
@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "content_type": file.content_type, "size": len(content)}
