
# Event Management API

A Django RESTful API for managing events and attendees.

## Setup

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API Documentation

Visit: http://127.0.0.1:8000/swagger/

## Sample API Requests

- Create Event:
```bash
curl -X POST http://127.0.0.1:8000/api/events/ -H "Content-Type: application/json" -d '{"name":"New Event","location":"Delhi","start_time":"2030-01-01T10:00:00Z","end_time":"2030-01-01T12:00:00Z","max_capacity":5}'
```

- List Events:
```bash
curl http://127.0.0.1:8000/api/events/
```

- Register Attendee:
```bash
curl -X POST http://127.0.0.1:8000/api/events/1/register/ -H "Content-Type: application/json" -d '{"name":"John Doe","email":"john@example.com"}'
```

- List Attendees:
```bash
curl http://127.0.0.1:8000/api/events/1/attendees/
```

## Notes
- Events are listed only if upcoming.
- Registrations prevent duplicate emails and overbooking.
- Uses SQLite by default.
- Timezone is set to IST (Asia/Kolkata).

Enjoy!
    