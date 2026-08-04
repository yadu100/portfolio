# Changelog

All notable changes to this portfolio project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.1.0] — Refactoring & Modernization Sprint (2026-08-04)

### Architecture & Deployment
- Migrated database from AWS RDS PostgreSQL to **Neon PostgreSQL (serverless)** via `dj-database-url`.
- Migrated hosting from PythonAnywhere to **Render** with `build.sh` automation and Gunicorn WSGI server.
- Replaced legacy AWS S3 bucket image storage with **Cloudinary** (`django-cloudinary-storage`).
- Configured Django 5.1 `STORAGES` dict for `MediaCloudinaryStorage` (default) and `CompressedManifestStaticFilesStorage` (staticfiles).
- Dropped custom domain `ykbs100.com` in favor of Render's default `*.onrender.com` domain.
- Fixed `.gitignore` to exclude `__pycache__/`, `*.pyc`, `db.sqlite3`, `staticfiles/`, and `.env`.

### Template & Code Quality
- **Eliminated ~970 lines of duplicated template code** by creating `templates/base.html` with `{% block %}` template inheritance and refactoring all 8 page templates.
- Quoted all `{{ }}` attributes (`src="{{ }}"`, `href="{{ }}"`) in templates to prevent XSS and URL breakage.
- Removed duplicated `custom_filters.py` from the Project app (single copy retained in Work app).
- Removed `{% csrf_token %}` from the Articles GET-based search form.
- Cleaned up unnecessary blank lines in `INSTALLED_APPS` and removed unused imports.

### Models & Migrations
- Refactored all image-bearing `CharField` fields to **Django `ImageField`** across 4 apps:
  - **About:** `cover_image_url` → `cover_image`, `certificate_image_url` → `certificate_image`
  - **Work:** `company_image_url` → `company_image`
  - **Project:** `project_homepage_url` → `project_image`
  - **Articles:** `picture1`–`picture5` (CharField → ImageField)
- All new `ImageField`s use `upload_to='portfolio_images/'` targeting Cloudinary.
- Fixed `Articles.date` — removed erroneous `auto_now_add=True` to allow manual date entry.
- All template image references updated from `{{ field }}` to `{{ field.url }}` with `{% if %}` null guards.

### Security
- Moved `SECRET_KEY` from hardcoded value to `os.environ.get()` with dev-only fallback.
- `DEBUG` now reads from environment variable and defaults to `False`.
- Renamed database environment variables from generic names (`NAME`, `USER`) to prefixed names (`DB_NAME`, `DB_USER` → now unified under `DATABASE_URL`).
- Wrapped `send_mail()` in try/except in the contact form view with user-facing error messaging.
- Replaced all `Model.objects.get()` calls with `get_object_or_404()` to prevent unhandled 500 errors on invalid PKs.
- Added `CSRF_TRUSTED_ORIGINS` configuration for Render's domain.
- Created `.env.example` template with all required environment variables documented.

### Performance & UX
- Added **pagination** (5 items per page) to Work, Project, and Articles list views with a reusable `_pagination.html` include template.
- Activated `load_dotenv()` — `.env` file loading now properly functions.

### Documentation
- Replaced 2-line `README.md` with comprehensive documentation covering setup, deployment, architecture, and environment variables.
- Converted `changelog.txt` to structured `CHANGELOG.md`.

---

## [1.0.0] — Initial Build (2024-08-16 to 2024-08-24)

### Added
- **About page** with personal introduction, academics section, and social media links.
- **Certifications section** with cover images and certificate image links fetched from AWS S3.
- **Contact form** with Gmail SMTP backend for sending inquiry emails.
- **Work section** listing all previous professional experiences in reverse chronological order, with alternating left/right layout using a custom `mod` template filter.
- **Individual work detail pages** showing company logo, designation, department, role description, and technologies used.
- **Projects page** with status badges (Completed/On Going) and project area highlights.
- **Individual project detail pages** with homepage screenshot, description, technologies, source code link, and live site link.
- **Articles page** with search functionality across headings, sub-headings, and body text.
- **Individual article pages** with up to 5 sub-sections (heading, image, text) and a conclusion section.
- Custom CSS with Google Fonts (Khand, DM Serif Text, Dancing Script, New Amsterdam, Jersey 10, Sedan) and Bootstrap Icons.
- `custom_filters.py` template tag providing a `mod` (modulus) filter for alternating layout logic.
- Environment variable support via `.env` file with `python-dotenv`.
- PostgreSQL database connection (local + AWS RDS).
- AWS S3 bucket integration for all image and asset storage.
- Responsive Bootstrap 4.6 layout with mobile-first navbar and media queries.
