# yd — Portfolio

A personal portfolio website built with **Django 5.1** and **Bootstrap 4.6**, showcasing my professional experience, personal projects, certifications, and technical articles. Deployed on **Render** with a serverless **Neon PostgreSQL** database and **Cloudinary** for media storage.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 5.1, Python 3.12 |
| Database | Neon PostgreSQL (serverless) |
| Media Storage | Cloudinary |
| Static Files | Whitenoise (CompressedManifestStaticFilesStorage) |
| Frontend | Bootstrap 4.6, jQuery, Google Fonts, Bootstrap Icons |
| Deployment | Render (`build.sh` + Gunicorn) |
| Email | Gmail SMTP (contact form) |

## Project Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── build.sh                   # Render build script
├── .env.example               # Environment variable template
│
├── portfolio/                 # Project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── About/                     # Home page, certifications, contact form
├── Work/                      # Professional experience (Experiences model)
├── Project/                   # Personal projects (Projects model)
├── Articles/                  # Technical articles with search
│
├── templates/
│   ├── base.html              # Shared layout (nav, footer, CSS/JS)
│   └── _pagination.html       # Reusable pagination controls
│
├── static/
│   └── styles/
│       └── style.css
│
└── staticfiles/               # Collected static (gitignored)
```

## Apps & URL Routing

| URL Path | App | Description |
|----------|-----|-------------|
| `/` | About | Home page, intro, certifications, social links |
| `/contact/` | About | Contact form (emails via Gmail SMTP) |
| `/Work/` | Work | Career timeline, alternating layout by entry number |
| `/Work/<pk>/` | Work | Single experience detail with technologies |
| `/Project/` | Project | Personal projects with status badges |
| `/Project/<pk>/` | Project | Single project detail with source/demo links |
| `/Articles/` | Articles | Searchable article list with pagination |
| `/Articles/<pk>/` | Articles | Full article with up to 5 sub-sections |
| `/admin/` | Django | Admin panel for content management |

## Local Development Setup

### Prerequisites

- Python 3.12+
- PostgreSQL (local or remote instance)
- Git

### Steps

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd portfolio
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate     # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and fill in your values (see table below).

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` in your browser.

## Deployment

The project deploys via **Render** using the `build.sh` script:

```bash
#!/usr/bin/env bash
set -o errexit
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

**Render configuration:**
- Build Command: `bash build.sh`
- Start Command: `gunicorn portfolio.wsgi:application`
- Python Version: `3.12.1` (from `runtime.txt`)

## Environment Variables

Create a `.env` file in the project root with the following variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `SECRET_KEY` | Yes | Django secret key. Generate with `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | Yes | Set to `False` in production |
| `DATABASE_URL` | Yes | Neon PostgreSQL connection string. Format: `postgresql://user:pass@host:5432/dbname` |
| `CLOUDINARY_CLOUD_NAME` | Yes | Cloudinary cloud name |
| `CLOUDINARY_API_KEY` | Yes | Cloudinary API key |
| `CLOUDINARY_API_SECRET` | Yes | Cloudinary API secret |
| `EMAIL_HOST_USER` | No | Gmail address for sending contact form emails |
| `EMAIL_HOST_PASSWORD` | No | Gmail app password (not your regular password) |
| `EMAIL_TO_USER` | No | Email address that receives contact form submissions |

A template file (`.env.example`) is provided with placeholder values.

## Features

- **Responsive design** — Bootstrap 4.6 grid with mobile-friendly navbar and media queries
- **Template inheritance** — Single `base.html` with `{% block %}` overrides eliminates duplication
- **Pagination** — List views paginated at 5 items per page with windowed page range
- **Search** — Full-text search across article headings, sub-headings, and body text
- **Contact form** — POST-based form with CSRF protection and Gmail SMTP backend
- **Cloudinary media** — All uploaded images stored and served via Cloudinary CDN
- **Resource-level 404s** — `get_object_or_404` on all detail views for clean error handling
- **Environment-based config** — All secrets and service URLs read from environment variables

## Admin Panel

Content is managed through Django's built-in admin at `/admin/`. The following models are registered:

- **Certifications** — Upload certificate cover images and PDF/image files
- **Experiences** — Manage work history with company logos
- **Projects** — Add project entries with homepage screenshots
- **Articles** — Write technical articles with up to 5 sections and images

## License

This project is a personal portfolio. All rights reserved.
