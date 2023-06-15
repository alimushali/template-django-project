# Dockerfile

FROM python:3.12-rc-bullseye


# copy source and install dependencies
RUN mkdir -p /opt/app/
COPY requirements.txt run_gunicorn.sh make_db.sh core /opt/app/
WORKDIR /opt/app
ENV PYTHONPATH "${PYTHONPATH}:/opt/app/core"
RUN pip install wheel
RUN pip install -r requirements.txt
# RUN ./make_db.sh
RUN chmod +x /opt/app/run_gunicorn.sh



# start server
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/opt/app/run_gunicorn.sh"]

