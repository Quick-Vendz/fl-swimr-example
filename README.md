# Swimming School Website

A modern swimming school website built with Django, HTMX, Alpine.js, and Tailwind CSS.

## Features

- 🏊‍♂️ Class scheduling and booking system
- 👥 Multi-level swimming programs (Kids, Beginner, Intermediate, Advanced)
- 📅 Interactive weekly schedule with availability
- 👨‍💼 Admin portal for instructors and classes
- 📱 Responsive design with modern UI
- ⚡ Dynamic interactions with HTMX and Alpine.js

## Tech Stack

- **Backend**: Django 5.2
- **Frontend**: HTML, Tailwind CSS, Alpine.js, HTMX
- **Database**: SQLite (for demo)
- **Icons**: Font Awesome

## Local Development

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Run server: `python manage.py runserver`

## Deployment

### Railway (Recommended for Free Hosting)

1. Push code to GitHub
2. Connect to [Railway.app](https://railway.app)
3. Add environment variables:
   - `SECRET_KEY`: Generate a secure key
   - `ALLOWED_HOSTS`: Your Railway domain
   - `DEBUG`: False
4. Deploy automatically

### Render

1. Push code to GitHub
2. Connect to [render.com](https://render.com)
3. Create Web Service
4. Set build command: `pip install -r requirements.txt && python manage.py migrate`
5. Set start command: `python manage.py runserver 0.0.0.0:10000`
6. Add environment variables as above

### Environment Variables

For production, set these environment variables:

```
SECRET_KEY=your-secure-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DEBUG=False
```

## Demo Data

The application includes sample data for:
- Swimming classes (Kids, Beginner, Intermediate, Advanced)
- Weekly schedules with availability
- Instructor information
- Pricing packages

## Project Structure

```
├── _CORE/                 # Django settings
├── a_FRONT/              # Frontend app (public pages)
├── a_ACCOUNTS/           # User accounts
├── a_DASH/               # Admin dashboard
├── templates/            # HTML templates
├── static/               # Static files (CSS, JS, images)
└── manage.py            # Django management script
```

## License

This project is for educational purposes.