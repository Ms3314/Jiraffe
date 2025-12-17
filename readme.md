# Jiraffe 🦒

An API to generate intuitve choice based stories using AI

## Overview

Jiraffe is a FastAPI-based backend application that provides story generation capabilities. The application uses OpenAI's API to create engaging stories where the user can choose a descition through which the story changes.

## Features

- 📖 AI-powered story generation
- 🔄 Job management system
- 🗃️ SQLite database storage
- 🌐 CORS-enabled API
- 📝 Interactive API documentation

## Tech Stack

- **Backend Framework**: FastAPI
- **Database**: SQLite with SQLAlchemy
- **AI Integration**: LangChain + OpenAI
- **Package Management**: UV
- **Language**: Python 3.13+

## Project Structure

```
Jiraffe/
├── src/backend/
│   ├── core/           # Core application configuration and logic
│   ├── db/             # Database configuration
│   ├── models/         # SQLAlchemy models
│   ├── routers/        # API route handlers
│   ├── schema/         # Pydantic schemas
│   └── main.py         # FastAPI application entry point
├── .env                # Environment variables
└── README.md           # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.13+
- UV package manager
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Jiraffe
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Configure your `.env` file:
```properties
DATABASE_URL=sqlite:///./database.db
API_PREFIX=/api
DEBUG=True
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
OPENAI_API_KEY=your_openai_api_key_here
```

4. Navigate to the backend directory and install dependencies:
```bash
cd src/backend
uv install
```

### Running the Application

From the backend directory:
```bash
uv run main.py
```

Or from the project root:
```bash
uv run src/backend/main.py
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/doc
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Stories
- `GET /api/stories` - List all stories
- `POST /api/stories` - Create a new story
- `GET /api/stories/{id}` - Get a specific story
- `PUT /api/stories/{id}` - Update a story
- `DELETE /api/stories/{id}` - Delete a story

### Jobs
- `GET /api/jobs` - List all jobs
- `POST /api/jobs` - Create a new job
- `GET /api/jobs/{id}` - Get job status

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `sqlite:///./database.db` |
| `API_PREFIX` | API route prefix | `/api` |
| `DEBUG` | Enable debug mode | `True` |
| `ALLOWED_ORIGINS` | CORS allowed origins | `http://localhost:3000,http://localhost:5173` |
| `OPENAI_API_KEY` | OpenAI API key for story generation | Required |

## Development

### Running in Development Mode

The application runs with auto-reload enabled when `DEBUG=True` in your environment.

### Database

The application uses SQLite by default. The database file will be created automatically when you first run the application.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions, please open an issue on the GitHub repository.