from typing import Union

from fastapi import FastAPI
from audio_to_video_flask import convert_video_to_audio

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/helo")
def read_root():
    return {"Hello": "online World"}

@app.post('/convert_video_to_audio')
def extract_audio_action(video_path: str):
    res = convert_video_to_audio(video_path)
    return {"res": res}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}