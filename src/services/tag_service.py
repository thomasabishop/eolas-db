from services.sqlite_service import SqliteService


class TagService(SqliteService):
    def __init__(self, db_connection):
        super().__init__(db_connection)

    def __retrieve_entries_for_tag(self, tag):
        entries = self._query("SELECT * FROM entries_tags WHERE tag_name = ?", (tag,))
        return sorted([entry[0] for entry in entries])

    def export_tags(self):
        tags = self._query("SELECT * FROM tags")
        tags = sorted([tag[0] for tag in tags])
        tag_dict = {}
        for tag in tags:
            tag_dict[tag] = self.__retrieve_entries_for_tag(tag)
        return tag_dict
