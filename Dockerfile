FROM python:3.10

# Set the working directory to /usr/src/app
WORKDIR /usr/src/app

# Copy everything from your current directory to /usr/src/app
COPY . .

# Install Python dependencies
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r req.txt

# Ensure the entrypoint script is executable
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
