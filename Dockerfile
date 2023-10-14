# Install OS/Base Image yang udah terinstall python juga
FROM python:3.8-slim

COPY . .

# Install lib/package/dependency
RUN pip install -r requirements.txt

# Run aplikasi
CMD ["uvicorn","main:app","--host"]