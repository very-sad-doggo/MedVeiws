FROM python:3.11-slim
#Setting up an app directory
WORKDIR /usr/src/backend
#Copy content
COPY . .
#Making container logs unbuffered 
ENV PYTHONUNBUFFERED 1
#installing dependencies
RUN pip3 install -r ./requirements.txt
#allowing frontend to connect
RUN sed -i 's/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \[\"\*\"\]/g' lib_catalog/settings.py && \
    echo >> lib_catalog/settings.py && \
    echo CORS_ORIGIN_ALLOW_ALL = True >> lib_catalog/settings.py
#running the app
CMD python manage.py runserver 0.0.0.0:8000