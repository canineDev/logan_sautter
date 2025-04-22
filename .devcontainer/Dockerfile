FROM mcr.microsoft.com/devcontainers/universal:2-linux

# Set working dir
WORKDIR /app

# Grab updates
RUN apt-get update

# Install Node.js and Vue CLI
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g @vue/cli

# install Flask
RUN pip install flask

# Expose ports for Flask and Vue
EXPOSE 5173 5000
