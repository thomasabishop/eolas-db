# eolas-db

This CLI application parses entries in my
[zettelkasten](https://github.com/thomasabishop/eolas) and extracts key metadata
about each entry. It creates and populates an SQLite database and offers options for
exporting mapped relations between entries.

## Local development

```
source venv/bin/activate
eolas-db [opts]
```

## Production

After development is complete, instead of compiling to a single executable I can just install the application
with `pipx` like any other.

```
pipx install [local_path_to_application]
eolas-db [opts]
```

### Update after changes

```
pipx uninstall eolas-db
pipx install [local_path_to_application]
```

## Options

### `populate`

```
eolas-db populate
```

Parse Eòlas entries and extract key metadata and body text, import into database
tables.

## ERM

![ERM diagram for eolas-db](./eolas-db-ERM.png)

## Resources

https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3
