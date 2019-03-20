from __future__ import print_function

from future import standard_library
standard_library.install_aliases()
from builtins import range
from builtins import object
import MalmoPython
import json
import logging
import os
import random
import sys
import time
from string import Template
import importlib

if sys.version_info[0] == 2:
    # Workaround for https://github.com/PythonCharmers/python-future/issues/262
    import Tkinter as tk
else:
    import tkinter as tk


if sys.version_info[0] == 2:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
else:
    import functools
    print = functools.partial(print, flush=True)


# command = sys.argv[1]
# my_module = importlib.import_module(command)

# mission = my_module.mission
# agent = my_module.solution.MyAgent()

agent_host = MalmoPython.AgentHost()

# -- set up the mission -- #
mission_file = f'./mission1a.xml'
agent_name = "Brian"

with open(mission_file, 'r') as f:
    print("Loading mission from %s." % mission_file)
    src = Template(f.read())
    mission_xml = src.substitute({"name": agent_name})
    my_mission = MalmoPython.MissionSpec(mission_xml, True)
    
# my_module.mission_init(my_mission)
print("Done loading mission file.")

my_mission.forceWorldReset()
my_mission_record = MalmoPython.MissionRecordSpec()

max_retries = 3

for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print("Error starting mission:", e)
            exit(1)
        else:
            time.sleep(2.5)

# agent_host.startMission(my_mission, my_mission_record)

print("Waiting for the mission to start", end=' ')
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:", error.text)
print(" mission started")

time.sleep(3)
# -- run the agent in the world -- #
# cumulative_reward = agent.run(agent_host)


class UserAgent(object):
    """User Agent for discrete state/action spaces."""

    def __init__(self):
        self.agent_host = None
        self.logger = logging.getLogger(__name__)
        if False: # True if you want to see more information
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        self.logger.handlers = []
        self.logger.addHandler(logging.StreamHandler(sys.stdout))
        self.actions = ["north", "south", "west", "east"]

    def move_direction(self, command):
        """moves the agent in the direction given"""
        d = {"north": "movenorth 1", "south": "movesouth 1", "west": "movewest 1", "east": "moveeast 1"}
        self.try_command(d[command])

    def position_change(self, command):
        """returns the coordinate position change for a given direction"""
        d = {"north": [0, 0, -1], "south": [0, 0, 1], "west": [-1, 0, 0], "east": [1, 0, 0]}

        return d[command]
    
    def init_agent_host(self, agent_host):
        self.agent_host = agent_host

    def move_north(self):
        self.try_command("move 1")
    
    def move_south(self):
        self.try_command("movesouth 1")

    def move_west(self):
        self.try_command("movewest 1")

    def move_east(self):
        self.try_command("moveeast 1")
        
    def turn_left(self):
        self.try_command("turn -0.5")
        
    def turn_right(self):
        self.try_command("turn 0.5")
    
    def try_command(self, command):
        try:
            self.agent_host.sendCommand(command)
        except RuntimeError as e:
            self.logger.error("Failed to send command: %s \n %s" % (command, e))
    
    def get_world_state(self):
        return self.agent_host.getWorldState()
    
    def get_coordinates_from_state_info(self, info):
        return [int(info['XPos']), int(info['YPos']), int(info['ZPos'])]

    def take_action(self, position, world_info):
        pass

    def act(self, world_state):
        """take 1 action in response to the current world state"""
        
        obs_text = world_state.observations[-1].text
        # print(obs_text)
        obs = json.loads(obs_text)
        self.logger.debug(obs)
        if not 'XPos' in obs or not 'ZPos' in obs:
            self.logger.error("Incomplete observation received: %s" % obs_text)
            return 0

        current_s = "%d:%d" % (int(obs['XPos']), int(obs['ZPos']))
        self.logger.debug("State: %s (x = %.2f, z = %.2f)" % (current_s, float(obs['XPos']), float(obs['ZPos'])))

        observation_list = obs["observationarea"]
        block_list = []
        for i in range(0, len(observation_list), 9):
            block_list.append([])
            for j in range(i, i + 9, 3):
                block_list[i // 9].append([])
                for k in range(j, j + 3):
                    # print(i // 9, (j % 9) // 3, k)
                    # print(block_list)
                    block_list[i // 9][(j % 9) // 3].append(observation_list[k])

        self.take_action(self.get_coordinates_from_state_info(obs), block_list)
        time.sleep(0.1)
        # return current_r

    def run(self, agent_host):
        """run the agent on the world"""

        self.agent_host = agent_host

        total_reward = 0
        
        # main loop:
        world_state = self.agent_host.getWorldState()
        while world_state.is_mission_running:
            
            time.sleep(0.1)
            
            if len(world_state.observations) > 0 and not world_state.observations[-1].text=="{}":
                self.act(world_state)
                for reward in world_state.rewards:
                    total_reward += reward.getValue()
                
            world_state = self.agent_host.getWorldState()

        for reward in world_state.rewards:
            total_reward += reward.getValue()

        # process final reward
        self.logger.debug("Final reward: %d" % total_reward)

        return total_reward


class MyAgent(UserAgent):
    def __init__(self):
        super(MyAgent, self).__init__()
        self.name = "YOUR NAME HERE"  # keep this and put your own name

        # TODO: Initialize any variables you'll need here!
        self.history = []

    def take_action(self, position, world_info):
        # TODO: replace the code below with your own!


        # print(world_info[0]) # 3x3 square beneath our feet
        # print(world_info[1]) # 3x3 square 1 block above our feet
        # print(world_info[2]) # 3x3 square 2 blocks above our feet

        # print(world_info[0][0], world_info[1][0], world_info[2][0]) # blocks in front of us
        # print(world_info[0][2], world_info[1][2], world_info[2][2]) # blocks behind us
        
        # print(position) # our position in the map
        self.history.append(position)

        # select the next action
        rnd = random.random()
        
        a = random.randint(0, len(self.actions) - 1) # actions are to move north, south, east, west ...for now
        action = self.actions[a]

        # if the two blocks in front of us are stone, randomly choose another action
        while (action == "north" and (world_info[1][0][1] == "stone" or world_info[2][0][1] == "stone")):  
            a = random.randint(0, len(self.actions) - 1)
            action = self.actions[a]

        position_change = self.position_change(action)
        next_position = [position[i] + position_change[i] for i in range(len(position))]
        print("next pos:", next_position)
        self.logger.info("Random action: %s" % action)

        # try to send the selected action
        self.move_direction(action)



agent = MyAgent()
agent.run(agent_host)
# agent.init_agent_host(agent_host)

# agent.turn_left()

# agent_host.sendCommand("movewest 1")
# agent_host.sendCommand("movewest 1")
# agent_host.sendCommand("movenorth 1")
# agent_host.sendCommand("movenorth 1")
# agent_host.sendCommand("moveeast 1")
# agent_host.sendCommand("moveeast 1")