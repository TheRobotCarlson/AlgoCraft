#!/usr/bin/env python
# coding: utf-8

# In[6]:


from UserAgent import UserAgent
import random
import time


class MyAgent(UserAgent):
    def __init__(self):
        super(MyAgent, self).__init__()
        self.name = "Brian"  # keep this and put your own name

        # TODO: Initialize any variables you'll need here!
        self.history = []

    def take_action(self, position, world_info):
        # TODO: replace the code below with your own!


        # print(world_info[0]) # 3x3 square beneath our feet
        # print(world_info[1]) # 3x3 square 1 block above our feet
        # print(world_info[2]) # 3x3 square 2 blocks above our feet

        # print(world_info[0][0], world_info[1][0], world_info[2][0]) # type of blocks in front of us
        # print(world_info[0][2], world_info[1][2], world_info[2][2]) # type of blocks behind us
        
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
        print("Random action: %s" % action)

        # try to send the selected action
        self.move_direction(action)


# In[8]:


# Run to submit your code. Don't modify this!
if __name__ == "__main__":
    import subprocess
    import time
    
    subprocess.check_output(["jupyter", "nbconvert", "--to", "script", "solution.ipynb"])
    print("done")
    time.sleep(2)
    print("running here")
    temp = subprocess.check_output(["python", "../../mission_server.py", "mission2.a"]).decode("utf-8").replace('\\\r\\\n', '\r\n')
    print(temp)
    


# In[17]:


print()


# In[ ]:




