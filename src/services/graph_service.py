import json
from constants import GRAPH_OUTPUT_DIRECTORY 
from services.sqlite_service import SqliteService
from models.graph_node import IGraphNode
from models.graph_edge import IGraphEdge

class GraphService(SqliteService):
    error_message_stub = "Could not retrieve contents of table:"

    def __init__(self, db_connection):
        super().__init__(db_connection)

    def __get_nodes(self) -> list[IGraphNode]:
        tags = self._query(
            "SELECT * FROM tags",
            error_message=f"{self.error_message_stub} tags",
        )
        tags = [IGraphNode(id=f"#{tag[0]}", type="tag") for tag in tags]
        entries = self._query(
            "SELECT title FROM entries",
            error_message=f"{self.error_message_stub} entries",
        )
        
        entries = [IGraphNode(id=entry[0], type="entry") for entry in entries]
        return tags + entries

    def __get_edges(self):
        tags = self._query(
            "SELECT * FROM entries_tags",
            error_message=f"{self.error_message_stub} entries_tags",
        )
    
        tags = [IGraphEdge(source=f"#{tag[1]}", target=tag[0]) for tag in tags]

        backlinks = self._query(
            "SELECT * FROM backlinks",
            error_message=f"{self.error_message_stub} backlinks",
        )
        
        backlinks = [IGraphEdge(source=f"{backlink[0]}", target = backlink[1]) for backlink in backlinks]


        return tags + backlinks

    def generate_graph(self):
        graph = {"nodes": self.__get_nodes(), "edges": self.__get_edges()}

        with open(f"{GRAPH_OUTPUT_DIRECTORY}/eolas-graph.json", "w") as f:
            json.dump(graph, f, indent=4)
