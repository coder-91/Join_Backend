# Join Backend
This project provides the backend service for the Join application. It utilizes the Django REST Framework and offers an API for managing and delivering users, tasks, and subtasks for the Join frontend application.

## Table of Contents
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [Usage Instructions](#usage-instructions)
  - [API Documentation](#api-documentation)
  - [API Endpoints](#api-endpoints)
  - [Tests](#tests)



## Installation
### Prerequisites
- Python 3.10.1+
- Django 5.0.4+
- Pip (Python package manage)
- Virtualenv (recommended)

### Installation Steps
1. Clone the repository:
```
git clone https://github.com/coder-91/Join_Backend.git
cd Join_Backend
```

2. Create and activate a virtual environment:
```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Perform database migrations:
```
python manage.py migrate
```

5. Create a Django superuser (password min length is 6)
```
python manage.py createsuperuser
```

6. Start the development server:
```
python manage.py runserver
```

7. Login to Admin Panel:  
Log in to the Admin Panel using your __email__ and password.



The API should now be accessible at http://127.0.0.1:8000/.


## Usage Instructions

### API Documentation
The API documentation can be accessed at http://127.0.0.1:8000/api/docs/ after starting the development server.

### API Endpoints
The main API endpoints are:
- `GET /api/users/`: List all users
- `POST /api/users/register`: Create a new user
- `POST /api/users/token`: Create a user token
- `GET /api/users/me`: Display own user profile

Further endpoints and their documentation can be found at http://127.0.0.1:8000/api/docs/.

### Tests
To run the test suite, use the following command:
```
python manage.py test
```
