# -*- mode: python; tab-width: 4; indent-tabs-mode: nil -*-
#
# Copyright © 2014 Michael Catanzaro
# Copyright © 2014 Levi Malott
#
# This file is part of RKP Attack.
#
# RKP Attack is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# RKP Attack is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with RKP Attack.  If not, see <http://www.gnu.org/licenses/>.

import random

    
class Sensor:
    def __init__(self, num_keys, total_keys):
        self.keys = random.sample(range(total_keys), num_keys)

def is_key_shared(s, t):
    '''
    true if sensor s shares a key with sensor t
    '''
    for s_key in s.keys:
        for t_key in t.keys:
            if s_key == t_key:
                return True
    return False


def add_logical_edge_one_hop(physical_graph, logical_graph, s_node, t_node):
    '''
    true if the sensor at node s shares a key with the sensor at node t, or if
    the sensor at node s shares a key with any sensor within range of the
    sensor at node t, and the sensor at node t also shares a key with that
    sensor. It makes sense!
    '''
    s_sensor = logical_graph.node[s_node]['sensor']
    t_sensor = logical_graph.node[t_node]['sensor']
    if is_key_shared(s_sensor, t_sensor):
        logical_graph.add_edge(s_node, t_node)
        return
    s_neighbors = set(physical_graph.neighbors(s_node))
    t_neighbors = set(physical_graph.neighbors(t_node))
    for r_node in list(s_neighbors & t_neighbors) + \
                  list(s_neighbors - t_neighbors) + \
                  list(t_neighbors - s_neighbors):
        r_sensor = logical_graph.node[r_node]['sensor']
        if is_key_shared(r_sensor, s_sensor) and \
           is_key_shared(r_sensor, t_sensor):
            logical_graph.add_edge(s_node, t_node)
            return
