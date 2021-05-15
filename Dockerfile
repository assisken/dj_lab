FROM python:3.9

EXPOSE 8000
WORKDIR /app
COPY requirements.txt requirements.txt
RUN ["pip", "install", "-r", "requirements.txt"]
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
