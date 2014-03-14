# -*- mode: python; tab-width: 4; indent-tabs-mode: nil -*-
#
# Copyright © 2014 Michael Catanzaro
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
    def __init__(self, num_keys, total_keys, probability_evil):
        self.keys = random.sample(range(total_keys), num_keys)
        self.evil = (random.random() < probability_evil)


def is_key_shared(s, t):
    '''
    true if sensor s shares a key with sensor t
    '''
    for s_key in s.keys:
        for t_key in t.keys:
            if s_key == t_key:
                return True
    return False
