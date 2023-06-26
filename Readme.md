# Template django project

This is template django project created for testing purposes.
Contains only dummy data.


### install

```bash
git clone https://github.com/alimushali/template-django-project.git
cd ./template-django-project

# assuming you have python, virtualenv and python-wheel installed
python -m venv venv && source ./venv/bin/activate && pip install -r requirements.txt
chmod +x ./make_db.sh && chmod +x ./run_gunicorn.sh && /opt/app/make_db.sh
```


### run in cli
```bash
python core/manage.py runserver
```

### run in podman

See docs/podman.md