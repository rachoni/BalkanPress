# BalkanPress

BalkanPress is a production ready news and blogging platfor built with Django. It supports articles, categories, tags, comments, search functionality and a clean scalable architecture.

---

## Features

- Article management (Create, Edit, Delete)
- Category & Tag filtering
- Full text search (title, summary, content, categories, tags)
- Comment system (with moderation support)
- Pagination
- Reaing time calculation
- Bootstrap 5 UI
- DRY & scalable architecture
- Production-grade class-based views
- Reusable form mixins
- Clean template structure
- Optimised querysets (select_related, prefetch_related)

---

## Architecture Overview

BalkanPress/
|-- articles/
|-- |-- migrations/
|-- |-- templatetags/
|-- |-- |-- article_extras.py
|-- |-- admin.py
|-- |-- apps.py
|-- |-- forms.py
|-- |-- models.py
|-- |-- tests.py
|-- |-- urls.py
|-- |-- views.py
|-- categories/
|-- |-- migrations/
|-- |-- admin.py
|-- |-- apps.py
|-- |-- forms.py
|-- |-- models.py
|-- |-- tests.py
|-- |-- urls.py
|-- |-- views.py
|-- comments/
|-- |-- migrations/
|-- |-- admin.py
|-- |-- apps.py
|-- |-- forms.py
|-- |-- models.py
|-- |-- tests.py
|-- |-- urls.py
|-- |-- views.py
|-- common/
|-- |-- migrations/
|-- |-- admin.py
|-- |-- apps.py
|-- |-- forms.py
|-- |-- models.py
|-- |-- tests.py
|-- |-- urls.py
|-- |-- views.py
|-- tags/
|-- |-- migrations/
|-- |-- admin.py
|-- |-- apps.py
|-- |-- forms.py
|-- |-- models.py
|-- |-- tests.py
|-- |-- urls.py
|-- |-- views.py
|-- asgi.py
|-- settings.py
|-- urls.py
|-- wsgi.py
media/
staticfiles/
|-- css/
|-- |-- styles.css
|-- images/
|-- |-- favicon.ico
|-- |-- logo.png
templates/
|-- articles/
|-- |-- article-create.html
|-- |-- article-delete.html
|-- |-- article-detail.html
|-- |-- article-edit.html
|-- |-- article-list.html
|-- categories/
|-- |-- category-create.html
|-- |-- category-delete.html
|-- |-- category-edit.html
|-- |-- category-list.html
|-- common/
|-- |-- errors/
|-- |-- |-- 404.html
|-- |-- partials/
|-- |-- |-- footer.html
|-- |-- |-- nav.html
|-- about.html
|-- base.html
.gitignore
manage.py
README.md
requirements.txt

---

## Search System

Search is implemented using:

- 'ArticleSearchForm'
- 'ArticleSearchView'
- Query filtering with Django 'Q' objects
- Case-insesitive matching

Search covers:

- Title
- Summary
- Content
- Category names
- Tag names

---

## Tech Stack

- Python 3.13
- Django 6.0.2
- Bootstrap 5
- PostgreSQL

---

## Installation

### Clone the repository

git clone http://github.com/rachoni/balkanpress.git
cd balkanpress

### Create virtual environment

python -m venv venv
source venv/bin/activate # macOS / Linux
venv\Scripts\activate # Windows

### Install dependencies

pip install -r requirements.txt

### Apply migrations

python manage.py migrate

### Create superuser

python manage.py createsuperuser

### Run server

python manage.py runserver

---

## Design Principles

- DRY (Don't Repeat Yourself)
- Separation of Concerns
- Reusable mixins
- Clean class-based views
- Scalable URL structure
- Template partials
- Bootstrap form integration
- Production-oriented structure

---

## Security Considerations

- CSRF protection enabled
- Form validation layer
- Login-required admin operations

---

## Environment Variables

This project uses environment variables stored in a .env file.
Create a .env file in the project root directory and add the following:

SECRET_KEY=django-insecure-4tpxsd8sv7vdfl92fsvkfah%=(f@dg-j&md51sjpe)9h87rrz$
DB_NAME=balkan_press_db
DB_USER=postgres
DB_PASSWORD=admin123
DB_HOST=127.0.0.1
DB_PORT=5432

ALLOWED=127.0.0.1,localhost

---

## License

This project is open-source and available under the MIT License.