# Install python BASE IMAGE
FROM python:3.8-slim

WORKDIR /aplikasi_gue

COPY requirements.txt /aplikasi_gue
# Install dependencies/library/requirements
RUN pip install -r requirements.txt

COPY . /aplikasi_gue

EXPOSE 8000

# Comman running aplikasi
CMD [ "uvicorn" ,"main:app", "--host","0.0.0.0"]