FROM python:3.11-slim

WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip


COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]