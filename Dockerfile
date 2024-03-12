FROM python:3.10.2-alpine

WORKDIR /usr/src/app
COPY requirements.txt .
RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r requirements.txt
COPY . .
EXPOSE 3005
CMD ["gunicorn", "src.auditoria.api:app", "--bind", "0.0.0.0:3005"]
