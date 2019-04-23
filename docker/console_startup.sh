#!/bin/bash
/dockerstartup/vnc_startup.sh echo "Starting Malmo Minecraft Mod"

# Launch mimecraft (which may take several minutes first time)
python3 -c "import malmo.minecraftbootstrap;malmo.minecraftbootstrap.launch_minecraft()"
echo "Starting jupyter"
# ./mission0/solution.ipynb
cd /home/malmo/missions
jupyter notebook --ip 0.0.0.0 --no-browser 
