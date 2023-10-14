# Install OS/Base Image yang udah terinstall python juga
FROM python:3.8-slim

WORKDIR /aplikasi_gue

COPY requirements.txt /aplikasi_gue

# Install lib/package/dependency
RUN pip install -r requirements.txt

COPY . /aplikasi_gue

EXPOSE 8000

# Run aplikasi
CMD ["uvicorn","main:app","--host","0.0.0.0"]