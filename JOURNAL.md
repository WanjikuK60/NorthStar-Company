# Day 1 Journal

**Tool:** Webhooks (new to me)

## What I built

- **Backend:** FastAPI `POST /webhook` endpoint, built and tested
- **Frontend:** simple HTML and JavaScript form that uses `fetch()` to send JSON and show the reply
- **Result:** end-to-end integration confirmed (demo → hello webhook → JSON response)

## What I learned

- FastAPI basics: routes and JSON parsing
- Running the server with `python -m uvicorn app:app --reload`
- Testing with `curl` and a browser frontend
- Adding CORS middleware to fix browser errors

## Blockers and fixes

- `uvicorn` not found in Git Bash → solved with `python -m uvicorn`
- File structure confusion → fixed with a clear folder setup (`app.py`, `index.html`, journal)

## Insight

Webhooks are just HTTP POST callbacks. Once that clicked, they were straightforward.

## Next

Poll the warehouse API every 5 minutes, cache stock, expose a `/stock` endpoint, and extend the frontend to show the cached data.
