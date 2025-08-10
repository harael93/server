# Tarot API Server

This is the backend API server for the Tarot application built with Django and Django REST Framework.

## Setup

1. **Virtual Environment**: A Python virtual environment is already set up in the `venv/` directory.

2. **Dependencies**: Django and Django REST Framework are installed. See `requirements.txt` for full list.

## Running the Server

1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Run the Django development server:
   ```bash
   python manage.py runserver 8000
   ```

The server will start on http://localhost:8000

## API Endpoints

- **Health Check**: `GET /api/health/`
  - Returns a simple health check response

- **Tarot Reading**: `GET /api/reading/`
  - Returns a sample tarot card reading (placeholder implementation)

## Project Structure

- `tarot_api/` - Main Django project configuration
- `api/` - Django app containing API endpoints
- `venv/` - Python virtual environment
- `manage.py` - Django management script
- `requirements.txt` - Python dependencies

## Development

To add new API endpoints:

1. Add views to `api/views.py`
2. Add URL patterns to `api/urls.py`
3. Update this README with new endpoint documentation

## Database

The project uses SQLite by default for development. Database file: `db.sqlite3`

Run migrations when needed:
```bash
python manage.py migrate
```
