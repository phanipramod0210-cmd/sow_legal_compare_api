# SOW Legal Compare API

This is a FastAPI backend prototype for analyzing SOW/contract clauses using AI + legal rules.

## Features
- `/api/analyze` endpoint accepts contract text and jurisdictions.
- Splits into clauses, checks for vague language, suggests tighter rewrites.
- Uses a sample legal rules dataset (India, UK, US).
- Placeholder logic included; integrate with OpenAI or other LLMs for production.

## Run locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then visit: http://127.0.0.1:8000/docs

## Deploy
- Can be deployed to GitHub + Render/Heroku/Cloud Run.
