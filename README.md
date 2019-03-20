# stlp-project

all missions are available inside docker container notebooks. New docker container for each person

each person can run as much as they'd like and can submit through a file conversion and submission using python

build container with all missions included and submission code

docker run -it -p 5901:5901 -p 6901:6901 -p 8888:8888 -e VNC_PW=vncpassword malmo-me

## Mission Types
### Phase 1 static
1.) navigate static obstacles: static directions, no observations
    - Flat world, narrow rooms
    - two block high obstacles, list of maps

1.) solving all these with the same agent

### Phase 2 dynamic
1.) navigate dynamic obstacles: observation-based directions
    - flat world, narrow rooms
    - two block high random arrangement

1.) navigate maze: observation-based directions with memory
1.) navigate maze with dynamic obstacles: increased complexity

### Phase 3 
1.) mob escape: observation-based directions, entity tracking, strategy development
1.) mob escape with obstacles: observation-based directions, entity tracking, strategy development

1.) mob fight - kill the zombies: observation-based directions, entity tracking, strategy development


basic programming skills, programming exactly what to do
general case thinking 



binary search
sorting algorithm
breadth first search