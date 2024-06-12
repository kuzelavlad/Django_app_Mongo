# Use the official Python image as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container
COPY ./DjangoMongo /code/

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
