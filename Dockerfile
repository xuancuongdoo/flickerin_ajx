# Use the official Python image as the base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the project files to the container
COPY . .

# Set execute permission on the entrypoint script
RUN chmod +x /app/docker-entrypoint.sh

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-openbsd postgresql postgresql-contrib libpq-dev && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn

# Create a new user and group
ENV USER=appuser
ENV GROUP=appgroup
RUN addgroup --system ${GROUP} && \
    adduser --system --ingroup ${GROUP} ${USER} && \
    chown -R ${USER}:${GROUP} /app

# Set the ownership of the /app directory to the new user and group
USER ${USER}:${GROUP}

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run the entrypoint script
ENTRYPOINT ["/app/docker-entrypoint.sh"]
