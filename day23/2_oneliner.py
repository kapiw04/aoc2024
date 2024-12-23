import networkx as nx
import sys

print(",".join(sorted(max([clique for clique in nx.find_cliques(nx.from_edgelist(list(map(lambda x:x.split("-"),sys.stdin.read().splitlines(False),))))],key=len,))))  # fmt: skip
