# Job Application Tracker — Backend

FastAPI backend for the Week 1 milestone: CRUD API over a Postgres/SQLite database.

## Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000/docs — this is FastAPI's auto-generated Swagger UI.
Use it to create, list, update, and delete applications without a frontend yet.

## Database

Defaults to a local SQLite file (`job_tracker.db`) so you can start immediately with
zero setup. To use Postgres instead:

1. Create a local Postgres database (e.g. `createdb job_tracker`)
2. Copy `.env.example` to `.env` and set `DATABASE_URL` to your Postgres connection string
3. Restart the server — tables are created automatically on startup

## Endpoints

- `GET /applications` — list all (supports `?status=` and `?sort_by=&order=`)
- `POST /applications` — create one
- `GET /applications/{id}` — get one
- `PUT /applications/{id}` — update one (partial updates allowed)
- `DELETE /applications/{id}` — delete one

## Next steps (Week 2+)

- Build a static HTML page that fetches from `/applications`
- Add filtering/sorting UI
- Eventually rebuild the frontend in React
