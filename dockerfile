# 1. Use an official lightweight Python image
FROM python:3.10-slim

# 2. Set environment variables to prevent Python from writing .pyc files 
# and to ensure stdout/stderr logs are sent straight to the terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Install system dependencies required for UMAP, SHAP, and other C-based libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# 4. Set the working directory inside the container
WORKDIR /app

# 5. Copy requirements file and install Python dependencies
# We do this before copying the full code to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the application code, including the model weights (.pth)
COPY . .

# 7. Expose the default Streamlit port
EXPOSE 8501

# 8. Define the healthcheck to ensure the container is running correctly
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# 9. Command to launch the Streamlit application on container startup
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]