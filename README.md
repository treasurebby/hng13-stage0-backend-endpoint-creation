# HNG13 Stage 0 - Backend Endpoint Creation

A FastAPI backend endpoint that returns user profile information along with an interesting cat fact.

## Description

This project is a simple REST API built with FastAPI that exposes a `/me` endpoint. The endpoint returns:
- User profile information (email, name, tech stack)
- Current timestamp in UTC
- A random cat fact from an external API

## Features

- ✅ RESTful API endpoint at `/me`
- ✅ Returns JSON response with user data
- ✅ Integrates with external Cat Facts API
- ✅ Error handling with fallback messages
- ✅ UTC timestamp for each request

## Tech Stack

- **Python** - Programming language
- **FastAPI** - Modern web framework for building APIs
- **Requests** - HTTP library for API calls

## Installation

1. Clone the repository:
```bash
git clone https://github.com/treasurebby/hng13-stage0-backend-endpoint-creation.git
cd hng13-stage0-backend-endpoint-creation
```

2. Install dependencies:
```bash
pip install fastapi uvicorn requests
```

## Usage

1. Run the application:
```bash
uvicorn main:app --reload
```

2. Access the endpoint:
   - API endpoint: `http://127.0.0.1:8000/me`
   - API documentation: `http://127.0.0.1:8000/docs`

## API Response Example

```json
{
  "status": "success",
  "user": {
    "email": "your_email@example.com",
    "name": "Your Full Name",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-18T12:00:00.000000+00:00",
  "fact": "A cat's brain is biologically more similar to a human brain than it is to a dog's."
}
```

## Project Structure

```
backend-stage0/
├── main.py          # Main FastAPI application
└── README.md        # Project documentation
```

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Requests

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available for educational purposes.

## Learn More

Interested in learning more about backend development? Check out [HNG Internship](https://hng.tech/hire) for opportunities to work with talented developers.

---

**Hire Python Developers:** [https://hng.tech/hire](https://hng.tech/hire)
