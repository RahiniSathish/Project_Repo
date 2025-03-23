# Use official Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8000

# Start the Streamlit app correctly
CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]
