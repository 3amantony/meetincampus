FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ENV DATABASE_URL=sqlite:////api/db/database.db
WORKDIR /api
COPY ./api/app/ ./app/

RUN mkdir -p /api/db

RUN pip install fastapi uvicorn sqlalchemy pydantic
RUN useradd --create-home api
RUN chown -R api:api /api
USER api

EXPOSE 8000
CMD ["python","/api/app/api.py"]