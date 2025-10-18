Backend Wizards Stage 0 Task

Description
Simple FastAPI app that returns my profile info and a random cat fact.

Endpoint
`GET /me`

Example Response
```json
{
  "status": "success",
  "user": {
    "email": "treasure@example.com",
    "name": "Treasure Roduction",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-18T16:00:00Z",
  "fact": "Cats sleep for 70% of their lives."
}
