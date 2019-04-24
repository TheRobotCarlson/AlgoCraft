
from .solution import MyAgent

mission = "mission0"
target_location = [-2, 3, 10]
starting_location = -1.5, 4.0, 1.5

def mission_init(my_mission):
    my_mission.startAt(*starting_location)