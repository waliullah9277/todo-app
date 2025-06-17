# Django To-Do App

A simple, responsive Django To-Do application following the MVT (Model-View-Template) pattern.  
Users can register, log in, manage tasks, edit/delete, and reset passwords.  
Tailwind CSS is used for the modern UI.

---

## Features

- User Registration, Login & Logout
- Password Reset (via email)
- Add, Edit, Delete, and Complete Tasks
- Responsive design with Tailwind CSS
- Only authenticated users can access their tasks
- CSRF protection, session security

---

## Screenshots

<!-- Add your app screenshots here (optional) -->
<!-- ![screenshot1](screenshots/home.png) -->

---

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates, Tailwind CSS
- **Database:** SQLite (default, easy to switch)
- **Deployment-ready:** Render, Railway, Heroku, etc.

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Create virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the project root. Example:

```dotenv
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Email configuration for password reset, etc.
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
EMAIL_USE_TLS=True
```

> **Never commit your real `.env` file with secrets to GitHub!**

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create superuser (admin)

```bash
python manage.py createsuperuser
```

### 6. Collect static files

```bash
python manage.py collectstatic
```

### 7. Start the development server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Deployment

- Make sure `DEBUG=False` and set `ALLOWED_HOSTS` in `settings.py` for production
- Use Gunicorn for production (`web: gunicorn your_project_name.wsgi` in Procfile)
- Set up environment variables and static files on the server (see [Django deployment checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/))
- For free and easy deployment, you can use [Render](https://render.com/), [Railway](https://railway.app/), or [Heroku](https://heroku.com/)

---

## Folder Structure

```
your_project/
│
├── todo_project/           # Django project settings
│   ├── settings.py
│   └── ...
├── tasks/                  # Main app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   └── ...
├── templates/
│   └── tasks/
├── static/
│   └── ...
├── requirements.txt
├── Procfile
├── README.md
└── .env.example
```

---

## Example `.env` file

See `.env.example` in this repo for all supported environment variables.

---

## Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you would like to change.

---

## License

This project is [MIT](LICENSE) licensed.

---

**Developed with ❤️ by [Your Name](https://github.com/yourusername)**
