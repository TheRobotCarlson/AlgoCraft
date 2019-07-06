# from __future__ import print_function

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

    def turn_right(self):
        self.try_command("turn 1")

    def turn_left(self):
        self.try_command("turn -1")

    def move_north(self):
        self.try_command("movenorth 1")
    
    def move_south(self):
        self.try_command("movesouth 1")

    def move_west(self):
        self.try_command("movewest 1")

    def move_east(self):
        self.try_command("moveeast 1")
    
    def try_command(self, command):
        try:
            self.agent_host.sendCommand(command)
        except RuntimeError as e:
            self.logger.error("Failed to send command: %s \n %s" % (command, e))
    
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

        print(observation_list)
        block_list = []
        # for i in range(0, len(observation_list), 9):
        #     block_list.append([])
        #     for j in range(i, i + 9, 3):
        #         block_list[i // 9].append([])
        #         for k in range(j, j + 3):
        #             # print(i // 9, (j % 9) // 3, k)
        #             # print(block_list)
        #             block_list[i // 9][(j % 9) // 3].append(observation_list[k])

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

