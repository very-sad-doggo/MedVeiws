FROM python:3.11-slim
#Setting up an app directory
WORKDIR /usr/src/create_tables
#Copy content
COPY . .
#Making container logs unbuffered 
ENV PYTHONUNBUFFERED 1

#installing dependencies
RUN pip3 install -r ./requirements.txt

#running the app
ENTRYPOINT ["python3", "create_tables.py"]