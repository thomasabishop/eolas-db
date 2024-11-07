TABLE_EXISTS = (
    "SELECT count(*) FROM sqlite_master WHERE type ='table' AND name=:table_name"
)
