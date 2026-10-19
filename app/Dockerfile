# File purpose: Builds an Alpine-based lightweight Python container running as a non-root user.
# Build command: docker build -t notice-board:02230128-1.0.0 .
FROM python:3.11-alpine

# Create a non-root user for security compliance
RUN adduser -D nonroot
USER nonroot

WORKDIR /app
COPY app.py /app/

EXPOSE 8080
CMD ["python", "app.py"]