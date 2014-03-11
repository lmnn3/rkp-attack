#!/usr/bin/env python3
# -*- mode: python; tab-width: 4; indent-tabs-mode: nil -*-

import networkx as nx
import matplotlib.pyplot as plt

NUM_SENSORS = 42
SENSOR_RANGE = 0.2

G = nx.random_geometric_graph(NUM_SENSORS, SENSOR_RANGE)

nx.draw(G)
plt.show()
