# Little Lemon Restaurant API

This is a Django REST API for the fictional **Little Lemon Restaurant**, built to manage menu items, table bookings, and user authentication. It uses Django REST Framework (DRF), MySQL for persistent storage, and Docker for optional containerization.

---

## Features

- Menu management (CRUD)
- Booking management (CRUD)
- User registration and authentication (Token & Session)
- Admin interface
- Docker support
- MySQL database integration
- REST API endpoints with DRF

---

## Project Structure

```
django_littlelemon/
│
├── .env                   # Environment variables
├── Dockerfile             # Docker build instructions
├── requirements.txt
├── littlelemon/           # Django project
│   ├── manage.py
│   ├── littlelemon/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── restaurant/        # App: menu and booking logic
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│   └── templates/
│       └── index.html
└── ...
```
---

## Requirements

- Python 3.13+
- MySQL
- Docker (optional, for containerized deployment)

📌 For WSL Users: Before installing dependencies, run:
```
sudo apt-get update
sudo apt-get install default-libmysqlclient-dev build-essential pkg-config
```
If you encounter any compile issues with mysqlclient during installation, you can also run this(For Ubuntu/Debian Users)

---

## MySQL Setup on Linux(Ubuntu)

1. **Update your package list:**
   ```sh
   sudo apt update
   ```
2. **Install MySQL server:**
   ```sh
   sudo apt install mysql-server
   ```
3. **Start the MySQL service:**
   ```sh
   sudo service mysql start
   ```
4. **Log in to MySQL and create your database and user:**
   ```sh
   sudo mysql -u root -p
   ```
   Then in the MySQL shell:
   ```sql
   CREATE DATABASE your_database;
   CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON your_database.* TO 'your_username'@'localhost';
   FLUSH PRIVILEGES;
   EXIT;
   ```

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd django_littlelemon
   ```

2. **Create and configure your `.env` file in the project root, an example file is in the repo**

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   cd littlelemon
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## Running with Docker

1. **Build the Docker image:**
   ```sh
   docker build -t littlelemon .
   ```

2. **Run the container:**
   ```sh
   docker run --env-file .env -p 8000:8000 littlelemon
   ```

---

## Running Tests

```sh
cd littlelemon
python manage.py test
```

---

## API Endpoints

- `/admin/` – Django admin
- `/` and `/menu/` – Menu endpoints (see `restaurant.urls`)
- `/booking/tables/` – Booking management (via DRF ViewSet)
- `/auth/` – User registration and authentication (Djoser)
- `/auth/token/login/` – Obtain auth token (Djoser)


---

