import random
from .road import Road
import time
from collections import deque


class TrafficSignal:
    def __init__(self, roads, road_groups, config={}):
        # Initialize roads
        self.roads = roads
        # Set default configuration
        self.set_default_config()
        self.road_groups = road_groups
        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)
        # Calculate properties
        self.init_properties()
        self.timie = time.time()
        self.last_green_time = {i: 0 for i in range(len(self.roads))}
        self.max_density_queue = deque()

    def update_time(self):
        self.time = time.time()

    def set_default_config(self):
        self.cycle = [(True, False, False, False), (True, False, False, False), (False, False, True, False),
                      (False, True, False, False),
                      (False, False, False, True)]
        self.slow_distance = 50
        self.slow_factor = 0.4
        self.stop_distance = 12

        self.current_cycle_index = 0

        self.last_t = 0

    def init_properties(self):
        for i in range(len(self.roads)):
            for road in self.roads[i]:
                road.set_traffic_signal(self, i)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]

    def update(self, sim):
        # get the current time
        current_time = time.time()

        # calculate the average number of vehicles for each road
        avg_num_vehicles = [sum([road.get_num_vehicles() for road in self.roads[i]]) / len(self.roads[i]) for i in
                            range(len(self.roads))]

        # get the index of the road with the highest density
        max_density_index = avg_num_vehicles.index(max(avg_num_vehicles))

        # if the road with the highest density has not been green for a while, make it green
        if current_time - self.last_green_time[max_density_index] > 5:
            self.current_cycle_index = max_density_index

        # calculate the cycle length based on the current traffic volume
        cycle_length = 100 / (max(avg_num_vehicles) + 1e-8)
        # randomize the cycle length after every cycle
        if (sim.t % cycle_length == 0):
            cycle_length = random.randint(20, 40) / (max(avg_num_vehicles) + 1e-8)

        # update the current cycle index based on the cycle length
        k = (sim.t // cycle_length) % len(self.cycle)
        self.current_cycle_index = int(k)

        self.update_time()

        # update the last green time for the current cycle index
        self.last_green_time[self.current_cycle_index] = current_time