## DB migrations

### Apply migration manually:
Inside flask_app container call
```shell
poetry run python -m flask db migrate upgrade --directory capybara_clicker/migrations/
```

### Create new migration:
Inside flask_app container call
```shell
poetry run python -m flask db migrate -m "Initil migration" --directory capybara_clicker/migrations/
```

It will create migration in folder capybara_clicker/migrations/versions