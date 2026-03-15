# BalkanPress

<img width="1313" height="604" alt="Screenshot 2026-02-22 at 12 54 10" src="https://github.com/user-attachments/assets/5d4c6fa9-6175-44f3-b67a-381a4c16113c" />

BalkanPress is a production-ready news and blogging platform built with Django. It supports articles, categories, tags, comments, search functionality, and a clean, scalable architecture.


---

## Features

- Article management (Create, Edit, Delete)
- Category & Tag management (Full CRUD)
- Category & Tag filtering
- Full text search (title, summary, content, categories, tags)
- Comment system (with moderation support)
- Newsletter subscription
- Pagination
- Reading time calculation
- Bootstrap 5 UI
- DRY & scalable architecture
- Production-grade class-based views
- Reusable form mixins
- Clean template structure
- Optimised querysets (select_related, prefetch_related)

---

## Architecture Overview

```text
BalkanPress/
├── BalkanPress/
│   ├── articles/
│   │   ├── migrations/
│   │   ├── templatetags/
│   │   │   └── article_extras.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── categories/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── comments/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── common/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── helpers.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── validators.py
│   │   └── views.py
│   ├── tags/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── newsletter/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
├── staticfiles/
│   ├── css/
│   │   └── styles.css
│   └── images/
│       ├── favicon.ico
│       └── logo.png
├── templates/
│   ├── articles/
│   │   ├── article-create.html
│   │   ├── article-delete.html
│   │   ├── article-detail.html
│   │   ├── article-edit.html
│   │   ├── article-list.html
│   │   └── _sidebar.html
│   ├── categories/
│   │   ├── category-create.html
│   │   ├── category-delete.html
│   │   ├── category-edit.html
│   │   └── category-list.html
│   ├── tags/
│   │   ├── tag-create.html
│   │   ├── tag-delete.html
│   │   ├── tag-edit.html
│   │   └── tag-list.html
│   ├── common/
│   │   ├── errors/
│   │   │   └── 404.html
│   │   └── partials/
│   │       ├── _clock.html
│   │       ├── _weather.html
│   │       ├── footer.html
│   │       └── nav.html
│   ├── about.html
│   └── base.html
├── .env.example
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

---

## Search System

Search is implemented using:

- 'ArticleSearchForm'
- 'ArticleSearchView'
- Query filtering with Django 'Q' objects
- Case-insensitive matching

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
- HTML/CSS
- JavaScript (minimal)

---

## Installation

### Prerequisites
- Python 3.13 or higher
- PostgreSQL
- Git

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rachoni/balkanpress.git
   cd balkanpress
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate # macOS / Linux
   venv\\Scripts\\activate # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   ```bash
   createdb balkan_press_db
   ```
   Or using `psql`:
   ```sql
   CREATE DATABASE balkan_press_db;
   ```

5. **Environment Variables**
   Create `.env` from the existing `.env.example` file:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and set your real local values (especially `SECRET_KEY` and `DB_PASSWORD`).

6. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

9. **Run server**
   ```bash
   python manage.py runserver
   ```

10. **Access the application**
    - Main site: http://127.0.0.1:8000/ or http://localhost:8000/
    - Admin panel: http://127.0.0.1:8000/admin/ or http://localhost:8000/admin/

---

## Environment Variables

| Variable             | Description         | Default           |
|----------------------|---------------------|-------------------|
| `SECRET_KEY`         | Django secret key   | Required          |
| `DEBUG`              | Debug mode          | `True`            |
| `DB_NAME`            | Database name       | `balkan_press_db` |
| `DB_USER`            | Database user       | `postgres`        |
| `DB_PASSWORD`        | Database password   | Required          |
| `DB_HOST`            | Database host       | `127.0.0.1`       |
| `DB_PORT`            | Database port       | `5432`            |
| `ALLOWED_LOCAL_HOST` | Allowed local host  | `localhost`       |

---

## Existing .env.example

This project already includes an `.env.example` file. Keep only safe placeholder values there:

```env
SECRET_KEY=change-me
DB_NAME=balkan_press_db
DB_USER=postgres
DB_PASSWORD=change-me
DB_HOST=127.0.0.1
DB_PORT=5432
ALLOWED_LOCAL_HOST=localhost
```

---

## Design Principles

- **DRY (Don't Repeat Yourself)** - Reusable mixins and base classes
- **Separation of Concerns** - Clear app boundaries
- **Reusable mixins** - Common functionality extracted
- **Clean class-based views** - Organized view logic
- **Scalable URL structure** - Namespaced URL patterns
- **Template partials** - Reusable template components
- **Bootstrap form integration** - Consistent form styling
- **Production-oriented structure** - Ready for deployment

---

## Security Considerations

### ✅ Implemented:
- **CSRF Protection**: Enabled on all forms with '{% csrf_token %}'
- **SQL Injection Prevention**: Django ORM with parameterized queries
- **XSS Protection**: Automatic template escaping
- **Environment Variables**: Sensitive data stored in .env file
- **Form Validation**: Server-side validation with custom clean methods

### ⚠️ Partially Implemented / Configuration Required:
- **Client-side Validation**: HTML5 attributes added to form fields
- **Production Settings**: Set DEBUG=False in .env for production deployment

### Best Practices Followed:
- Secret key never committed to repository
- Database credentials in environment variables
- No sensitive data in source code

---

## Guidelines

### Contributing Guidelines
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## Known issues

- Image upload path in Article model needs optimization
- Search with special characters may need escaping
- Mobile responsiveness needs improvement on some pages
- Comment moderation lacks email notifications

---

## Future Improvements

- Add RSS feeds for articles
- Implement related articles suggestions
- Add social media sharing buttons
- Create article view count tracking
- Implement article bookmarking/saving
- Add multi-language support
- Create API endpoints with Django REST Framework
- Implement caching for frequently accessed data
- Add unit tests for all views and forms
- Deploy to production (AWS/Heroku)

---

## License

MIT License

---

## Contact

Radoslav Raychev - [GitHub](https://github.com/rachoni)
Project Link: https://github.com/rachoni/balkanpress
