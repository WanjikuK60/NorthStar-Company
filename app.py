"""Day 1 webhook prototype: a FastAPI endpoint that receives JSON events.

Run:  python -m uvicorn app:app --reload
Then open http://127.0.0.1:8000 to send test events from the browser.

Live: the same app runs on Render's free plan (see render.yaml). The GitHub
Pages copy of index.html sends its events there, so that origin is allowed
through CORS.
"""

import logging
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("webhook")

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Day 1 Webhook Prototype")

# Only the GitHub Pages copy of the test page needs cross-origin access.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://wanjikuk60.github.io"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


class WebhookEvent(BaseModel):
    event: str = Field(min_length=1, max_length=100)
    message: str = Field(default="", max_length=1000)


@app.get("/")
def index() -> FileResponse:
    """Serve the test page from the same origin, so no CORS setup is needed."""
    return FileResponse(BASE_DIR / "index.html")


@app.post("/webhook")
def receive_webhook(payload: WebhookEvent) -> dict:
    logger.info("Webhook received: %s", payload.model_dump())
    return {"status": "ok", "received": payload.model_dump()}
