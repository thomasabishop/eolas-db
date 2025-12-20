# eolas-db

A Python application that parses Markdown entries in my
[zettelkasten](https://github.com/thomasabishop/eolas), extracts the content
and metadata and inserts it into an SQLite database.

It is a constituent part of my knowledge management system comprising [eolas](https://forgejo.systemsobscure.net/thomasabishop/eolas),
[eolas-api](https://forgejo.systemsobscure.net/thomasabishop/eolas-api), and [eolas-app](https://forgejo.systemsobscure.net/thomasabishop/eolas-app).

Usage:

```sh
app.py --source="/my-zettelkasten-entries" --target="/tmp/zettelkasten-output-dir"

```

- `--source`
  - The directory containing the Markdown files
- `--target`
  - The location where the resulting SQLite file should be save

## Local development

```sh
source venv/bin/activate
python3 src/app.py --source="/my-zettelkasten-entries" --target="/tmp/zettelkasten-output-dir"
```

## Production

### Generate single executable

```sh
source venv/bin/activate
sudo pyinstaller --onefile ./src/app.py --distpath="/usr/local/bin/eolas-db"
```

### Run executable

```sh
/usr/local/bin/eolas-db/app --source="/my-zettelkasten-entries" --target="/tmp/zettelkasten-output-dir"
```

## ERM

![ERM diagram for eolas-db](./eolas-db-ERM.png)

> In addition to the tables listed in the diagram, there is a [full-text search](https://sqlite.org/fts5.html) virtual table applied to `entries`. This enables search queries against the text of every entry.

