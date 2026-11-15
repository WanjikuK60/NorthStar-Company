# Day 1 Webhook Prototype (Northstar Sprint)

My Day 1 deliverable for the Northstar Sprint, a one-week industry simulation: a FastAPI webhook receiver with a small browser page for sending test events. Day 1 was about learning webhooks, a tool I hadn't used before.

## What it does

- `POST /webhook` accepts a JSON event (`event` is required, `message` is optional), logs it, and echoes it back.
- `GET /` serves a chat-style page. Each event you send shows on the right, and the server's reply shows on the left.
- Invalid events (for example, with no `event` name) are rejected with a 422 error, and the page tells you so.

## Run it

```bash
git clone https://github.com/WanjikuK60/NorthStar-Company.git
cd NorthStar-Company
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash; on macOS/Linux use: source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app:app --reload
```

Open http://127.0.0.1:8000, enter an event name and a message, and press **Send**.

Or send an event from the terminal:

```bash
curl -X POST http://127.0.0.1:8000/webhook \
  -H "Content-Type: application/json" \
  -d '{"event": "order.created", "message": "hello"}'
```

## Tests

```bash
pip install -r requirements-dev.txt
python -m pytest -q
```

## Files

```
app.py          FastAPI app: the webhook endpoint and the test page route
index.html      Browser page for sending test events
test_app.py     API tests
JOURNAL.md      What I built, learned and got stuck on during Day 1
```

## What I'd add next

Verify a signature on incoming webhooks so only the real sender is accepted, and store events instead of only logging them. The journal lists the Day 2 plan: polling a warehouse API and caching stock.
