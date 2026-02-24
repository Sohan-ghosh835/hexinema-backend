from fastapi import WebSocket, WebSocketDisconnect
from rooms import get_room, rooms
import os

async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()

    room = get_room(room_id)
    if not room:
        await websocket.close()
        return

    room["clients"].add(websocket)

    if room.get("host") is None:
        room["host"] = websocket
        await websocket.send_json({
            "type": "role",
            "role": "host"
        })
    else:
        await websocket.send_json({
            "type": "role",
            "role": "viewer"
        })

    for client in room["clients"]:
        await client.send_json({
            "type": "count",
            "count": len(room["clients"])
        })

    try:
        while True:
            data = await websocket.receive_json()
            
            if data.get("action") == "ping":
                await websocket.send_json({"action": "pong"})
                continue

            for client in room["clients"]:
                if client != websocket:
                    await client.send_json(data)

    except WebSocketDisconnect:
        if websocket in room["clients"]:
            room["clients"].remove(websocket)

        if room.get("host") == websocket:
            room["host"] = None

        if len(room["clients"]) > 0:
            for client in room["clients"]:
                await client.send_json({
                    "type": "count",
                    "count": len(room["clients"])
                })
        else:
            if room["media_type"] == "local" and room["media_source"]:
                video_path = os.path.join("uploads", room["media_source"])

                if os.path.exists(video_path):
                    try:
                        os.remove(video_path)
                    except:
                        pass

            if room_id in rooms:
                del rooms[room_id]