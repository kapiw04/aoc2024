import sys
import networkx as nx

sys.path.append("/".join(__file__.split("/")[:-2]))
import utils


edges = list(utils.input_lines("{}-{}"))
lan_party = nx.from_edgelist(edges)

cliques = nx.enumerate_all_cliques(lan_party)


def find_max_list(list):
    return max(list, key=len)


password = ",".join(sorted(find_max_list(cliques)))

print(password)
