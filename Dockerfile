FROM postgres:15
#For testing purposes psql is listening to 0.0.0.0
#RUN sed -i 's/listen_addresses = \[\]/listen_addresses = \[\"\*\"\]/g' /etc/postgresql/14/main/postgresql.conf
# RUN /etc/init.d/postgresql stop
# RUN /etc/init.d/postgresql start
HEALTHCHECK --interval=10s --timeout=3s CMD ["/usr/local/bin/pg_isready", "--username=django"] 
#|| exit 1

# #layer for python scripts
# FROM python:3.11-slim
# #workdir for execution
# WORKDIR /usr/src/prepare_db
# #Copy content
# COPY ./create_tables/. .
# #Making container logs unbuffered 
# ENV PYTHONUNBUFFERED 1
# #installing dependencies
# RUN pip3 install psycopg2-binary
# # #wait Until postgres is ready
# # RUN sleep 180
# #running the app

# ENTRYPOINT ["python3", "create_tables.py"]
