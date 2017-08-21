FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

# Create the source code directory.
ARG SOURCE_DIR=/usr/src/app/
RUN mkdir -p ${SOURCE_DIR}
WORKDIR ${SOURCE_DIR}

# Install Linux packages via APT.
RUN apt-get update && \
    apt-get install -y \
        postgresql-client \
        vim && \
    # Remove APT caches to keep image size low.
    rm -rf /var/lib/apt/lists/*

# Install Python packages.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add the source code. If sharing code via volume, the code added at image build time is not used.
COPY . .

# Use Django's manage.py script to serve the application over port 8000.
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]
EXPOSE 8000