# ============================================================
# Maintainer: Nazish Khalid
# Version: 1.0.0
# Description: Optimized Flask app for Sakila DVD Rental
# ============================================================

# Use slim image to reduce size
FROM python:3.9-slim

# Add labels for documentation
LABEL maintainer="Nazish Khalid" \
      version="1.0.0" \
      description="Sakila Flask Web Application"

# Set working directory
WORKDIR /app

# Copy ONLY requirements first (better layer caching)
COPY requirements.txt .

# Install all dependencies in ONE layer with no cache
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application code
COPY . .

# Create a non-root user for security
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Only expose the necessary port
EXPOSE 5000

# Health check to verify app is running
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000')" || exit 1

# Run the application
CMD ["python", "app.py"]