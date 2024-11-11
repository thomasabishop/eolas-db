import os
import re

import frontmatter


class ParseMarkdownService:
    """Extract tags, internal links and body text from Markdown entries"""

    def __init__(self):
        pass

    def __get_internal_links(self, file):
        link_rgx = r"\[.*?\]\(([^)]+\.md)\)"
        with open(file, "r") as f:
            internal_links = []
            lines = f.readlines()
            for line in lines:
                internal_link = re.findall(link_rgx, line)
                if internal_link:
                    internal_links.append(
                        [os.path.basename(link) for link in internal_link]
                    )
            return [item for row in internal_links for item in row]

    def parse(self, markdown_file):
        with open(markdown_file) as f:
            metadata, content = frontmatter.parse(f.read())
            return {
                "tags": metadata.get("tags", []),
                "body": content or "",
                "links": self.__get_internal_links(markdown_file) or [],
            }
