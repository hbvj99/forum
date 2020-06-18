# Forum
A classic discussion app build on Django.

## How to run locally
```
- Clone this repository
- Setup virtual environment using Python => 3.x.x version (virtualenv venvp)
- cd venv
- Install dependencies using (pip install -r requirements.txt)
```

### Postgres database config
```
- psql -U postgres
- create user django_forum with password 'aqi_app';
- create database django_forum;
- grant all privileges on database django_forum to django_forum;
```

### Migrate
```
- python manage.py makemigrations
- python manage.py migrate
```

### Run server
```
- python manage.py runsever
```
### Extra
### Backup/Restore data
```
./manage.py dumpdata > backupdb.jspn
./manage.py loaddata backupdb.json
```

### API
Its build on Django REST framework 3. Refer [here](https://github.com/hbvj99/forum/blob/master/REST_API.txt) for simple CRUD operations.
