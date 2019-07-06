#!/usr/bin/env python
# coding: utf-8

# In[22]:


from UserAgent import UserAgent
import random
import time


class MyAgent(UserAgent):
    def __init__(self):
        super(MyAgent, self).__init__()
        self.name = "Christian"  # keep this and put your own name

        # TODO: Initialize any variables you'll need here!
        self.history = []
        self.states = ["finding wall", "using right hand rule", "ahhh, don't know what to do"]
        self.state = 0
        self.orientation = 0
    
    def rotate_2d_array(self, arr, num):
        
        rotated = arr
        for _ in range(num):
            rotated = zip(*rotated[::-1])
            
        return rotated
    
    def take_action(self, position, world_info):
        print(position)
        # self.move_east()
        self.move_direction("east")
        # self.try_command("strafe -1")
        
#         world_info = self.rotate_2d_array(world_info, self.orientation)
        
#         x, y, z = self.target_location
#         x, y, z = self.starting_location
        
#         front_ground = world_info[0][0][1]
#         front_bottom = world_info[1][0][1]
#         front_top    = world_info[2][0][1]
        
#         right_ground = world_info[0][1][2]
#         right_bottom = world_info[1][1][2]
#         right_top    = world_info[2][1][2]
        # left_ground = world_info[0][1][0]

        # print(world_info[0]) # 3x3 square beneath our feet
        # print(world_info[1]) # 3x3 square 1 block above our feet
        # print(world_info[2]) # 3x3 square 2 blocks above our feet

        # print(world_info[0][0], world_info[1][0], world_info[2][0]) # blocks in front of us
        # print(world_info[0][2], world_info[1][2], world_info[2][2]) # blocks behind us
        
#         # print(position) # our position in the map
#         self.history.append(position)
#         print(self.states[self.state])
        
#         if self.state == 0: # looking for a wall
#             if front_bottom == "stone": # found a wall
#                 self.turn_left()
#                 self.state = 1
#             else:
#                 self.move_north()
#             return
#         elif self.state == 1:
#             if right_bottom == "stone":
#                 if front_bottom != "stone":
#                     self.move_north()
#                 else: # we're in a corner!
#                     self.turn_left()
#             elif right_bottom == "air": # last block was stone, opening here
#                 self.turn_right()
#                 self.move_north()
#         else:
#             self.state = 2
            
#         # select the next action
#         rnd = random.random()
        
#         a = random.randint(0, len(self.actions) - 1) # actions are to move north, south, east, west ...for now
#         action = self.actions[a]

#         # if the two blocks in front of us are stone, randomly choose another action
#         while (action == "north" and (world_info[1][0][1] == "stone" or world_info[2][0][1] == "stone")):  
#             a = random.randint(0, len(self.actions) - 1)
#             action = self.actions[a]

#         position_change = self.position_change(action)
#         next_position = [position[i] + position_change[i] for i in range(len(position))]
#         print("next pos:", next_position)
#         self.logger.info("Random action: %s" % action)

#         # try to send the selected action
#         self.move_direction(action)


# In[26]:



if __name__ == "__main__":
    import subprocess
    import time
    
    subprocess.check_output(["jupyter", "nbconvert", "--to", "script", "solution.ipynb"])
    print("done")
    time.sleep(5)
    print("running here")
    temp = subprocess.check_output(["python", "../../mission_server.py", "mission1.a"]).decode("utf-8").replace('\\\r\\\n', '\r\n')
    print(temp)
    


# In[11]:


# %%time
# subprocess.check_output(["jupyter", "nbconvert", "--to", "script", "solution.ipynb"])


# In[ ]:




