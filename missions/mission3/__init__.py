
from .solution import MyAgent
import random

mission = "mission3"

def mission_init(my_mission):
    starting_locations = [-1.5, -0.5, 0.5, 1.5, 2.5]
    reward_locations = [-2, -1, 0, 1, 2]

    start_loc = random.randint(0, len(starting_locations) - 1)
    block_loc = random.randint(0, len(reward_locations) - 1)

    my_mission.startAt(starting_locations[start_loc], 4.0, 1.5)
    my_mission.drawBlock(reward_locations[block_loc], 3, 11, "redstone_block")