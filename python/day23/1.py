import sys
import networkx as nx

sys.path.append("/".join(__file__.split("/")[:-2]))
import utils


edges = list(utils.input_lines("{}-{}"))
lan_party = nx.from_edgelist(edges)

triangles = [
    clique for clique in nx.enumerate_all_cliques(lan_party) if len(clique) == 3
]


def has_t(triangle):
    return any(x.startswith("t") for x in triangle)


triangles = filter(has_t, triangles)

print(len(list(triangles)))
