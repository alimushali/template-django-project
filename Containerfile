# Dockerfile

FROM python:3.12-rc-bullseye


# copy source and install dependencies
RUN mkdir -p /opt/app/
COPY requirements.txt run_gunicorn.sh make_db.sh /opt/app/
RUN mkdir -p /opt/app/core
COPY core /opt/app/core
WORKDIR /opt/app
ENV PYTHONPATH "${PYTHONPATH}:/opt/app/core"
RUN pip install wheel virtualenv
RUN python -m venv venv
RUN ./venv/bin/pip install -r requirements.txt
RUN chmod +x /opt/app/make_db.sh
RUN chmod +x /opt/app/run_gunicorn.sh
RUN ./make_db.sh



# start server
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/opt/app/run_gunicorn.sh"]

