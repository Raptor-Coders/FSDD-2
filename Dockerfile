FROM heroku/heroku:22
RUN apt-get update && apt-get install -y curl build-essential python-pip gcc python3-dev musl-dev python3-venv libpq-dev

RUN python3 -m venv /opt/venv
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install psycopg2-binary

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN adduser django
USER django