# eolas-db

This application parses data in my [zettelkasten](https://github.com/thomasabishop/eolas) repository and populates an
SQLite database that records key metadata about each entry (tags, backlinks, outlinks etc).

It exposes a command line application for interfacing with the database.

## Local development

```
source venv/bin/activate
eolas-db
```

## ERM

![ERM diagram for eolas-db](./eolas-db-ERM.png)
