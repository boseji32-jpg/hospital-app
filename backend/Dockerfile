FROM python:3.11-slim

WORKDIR /app

# Install everything in one layer – no fancy multi-stage
RUN pip install --no-cache-dir \
    fastapi uvicorn[standard] sqlmodel python-multipart passlib[bcrypt] python-jose[cryptography] pydantic

# Copy code
COPY . .

EXPOSE 8000

# Use the absolute path that ALWAYS exists in python-slim
CMD ["/usr/local/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
