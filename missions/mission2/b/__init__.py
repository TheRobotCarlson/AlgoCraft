from .solution import MyAgent

mission = "mission2b"

def mission_init(my_mission):
    my_mission.startAt(2.5, 4.0, 1.5)
    my_mission.drawBlock(2, 3, 10, "redstone_block")