from fastapi.responses import FileResponse, StreamingResponse
import os
import uuid
from fastapi import WebSocket, UploadFile, File, FastAPI, Request, Form
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from websocket import websocket_endpoint
from rooms import rooms, create_room as create_new_room
from video_manager import save_video

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Watch Together backend running"}

@app.post("/create-room")
async def create_room_endpoint(
    media_type: str = Form("local"),
    media_source: str = Form(""),
    file: Optional[UploadFile] = File(None)
):
    source = media_source
    if media_type == "local" and file is not None:
        source = await save_video(file)
    
    room_id = create_new_room(media_type, source)
    return {"room_id": room_id}

@app.websocket("/ws/{room_id}")
async def ws_route(websocket: WebSocket, room_id: str):
    await websocket_endpoint(websocket, room_id)

@app.get("/video/{filename}")
def get_video(filename: str):
    video_path = os.path.join("uploads", filename)

    if not os.path.exists(video_path):
        return {"error": "Video not found"}

    return FileResponse(
        video_path,
        media_type="video/mp4"
    )

@app.get("/room-info/{room_id}")
def room_info(room_id: str):
    if room_id not in rooms:
        return {"error": "Room not found"}

    return {
        "media_type": rooms[room_id]["media_type"],
        "media_source": rooms[room_id]["media_source"]
    }

@app.on_event("shutdown")
def cleanup_uploads():
    upload_dir = "uploads"
    if os.path.exists(upload_dir):
        for filename in os.listdir(upload_dir):
            file_path = os.path.join(upload_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

    rooms.clear()