# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE config.settings

# Install system dependencies
RUN apt-get update \
    && apt-get -y install netcat

# Set up the working directory in the container
WORKDIR /app

# Copy the project files to the container
COPY . /app

# Install project dependencies
RUN pip install --no-cache-dir pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --deploy --ignore-pipfile

# Create .env file from env.example and replace SECRET_KEY
RUN cp env.example .env && \
    SECRET_KEY=$(python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())") && \
    sed -i "s/SECRET_KEY=.*/SECRET_KEY=${SECRET_KEY}/" .env

# Collect static files
RUN python manage.py collectstatic --noinput

# Run database migrations
RUN python manage.py migrate

# Expose the port the application runs on
EXPOSE 8000

# Run the application when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]