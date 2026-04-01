from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from backend.nlp import parse_user_input
from backend.ec2_creator import create_ec2

app = FastAPI()

# ✅ CORS (for frontend requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request model
class Command(BaseModel):
    text: str

# ✅ Serve frontend (ONLY index.html, not whole folder)
@app.get("/")
def serve_ui():
    return FileResponse("frontend/index.html")

# ✅ API endpoint
@app.post("/create")
def create(command: Command):
    config = parse_user_input(command.text)
    instance_id = create_ec2(config)

    return {
        "status": "success",
        "instance_id": instance_id,
        "config": config
    }