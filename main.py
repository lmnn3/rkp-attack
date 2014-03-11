#!/usr/bin/env python3
# -*- mode: python; tab-width: 4; indent-tabs-mode: nil -*-

import networkx as nx
import matplotlib.pyplot as plt

# TODO figure out what this does
# http://networkx.github.io/documentation/latest/reference/generated/networkx.generators.geometric.geographical_threshold_graph.html#networkx.generators.geometric.geographical_threshold_graph
G=nx.geographical_threshold_graph(n=42, theta=1)

nx.draw(G)
plt.show()
