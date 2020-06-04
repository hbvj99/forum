# Forum
A classic discussion app build on Django.

![Screenshot from 2019-12-20 21-18-28](https://user-images.githubusercontent.com/43197293/76218953-2adee800-623d-11ea-87f0-ff7cdbe0072f.png)

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
Its build on Django REST framework 3. Refer [here](https://github.com/hbvj99/django_forum/blob/master/REST_API.txt) for simple CRUD operations.

![Screenshot from 2020-03-09 19-39-02](https://user-images.githubusercontent.com/43197293/76219303-bd7f8700-623d-11ea-99ea-62515d31bc51.png)

To get discussion details;
```http://localhost:8000/api-discussion/ID/```

To add new discussion;

Non-image: ```http://127.0.0.1:8000/api-discussion/new -d title='YOUR_TITLE' -d content='YOUR_CONTENT' -d user=USER_ID```

With image: ```http://127.0.0.1:8000/api-discussion/new -d title='YOUR_TITLE' -d content='YOUR_CONTENT' -d img='FILE_NAME' -d user=USER_ID (not stable)```

To delete;
```http://localhost:8000/api-discussion/ID/```

To Update;
```http://127.0.0.1:8000/api-discussion/new -d title='YOUR_TITLE' -d content='YOUR_CONTENT' -d user=USER_ID```
