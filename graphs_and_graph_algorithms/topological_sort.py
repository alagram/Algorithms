import os, sys
sys.path.insert(0, os.path.abspath(".."))
from graphs_and_graph_algorithms.graph import Graph

class TopologicalSort(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
        self.topological_list = []

    def topological_sort(self):
        for a_vert in self:
            a_vert.set_color('white')
            a_vert.set_pred(-1)
        for a_vert in self:
            if a_vert.get_color() == 'white':
                self.dfs_visit(a_vert)
        return self.topological_list

    def dfs_visit(self, start_vert):
        start_vert.set_color('gray')
        self.time += 1
        self.set_discovery(self.time)

        for next_vert in start_vert.get_connections():
            if next_vert.get_color() == 'white':
                next_vert.set_pred(start_vert)
                self.dfs_visit(next_vert)
        start_vert.set_color('black')
        self.time += 1
        start_vert.set_finish(self.time)
        self.topological_list.append(0, (start_vert, self.time))
