# Hexinema

Hexinema is a high-performance, real-time platform designed for synchronized media consumption. It allows users to create virtual rooms where they can watch local videos, YouTube content, or share their screens with others in perfect synchronization, ensuring a seamless "no desync" experience.

## Features

- Real-Time Synchronization: Powered by WebSockets to ensure all participants are watching at the exact same timestamp.
- Multiple Media Sources:
    - Local Video Uploads: Direct streaming of video files from your device.
    - YouTube Integration: Shared playback of any public YouTube video.
    - Screen Sharing: Live broadcasting of your screen to room members.
- Dynamic Room Management: Create private rooms with unique identifiers for easy sharing.
- Minimalist Interface: A clean, distraction-free UI focused on the viewing experience.

## Technology Stack

### Backend
- Framework: FastAPI (Python)
- Communication: WebSockets for real-time state synchronization
- Server: Uvicorn
- Dependencies: python-multipart, websockets

### Frontend
- Structure: Semantic HTML5
- Styling: Custom Vanilla CSS
- Logic: Modern JavaScript (ES6+)

## Project Structure

```text
.
├── backend/
│   ├── main.py              # API entry point and room creation
│   ├── websocket.py         # Real-time sync logic
│   ├── rooms.py             # Room state management
│   ├── video_manager.py     # Local file handling
│   └── requirements.txt     # Python dependencies
├── frontend/ (or root)
│   ├── index.html           # Landing page
│   ├── room.html            # Media playback interface
│   ├── script.js            # Frontend logic and WebSocket client
│   └── style.css            # Custom styling
└── DEPLOYMENT.md            # Detailed deployment instructions
```

## Getting Started

### Prerequisites
- Python 3.8+
- Modern Web Browser (Chrome, Firefox, or Safari)

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup
Simply open `index.html` in your web browser. Ensure the `BACKEND_URL` in `index.html` and `script.js` points to your running backend instance (default: `http://127.0.0.1:8000`).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
