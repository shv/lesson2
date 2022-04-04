FROM python:3.8-alpine
COPY ./ /app
RUN apk update && pip install -r /app/requirements.txt --no-cache-dir
CMD python /app/src/app.py