FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=code_judge.settings
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]