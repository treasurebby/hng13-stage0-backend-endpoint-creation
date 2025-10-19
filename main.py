from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from datetime import datetime, timezone

app = FastAPI()

@app.get("/me")
def get_profile():
    try:
        # Fetch cat fact from external API
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()  # Raises error if status != 200
        cat_fact = response.json().get("fact", "Cats are awesome!")
    except requests.exceptions.RequestException:
        # Fallback if API fails
        cat_fact = "Could not fetch a cat fact at the moment."

    # Create response data
    data = {
        "status": "success",
        "user": {
            "email": "ehiomhentreasureruth@gmail.com",
            "name": "Ehiomhen Treasure",
            "stack": "Python/FastAPI"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return JSONResponse(content=data, media_type="application/json")
