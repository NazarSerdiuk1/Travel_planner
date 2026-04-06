# Travel Planner

## Description
A web application built with Django, Django Rest Framework and PostgreSQL to manage travel projects and places. The project is fully containerized using Docker and Docker Compose.

## Features

- Manage travel projects and places
- Admin panel for easy management
- PostgreSQL database for storing data
- Fully Dockerized setup for easy deployment

## Technology Stack
- Python 
- Django
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
## Installation and Setup

### Clone the Repository
```bash
git clone https://github.com/NazarSerdiuk1/Travel_planner.git
cd travel
```

## Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install
```
### Run Docker
```bash
docker-compose up --build
```
The API will be available at `http://localhost:8000/`.
Endpoints will be available at `http://localhost:8000/api/docs/`
