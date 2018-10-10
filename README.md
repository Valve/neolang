# neolang-api

## Development setup

### Copy env vars and update them as necessary
```
cp .env.example .env
```

### Create virtual env
```
virtualenv .venv
source .venv/bin/activate
(.venv) pip install -r requirements.txt
(.venv) pip install -U pip
```

### Create and migrate database
```
flask db upgrade
```

### Seed DB 

```
# seed entry types separately
flask seed-entry-types
# seed the rest of the data
flask seed
```

Now the app is ready to run.

```
flask run
# go to http://localhost:5000/v1/parts
```
