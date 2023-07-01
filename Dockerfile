# Use the official Python image as the base image
FROM python:3.9

# Set the working directory to /srv/app
WORKDIR /srv/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    USER=appuser \
    GROUP=appgroup

# Copy the project files to the container
COPY . /srv/app/

# Set execute permission on the entrypoint script
RUN chmod +x /srv/app/docker-entrypoint.sh

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-openbsd postgresql postgresql-contrib libpq-dev && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn

# Create a new user and group
RUN addgroup --system ${GROUP} && \
    adduser --system --ingroup ${GROUP} ${USER} && \
    chown -R ${USER}:${GROUP} /srv/app/

# Set the ownership of the /srv/app directory to the new user and group
USER ${USER}:${GROUP}

# Run the entrypoint script
ENTRYPOINT ["/srv/app/docker-entrypoint.sh"]
