rm -f ./db.sqlite3
./venv/bin/python ./core/manage.py migrate
./venv/bin/python ./core/manage.py loaddata 1_abstract 2_linked