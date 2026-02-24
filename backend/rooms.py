import uuid

rooms = {}

def create_room(media_type: str, media_source: str):
    room_id = str(uuid.uuid4())[:8]

    rooms[room_id] = {
        "media_type": media_type,
        "media_source": media_source,
        "clients": set(),
        "host": None,
        "is_playing": False,
        "current_time": 0.0
    }

    return room_id

def get_room(room_id: str):
    return rooms.get(room_id)
