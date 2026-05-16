# Zaptek Internship Applications API

This is a complete FastAPI backend project that uses mock/sample data instead of a real database.
It manages internship applications and supports CRUD operations.

## What the project does

The API allows a user to:

- Get all internship applications
- Get one application by ID
- Create a new application
- Update an existing application
- Delete an application
- Filter applications by status, track, or university

## Project structure

```text
zaptek_api_project/
  app/
    main.py       # API routes and CRUD logic
    schemas.py    # Pydantic validation models
    data.py       # Mock data list acting like a database
  requirements.txt
  README.md
```

## How to run the project

1. Install the requirements:

```bash
pip install -r requirements.txt
```

2. Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

3. Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## Main endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | / | Welcome route |
| GET | /applications | Get all applications |
| GET | /applications/{id} | Get one application |
| POST | /applications | Create new application |
| PUT | /applications/{id} | Update application |
| DELETE | /applications/{id} | Delete application |

## Example POST body

```json
{
  "fullName": "Eugene Duah",
  "email": "eugene@example.com",
  "phone": "0240000000",
  "whatsappNumber": "0240000000",
  "university": "KNUST",
  "course": "Computer Engineering",
  "level": "2nd Year",
  "track": "Backend Engineering",
  "motivation": "I want to improve my backend API development skills through practical projects.",
  "portfolioLink": "https://github.com/eugeneduah",
  "resumeLink": "https://linkedin.com/in/eugeneduah",
  "joinInnovationClub": true,
  "status": "pending"
}
```

## Deployment idea for Render

Use these settings on Render:

- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
