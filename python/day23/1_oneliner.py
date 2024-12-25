import sys
import networkx as nx

print(len(list(filter(lambda t: any(x.startswith("t") for x in t),[clique for clique in nx.enumerate_all_cliques(nx.from_edgelist(list(map(lambda x: x.split("-"),sys.stdin.read().splitlines(False),))))if len(clique) == 3],))))  # fmt: skip
