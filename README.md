
# Placement Prediction

This project provides career guidance to fresh graduates and individuals aiming to upgrade their skills, helping them fit into the real job world. By leveraging a Random Forest model for placement prediction, the platform enables users to assess their readiness for various roles and identify areas for improvement.
## Features

- Predicts placement chances based on user input.
- Provides insights and skill recommendations for employability.
- Admin dashboard to manage users and analyze prediction statistics.
- Intuitive and user-friendly interface for end-users.

## Tech Stack

**Backend:** Python, Django

**Frontend:** HTML, CSS, Bootstrap

**Database:** MySql

**ML Model:** Random Forest
## Installation

Clone repository

```bash
  git clone https://github.com/placement-prediction.git

  cd my-project
```

Setup Environment

```
  python -m venv env

  source env\Scripts\activate
```

Migrate Database

```
  python manage.py makemigrations
  
  python manage.py migrate
```

Run the server

```
  python manage.py runserver

```
Access the Application

Open your browser and navigate to http://127.0.0.1:8000/.