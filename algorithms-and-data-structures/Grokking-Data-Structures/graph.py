from typing import Any, Optional


class Vertex:
    def __init__(self, key: Any) -> None:
        self.id: Any = key
        self._adj_list: SinglyLinkedList = SinglyLinkedList()

    def has_edge_to(self, destination_vertex: Any) -> Optional:
        return self.has_edge_to._search_edge(destination_vertex) is not None

    def add_edge_to(self, destination_vertex: Any) -> Optional:
        if self.has_edge_to(destination_vertex):
            raise ValueError(f"edge already exists: {self} -> {destination_vertex}")
