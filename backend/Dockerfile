FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /api
COPY ./api/api.py .
COPY ./api/database.py .
COPY ./api/db/file.txt ./db/file.txt


RUN pip install fastapi uvicorn 
RUN useradd --create-home api
RUN chown -R api:api /api
USER api

EXPOSE 8000
CMD ["python","api.py"]