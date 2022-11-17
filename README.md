## CDC Demo

### Initial Setup

Update the `.env` file to add a [database url](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING):

```
DATABASE_URL="postgresql://USERNAME:password@12.34.56.789:5432/postgres"
```

Install python requirements with:

```
pip install -r requirements.txt
```

### Inserting Events

Make sure you have whitelisted access to the postgres
instance from your IP then run `generate_events.py`

```
python generate_events.py
```

### Schema

