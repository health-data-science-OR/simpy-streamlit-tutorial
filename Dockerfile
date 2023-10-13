# Start with a small python image (version 3.8)
FROM python:3.9-slim

# streamlit working dir is /app
RUN mkdir /app
WORKDIR /app

# The slim build is minimal. Install essentials so that it works with python 
# Git means we can clone from a repo instead of local copy if needed. 
# curl to perform health check
# Clean up after. 
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# clone the repository to the app directory 
RUN git clone https://github.com/health-data-science-OR/simpy-streamlit-tutorial /app

# pip install the software dependencies e.g. simpy 4.0 and streamlit
RUN pip3 install -r content/03_streamlit/requirements.txt

# EXPOSE PORT 8501 - standard for streamlit.
EXPOSE 8501

# run app on 0.0.0.0:8501
# This means that the app will run when the image is launched.
ENTRYPOINT ["streamlit", "run", "content/03_streamlit/app_to_deploy.py", "--server.port=8501", "--server.address=0.0.0.0"]
