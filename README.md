# Scribeo - Blogging System

A full-featured, role-based blogging platform built with Django. Scribeo supports multi-level user roles (Superuser, Manager, Editor), slug-based URLs, category-organized posts, real-time-style comments, and dedicated dashboards for content and user management.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Role-Based Access Control](#role-based-access-control)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Creating the First Superuser](#creating-the-first-superuser)
- [URL Structure](#url-structure)
- [Screenshots](#screenshots)


---

## Overview

Scribeo is an end-to-end blogging application built to demonstrate real-world patterns like role-based dashboards, granular permissions, and clean, SEO-friendly slug-based routing — instead of relying on primary-key-based URLs. It is composed of two Django apps:

- **blogs** — public-facing blog: home page, categories, individual post pages, search, comments, authentication.
- **dashboards** — private backend for content and user management, restricted to Managers and Editors.

Regular (non-staff) users can browse posts, search, and comment once logged in, but do **not** get a personal dashboard. Only Managers and Editors have access to a management backend.

---

## Features

- Multi-role system: **Superuser / Manager / Editor**
- **Media/image upload** support and configuration for post thumbnails
- **Comment system** — only authenticated users can comment on posts
- **Manager & Editor dashboards** with summary counts and data tables
- **Search feature** with the search term retained in the input box after a query
- **Home page** with featured posts and category listings
- **Category pages** with dedicated layouts and custom error pages

---

## Role-Based Access Control

| Capability | Superuser | Manager | Editor | Regular User |
|---|---|---|---|---|
| Create / edit / delete posts | ✅ | ✅ | ✅ | ❌ |
| Create / edit / delete categories | ✅ | ✅ | ✅ | ❌ |
| Add / edit / delete users & assign roles | ✅ | ✅ | ❌ | ❌ |
| Access management dashboard | ✅ | ✅ | ✅ | ❌ |
| View posts / categories | ✅ | ✅ | ✅ | ✅ |
| Comment on posts | ✅ | ✅ | ✅ | ✅ (if authenticated) |

**Notes:**
- Users cannot self-register as an Editor or Manager. Only a **Superuser** can promote a user to Editor, and only a **Manager/Superuser** can create/manage user accounts and assign roles.
- Editors are scoped to content (posts and categories) only — they have **no access** to user management screens.
- Managers have every Editor permission **plus** full user management (add, edit, delete, view users).

---

## Tech Stack

- **Backend:** Python 3.10+, Django 4.x
- **Database:** SQLite (development) — swappable with PostgreSQL / MySQL for production
- **Frontend:** HTML/CSS, Bootstrap
---

## Project Structure

```
blog_main/
├── blog_main/ # Project-level settings, URLs, WSGI/ASGI config
├── blogs/ # Public-facing app: models, views, posts, categories, comments, auth, search
├── dashboards/ # Manager/Editor backend: CRUD dashboards, permission checks
├── templates/ # Shared and app-level HTML templates
├── screenshots/ # App screenshots used in this README
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- `pip` and `venv` (or `virtualenv`)
- Git (Version Control)

### Installation

```bash
# Clone the repository
git clone https://github.com/themaverick27/scribeo-blog-platform.git
cd blog_main

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate     # On Mac: source venv/bin/activate 

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root  with the following:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Optional — only needed if using PostgreSQL/MySQL instead of SQLite
DATABASE_URL=postgres://user:password@localhost:5432/blog_manager
```

### Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### Running the Project

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

---

## Creating the First Superuser

Since users cannot self-register as Editor or Manager, create the first Superuser manually:

```bash
python manage.py createsuperuser
```

Log in as this Superuser to promote users to Editor/Manager or add new users with roles directly.

---

## URL Structure

Posts and categories use **slug-based URLs** (via `slugify` + uniqueness constraints) instead of primary keys:

```
/post/<post-slug>/
/category/<category-slug>/
```

## Screenshots

### Home
![Home](screenshots/home.png)

### Login
![Login](screenshots/login.png)

### Register
![Register](screenshots/register.png)

### Search
![Search](screenshots/search.png)

---

**Author:** _Aniwesh Kumar_