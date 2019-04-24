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

agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print('ERROR:', e)
    print(agent_host.getUsage())
    exit(1)

if agent_host.receivedArgument("help"):
    print(agent_host.getUsage())
    exit(0)

# client_pool = MalmoPython.ClientPool()
# client_pool.add(MalmoPython.ClientInfo('localhost', 10001))

command = sys.argv[1]
my_module = importlib.import_module(command)

print(my_module)
# from my_module.solution import MyAgent
mission = my_module.mission
agent = my_module.MyAgent()
agent.target_location = my_module.target_location
agent.starting_location = my_module.starting_location
# -- set up the mission -- #
mission_file = '../../missionfiles/%s.xml' % mission

with open(mission_file, 'r') as f:
    print("Loading mission from %s." % mission_file)
    src = Template(f.read())
    mission_xml = src.substitute({"name": agent.name})
    my_mission = MalmoPython.MissionSpec(mission_xml, True)
    
my_module.mission_init(my_mission)
print("Done loading mission file.")

my_mission.forceWorldReset()
my_mission_record = MalmoPython.MissionRecordSpec()

max_retries = 3

for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, my_mission_record)

        # agent_host.startMission( my_mission, client_pool, my_mission_record, 0, "blah")
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
cumulative_reward = agent.run(agent_host)
print('Cumulative reward: %d' % cumulative_reward)