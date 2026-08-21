from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests, time, threading

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cache dictionary
cache = {}

# ✅ Mock warehouse API for testing
WAREHOUSE_URL = "https://jsonplaceholder.typicode.com/todos/1"

# Background polling function
def poll_warehouse():
    while True:
        try:
            resp = requests.get(WAREHOUSE_URL)
            if resp.status_code == 200:
                cache["stock"] = resp.json()
                print("Cache updated:", cache["stock"])
        except Exception as e:
            print("Polling error:", e)
        time.sleep(300)  # poll every 5 minutes

# Start polling thread
threading.Thread(target=poll_warehouse, daemon=True).start()

# Day 1 webhook endpoint
@app.post("/webhook")
async def webhook_listener(request: Request):
    data = await request.json()
    print("Webhook received:", data)
    return {"status": "ok", "received": data}

# ✅ Day 3 stock endpoint
@app.get("/stock")
def get_stock():
    return {"cached_stock": cache.get("stock", "No data yet")}
