# Install python BASE IMAGE
FROM python:3.8-slim

COPY . .
# Install dependencies/library/requirements
RUN pip install -r requirements.txt

# Comman running aplikasi
CMD [ "uvicorn" ,"main:app", "--host","0.0.0.0"]