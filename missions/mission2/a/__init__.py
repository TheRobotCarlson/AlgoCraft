from .solution import MyAgent

mission = "mission2a"
target_location = [0, 3, 10]
starting_location = [-1.5, 4.0, 1.5]

def mission_init(my_mission):
    my_mission.startAt(-1.5, 4.0, 1.5)
    my_mission.drawBlock(0, 3, 10, "redstone_block")
