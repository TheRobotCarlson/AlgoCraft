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

        self.actions = ["movenorth 1", "movesouth 1", "movewest 1", "moveeast 1"]

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
        return (int(info['XPos']), int(info['YPos']), int(info['ZPos']))

    def take_action(self, position, world_info):
        pass

    def act(self, world_state):
        """take 1 action in response to the current world state"""
        time.sleep(0.1)
        obs_text = world_state.observations[-1].text
        obs = json.loads(obs_text)
        self.logger.debug(obs)
        if not 'XPos' in obs or not 'ZPos' in obs:
            self.logger.error("Incomplete observation received: %s" % obs_text)
            return 0

        current_s = "%d:%d" % (int(obs['XPos']), int(obs['ZPos']))
        self.logger.debug("State: %s (x = %.2f, z = %.2f)" % (current_s, float(obs['XPos']), float(obs['ZPos'])))

        self.take_action(self.get_coordinates_from_state_info(obs), obs["observationarea"])
        print(obs_text)

        # return current_r

    def run(self, agent_host):
        """run the agent on the world"""

        total_reward = 0
        
        is_first_action = True
        self.agent_host = agent_host
        # main loop:
        world_state = self.agent_host.getWorldState()
        # print(world_state)
        while world_state.is_mission_running:

            time.sleep(0.1)
            self.act(world_state)

            for reward in world_state.rewards:
                total_reward += reward.getValue()
            
            world_state = self.agent_host.getWorldState()

            # if is_first_action:
            #     # wait until have received a valid observation
            #     while True:
            #         print("stuck in first:", world_state)

            #         time.sleep(0.1)
            #         world_state = self.agent_host.getWorldState()
            #         for error in world_state.errors:
            #             self.logger.error("Error: %s" % error.text)
            #         for reward in world_state.rewards:
            #             current_r += reward.getValue()
            #         if world_state.is_mission_running and len(world_state.observations)>0 and not world_state.observations[-1].text=="{}":
            #             print("first act")
            #             total_reward += self.act(world_state, current_r)
            #             break
            #         if not world_state.is_mission_running:
            #             break

            #     is_first_action = False
            # else:
            #     # wait for non-zero reward
            #     while world_state.is_mission_running and current_r == 0:
            #         print("stuck in second:", world_state)

            #         time.sleep(0.1)
            #         world_state = self.agent_host.getWorldState()
            #         for error in world_state.errors:
            #             self.logger.error("Error: %s" % error.text)
            #         for reward in world_state.rewards:
            #             current_r += reward.getValue()
                    
            #     # allow time to stabilise after action
            #     while True:
            #         print("stuck in third:", world_state)

            #         time.sleep(0.1)
            #         world_state = self.agent_host.getWorldState()
            #         for error in world_state.errors:
            #             self.logger.error("Error: %s" % error.text)
            #         for reward in world_state.rewards:
            #             current_r += reward.getValue()
            #         if world_state.is_mission_running and len(world_state.observations) > 0 and not world_state.observations[-1].text=="{}":
            #             print("second act")
            #             total_reward += self.act(world_state, current_r)
            #             break
            #         if not world_state.is_mission_running:
            #             break

        # process final reward
        self.logger.debug("Final reward: %d" % current_r)
        total_reward += current_r        

        return total_reward

