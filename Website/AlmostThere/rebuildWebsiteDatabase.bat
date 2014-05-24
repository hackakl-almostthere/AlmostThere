rm -rf data\Website.db
py manage.py syncdb
py manage.py test

