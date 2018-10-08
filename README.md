# neolang-api

## Development setup

### Copy env vars and update them as necessary
```
cp .env.example .env
```

### Create virtual env
```
virtual env .venv
source .venv/bin/activate
(.venv) pip install -r requirements.txt
(.venv) pip install -U pip
```

### Create and migrate database
```
flask db upgrade
```

### Seed DB manually by running seed.sql in neolang DB
...

Now the app is ready to run.

```
flask run
# go to http://localhost:5000/v1/parts
```