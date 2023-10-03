FROM python:3.11-slim
#Setting up an app directory
WORKDIR /usr/src/backend
#Copy content
COPY . .
#Making container logs unbuffered 
ENV PYTHONUNBUFFERED 1
#installing dependencies
RUN pip3 install -r ./requirements.txt

#running the app
CMD python manage.py runserver 0.0.0.0:8000