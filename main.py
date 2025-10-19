from fastapi import FastAPI
import requests
from datetime import datetime
import os

app = FastAPI()

@app.get("/me")
def get_profile():
    try:
        # Fetch cat fact
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        fact = response.json().get("fact", "Cats are amazing creatures!")
    except Exception:
        fact = "Could not fetch cat fact right now."

    # Return JSON response
    return {
        "status": "success",
        "user": {
            "email": "ehiomhentreasureruth@gmail.com",
            "name": "Ehiomhen Treasure",
            "stack": "Python/FastAPI"
        },
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "fact": fact
    }

# 👇 THIS PART IS IMPORTANT FOR RAILWAY
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
