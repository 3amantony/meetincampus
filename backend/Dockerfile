FROM python:3.12-small

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /api
COPY test.py .


RUN pip install fastapi uvicorn 
RUN useradd -create-home api
USER api

EXPOSE 8000
CMD ["python","test.py"]