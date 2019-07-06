
from .solution import MyAgent

mission = "mission1a"
starting_location = 0, 4, -2
target_location = [-2, 3, 10]

def mission_init(my_mission):
    my_mission.startAt(*starting_location)