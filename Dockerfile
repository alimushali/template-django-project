# Dockerfile
FROM python:3.12-rc-bullseye

# copy source and install dependencies
COPY core /opt/app/core
COPY make_db.sh /opt/app/
COPY run_gunicorn.sh /opt/app/
COPY requirements.txt /opt/app/
ENV PYTHONPATH "${PYTHONPATH}:/opt/app/core"
WORKDIR /opt/app
RUN pip install wheel virtualenv && /usr/local/bin/python -m venv venv 
RUN /opt/app/venv/bin/pip install -r /opt/app/requirements.txt
RUN chmod +x /opt/app/make_db.sh && chmod +x /opt/app/run_gunicorn.sh && /opt/app/make_db.sh
WORKDIR /opt/app/core

# start server
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/opt/app/run_gunicorn.sh"]

