import frontmatter


class MarkdownParseService:
    """Extract tags, links and body text from Markdown entries"""

    def __init__(self, eolas_file):
        self.eolas_file = eolas_file

    def parse(self):
        with open(self.eolas_file) as f:
            metadata, content = frontmatter.parse(f.read())
            return {
                "tags": metadata.get("tags", []),
                "body": content or "",
            }
