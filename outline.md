## introduction
AlgoCraft is a platform for teaching programming, algorithms, and AI principles in an environment that encourages exploration of programming concepts. It uses gamification in the form of Minecraft to make learning more effective and enjoyable. 

Minecraft is an extremely popular sandbox game where players are given creative freedom to build and explore a randomly generated 3D world with the potential to have friendly creatures, enemies, weather, day / night cycles, and collaborative play.

This gives a world with both static and dynamic components. Microsoft saw the potential of that environment to be used for artificial intelligence research and experimentation when they created Project Malmo: a game modification that allows for an easier programmatic interface to Minecraft. However, Project Malmo was made with artificial intelligence researchers in mind, not providing an easy-to-use interface.

AlgoCraft builds on Project Malmo's libraries, providing an intuitive and pythonic wrapper. Taking the convention over configuration approach to software development, the platform favors a simple quickstart in place of flexibility. This allows the same tool constructed for reinforcement learning research to be used to teach simpler algorithms and encourage progression into harder AI concepts. 

The AlgoCraft platform can be ran entirely in the cloud and can be made available from the browser, allowing easy access for users with no installs necessary on their end. A student can access challenges anywhere they have access to a browser on a computer. 

## motivation
There are many different platforms being built to teach programming and present it in a way to make it more appealing to all ages. Code.org, for example, has a long list of fun, easy-to-learn programming-like, drag and drop code-block projects. Few of these, however, teach real programming languages or higher level programming ideas like algorithms and artificial intelligence. They're focused around _getting people interested_ in programming.

There are also many different courses and resources online for teaching algorithms. This can be boring and dry to interact with and don't stimulate real-world problems very well. Sites like Hackerrank and LeetCode provide great resources for learning algorithms, but don't provide a fun environment to do it in. They are focused around people _practicing for interviews_ and on _practicing algorithms_ in ways that encourage fast, but poorly written code in unrealistic scenarios.

AlgoCraft is meant to bridge the gap left by the two: providing an interesting and engaging environment that teaches algorithms through writing real code. 


## design details

The AlgoCraft project is made of four major components: the Project Malmo wrapper library for Python, the browser viewer for the Minecraft instance, the Python Jupyter Notebook IDE, and the cloud deployment application.


Project Malmo has systems in place for generating "worlds" and scenarios in Minecraft. It allows a programmer to specify block placements, mission goals, rewards, and mission termination conditions. Using this setup, I created missions that took advantage of the goal states and rewards system in place to measure progress through the lesson and assign a score when the student completed the lesson. Malmo also provided methods for generating blocks and maps programmatically, allowing for the difficulty of challenges to be dynamically adjusted based on performance of the student.

AlgoCraft provides a starter agent that the student must modify to run against the provided mission. A Jupyter notebook server is launched on start of the docker container, providing access to the Jupyter notebooks that the student can write and test code in.



packaged into a Docker container, and displays graphics using noVNC. It also uses Jupyter notebooks for writing and executing the code that interacts with a Minecraft client. AlgoCraft was initially developed for educating middle school and high school students, for example, participants of the Kentucky Student Technology Leadership Program. 
    



## Cloud architecture 

The AlgoCraft client instance is packaged into a Docker container for easy replication of environment for students. This also allows the build and deployment process to be relatively painless. When a change is made, the image is rebuilt and deployed to Google's Container Registry service. A build trigger then deploys the image to the Kubernetes cluster to be launched when a student starts a mission through the frontend and the score and deployment server creates another deployment. 

This deployment provides a url and password for the noVNC HTML5 client for viewing the Minecraft instance and their agent operate. Also provided are the url and auth token for the jupyter notebook where the student writes their agent code for the provided missions.

Information about the progress of the student and their scores are kept in a Cloud SQL server for monitoring progress of a student over time and for the potential of having a leaderboard for scores across missions.



## future work
- Instead of just wrapping Project Malmo, creating my own offshoot of Project Malmo would allow me to have full control over the features I actually use in AlgoCraft. This would allow me to make data be returned in more common-sense formats and make my scoring system more tightly integrated.

- Create a pip-installable version of the python code I built to interact with the the Project Malmo mod running on Minecraft. This would allow for better modularity and it would allow users to write code on their home computers that interacts with their AlgoCraft agents.

- cre


