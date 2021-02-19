# LGSVL Simulator and Apollo

## New Simulation Tools for Training and Testing AVs

![](LGSVL_Simulator_Apollo_AVS20.png)

## 0. <a name="introduction">Introduction</a>

_Refer to related video or slides for additional information_

### Intro
Presented by Steve Lemke, Principal Engineer @ LG America R&D Lab

### Outline
0. [Introduction and features of the Simulator](#introduction) (slides 2-13)
1. [Installation of the Simulator](#installation) (slides 14-16)
2. [Getting Started, User Interface, Configuration](#ui) (slides 17-24 and hands-on)
3. [Installing, Building, and Running Apollo](#apollo) (hands-on)
4. [Automation and Python API](#pythonapi) (hands-on)
5. [Advanced Topics](#advanced) (tutorial videos)
6. [Additional Information](#moreinfo) (slide 25)


### Key Features
* Unity 3D engine
	* High Definition Render Pipeline
	* Physics-based modeling of multiple lighting sources
* Out of the box integration with Apollo, Autoware.AI and Autoware.Auto (and other AD stacks)
* ROS, ROS2, CyberRT bridges (and other bridges via customized plugin)
* Physical Sensors: Cameras, LiDAR, Radar, GPS, IMU, etc.
* Virtual Sensors: 2D and 3D Ground Truth, Depth and Segmentation Cameras
* Road/map annotation editor
	* Import of HD maps from: Lanelet2, OpenDRIVE, Apollo
	* Export of HD maps to: Lanelet2, Autoware Vector, OpenDRIVE, Apollo

## 1. <a name="installation">Installation of the Simulator</a>

### Goal: Understand simulator requirements and installation

1. [System Requirements](https://www.lgsvlsimulator.com/docs/getting-started/#getting-started)
	* 4GHz Quad core CPU
	* Nvidia GTX-1080 (8GB memory)
	* Windows 10 64-bit (or Ubuntu ~18.04)

2. [GPU drivers and libraries](https://www.lgsvlsimulator.com/docs/getting-started/#downloading-and-starting-simulator)
	* Install latest Nvidia drivers
	* Install libvulkan (on Linux) 
	* Install nvidia-smi (on Linux)

3. [Downloading and installing](https://www.lgsvlsimulator.com/docs/getting-started/#downloading-and-starting-simulator)
	* Click Download button on [LGSVLSimulator.com](https://lgsvlsimulator.com)
	* Or find release notes at [https://github.com/lgsvl/simulator/releases/latest](https://github.com/lgsvl/simulator/releases/latest)

4. [Building from source](https://www.lgsvlsimulator.com/docs/build-instructions/)
	* Download and install Unity Hub
	* Download and install Unity 2019.3.3f1
	* Download and install Node.js
	* Verify git-lfs installation
	* Clone simulator source from GitHub
	* More on this later in "Advanced Topics"


## 2. <a name="ui">Getting Started</a>

### Goal: Understand simulator user interface for configuring maps, vehicles, and other settings

1. Basic simulator concepts: Refer to [Getting Started doc](https://www.lgsvlsimulator.com/docs/getting-started/#simulator-instructions) or the lecture slides

	1. [Maps](https://www.lgsvlsimulator.com/docs/maps-tab/)
		* There are several pre-loaded reference maps including:
			* BorregasAve
			* AutonomouStuff
			* GoMentum
		* Other maps available at [https://content.lgsvlsimulator.com/](https://content.lgsvlsimulator.com/)

	2. [Vehicles](https://www.lgsvlsimulator.com/docs/vehicles-tab/)
		* There are several pre-loaded reference vehicles including:
			* Jaguar2015XE
			* Lexus2016RXHybrid
				* We could just change bridge type but instead let's create a new vehicle:
		* Navigate to content site: [https://content.lgsvlsimulator.com/](https://content.lgsvlsimulator.com/)
			* Scroll to "Vehicles" and click "View All"
			* Click on [Lexus RX 2016](https://content.lgsvlsimulator.com/vehicles/lexusrx2016/)
			* Right-click to copy `Asset Bundle` link location
			* Close Lexus browser window
			* Return to LGSVL Vehicles web UI
		* Click "Add New" vehicle
			* Enter Vehicle Name: `Lincoln2017MKZ (Apollo master)`
			* Paste copied URL
			* Click "Submit" to save new vehicle
		* Navigate to example [Apollo json config](https://www.lgsvlsimulator.com/docs/apollo5-0-json-example/)
			* Scroll to "Complete JSON Configuration" field
			* Click "Copy" to copy JSON Configuration text
		* Click wrench icon to edit vehicle configuration
			* Select Bridge Type: `CyberRT`
			* Paste copied JSON Configuration text into "Sensors" field
			* Click "Submit" to save vehicle configuration
	3. [Clusters](https://www.lgsvlsimulator.com/docs/clusters-tab/)
		* Local Machine: Default (single machine simulation)
		* Local Cluster: See [Cluster Simulation Introduction](https://www.lgsvlsimulator.com/docs/cluster-simulation-introduction/)
	4. [Simulations](https://www.lgsvlsimulator.com/docs/simulations-tab/)
		* BorregasAve (with Apollo)
			* We could just select our new vehicle but let's create a new simulation:
		* Click "Add New" Simulation
			* General tab:
				* Enter Simulation Name: `AVS Apollo master`
				* Select Cluster: `Local Machine`
				* API Only: leave unchecked
				* Headless Mode: leave unchecked
			* Map & Vehicles tab:
				* Interactive Mode: check this for interactive controls
				* Select Map: `BorregasAve`
				* Select Vehicle: `Lincoln2017MKZ (Apollo master)`
				* Enter "Bridge Connection String": `localhost:9090`
				* We could click "+" to add additional ego vehicles/bridges
			* Traffic tab:
				* Use Predetermined Seed: leave unchecked
				* Random Traffic: check to have NPC vehicles spawn at beginning of simulation
				* Random Pedestrians: check to have pedestrians spawn at beginning of simulation
			* Weather tab:
				* Set time of day during simulation
				* Set rain, wetness, fog, and cloudiness
			* Click "Submit" to save new simulation


2. [How to start simulation](https://www.lgsvlsimulator.com/docs/simulation-menu/)

	* Click in `Lincoln2017MKZ (Apollo master)` to select simulation (indicated by check mark)
	* Click "Play" icon to begin simulation

3. [Controlling the simulator](https://www.lgsvlsimulator.com/docs/simulation-menu/#controls-menu)
1. Start/Pause Simulation (only necessary in Interactive Mode)
		* Click "Play" button
	2. Show Menu Layer
		* Click "Menu" button (if NON-Interactive Mode)
	3. Information
		* Build information, and logged warnings and errors
	4. Controls
		* [Keyboard shortcuts](https://www.lgsvlsimulator.com/docs/keyboard-shortcuts/) 
	5. Bridge Info
		* Bridge address, status, and topic list
	6. Environment (only in Interactive Mode)
		* [Simulation parameters](https://www.lgsvlsimulator.com/docs/simulation-menu/#interactive-menu)
	7. Visualize
		* Color, Depth, Semantic Cameras
		* LiDAR, RADAR
		* 2D and 3D Ground Truth


## 3. <a name="apollo">Installing, Building, and Running Apollo </a>

### Goal: Learn how to use the simulator with Apollo autonomous driving software

1. Setup Apollo
	
	* Should already have installed latest Nvidia drivers (above) before installing Simulator
		
	* Install Docker CE and Nvidia Docker as described in https://www.lgsvlsimulator.com/docs/apollo-master-instructions/
		
	* Clone the Apollo Repository

		```bash
		git clone https://github.com/ApolloAuto/apollo
		```

		* If you have problems with the latest changes in Apollo master, check our online instructions which include a link to the latest commit we've tested with on Apollo master: [https://www.lgsvlsimulator.com/docs/apollo-master-instructions/](https://www.lgsvlsimulator.com/docs/apollo-master-instructions/)
		
		* You could also try checking out a named branch such as `pre6`:

			```bash
			git checkout pre6
			```
   	
		* Alternatively you could try Apollo 5.0 [https://www.lgsvlsimulator.com/docs/apollo5-0-instructions/](https://www.lgsvlsimulator.com/docs/apollo5-0-instructions/)

	* Start and enter Apollo docker
	
		* Start the docker (DO NOT run it with `sudo`!)
		
			```bash
			./docker/scripts/dev_start.sh
			```
		
		* Enter the docker:
			
			```bash
			./docker/scripts/dev_into.sh
			```

		* Make sure `nvidia-smi` is working inside the docker
		
	* Build Apollo (one time operation)

	* Once inside the docker, build Apollo (optimized, not debug, with GPU support):
		
		```bash
		./apollo.sh build_opt_gpu
		```


2. Run Simulator alongside Apollo

  * Launch Cyber bridge

	  	```bash
	  	./scripts/bridge.sh
	  	```
  	
  * Start (resume) the LGSVL Simulator:

  	* Note this is LGSVL Simulator, downloaded from [LGSVLSimulator.com](LGSVLSimulator.com), version 2020.05
  	* Launch the executable and click on the button to open the web UI
  	* Click "Simulations" to view the available/configured simulations
  	* Click in `AVS Apollo master` simulation to select it (indicated by check mark)
  	* Click "Play" icon to begin simulation
  
  * Use `cyber_monitor` to view messages, and use `cyber_visualizer` to visualize them

3. Run Apollo modules

  * Start Dreamview

	    ```bash
	    ./scripts/bootstrap_lgsvl.sh
	    ```

  * Open Dreamview in a browser by navigating to: `localhost:8888`

  * Select correct "setup mode", "vehicle", and "map"

    * For setup mode: select `Mkz Lgsvl`;
    * For vehicle: select `Lincoln2017MKZ LGSVL`;
    * For map: select `Borregas Ave`

  * Open the **Module Controller** tap (on the left bar).

  * Enable **Localization**, **Transform**, **Perception**, **Traffic Light**, **Planning**, **Prediction**, **Routing**, and **Control** modules.

  * Navigate to the **Route Editing** tab.

  * Select a destination by clicking on a lane line and clicking **Submit Route**.


## 4. <a name="pythonapi">Automation and Python API</a>

### Goal: Learn how to control the simulator using the Python API

1. [Controlling environment using Python API](https://www.lgsvlsimulator.com/docs/python-api/)

2. [Quickstart](https://www.lgsvlsimulator.com/docs/python-api/#quickstart)

    * Select pythonapi (virtual environment)

    	* Check out [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
    	* Create virtualenv with: ```mkvirtualenv -p python3 pythonapi```
    	* Activate with: ```workon pythonapi```

    * Download and Install Python API

    	```bash
    	cd ~
    	git clone https://github.com/lgsvl/PythonAPI.git
    	cd PythonAPI
    	pip3 install --user -e .
    	```

    	(Leave out `--user` if working in a python virtual environment)

    * Launch Simulator
    * Review "API Only" Simulation settings
    * Start "API Only" mode simulation

    	* "Open Browser..." changes to "API Ready!"

    * Let's try one of the quickstart scripts to confirm that everything is working:

    	```bash
    	./quickstart/05-ego-drive-in-circle.py
    	```

3. [Core Concepts](https://www.lgsvlsimulator.com/docs/python-api/#core-concepts): Simulator and Agents

  	* Show doc page; intro to Python API concepts

## 5. <a name="advanced">Advanced Topics</a>

### Goal: Build the simulator from source, plus create new environments, vehicles, and sensors

1. Running Simulator with Autoware.Auto and ROS2

   * Refer to [Autoware.Auto with LGSVL Simulator](https://www.lgsvlsimulator.com/docs/autoware-auto-instructions/)
   * Video Tutorial on YouTube (@ 33:40): [Autoware.Auto Course Lecture 11: LGSVL Simulator](https://youtu.be/OcB6FUbjZXo?t=2020)
   * Check out the entire lecture series: [Self-Driving Cars with ROS and Autoware](https://www.apex.ai/autoware-course)


2. Building Simulator from source in Unity

   * Refer to Build Instructions: [(https://www.lgsvlsimulator.com/docs/build-instructions/](https://www.lgsvlsimulator.com/docs/build-instructions/)
   * New Video Tutorial on YouTube: [How to build LGSVL Simulator from source](https://youtu.be/EsCVYI6mhL4)
   * See also Adding and Building Assets: [https://www.lgsvlsimulator.com/docs/assets](https://www.lgsvlsimulator.com/docs/assets/)


3. New environment creation

   * Refer to Adding and Building Assets: [https://www.lgsvlsimulator.com/docs/assets](https://www.lgsvlsimulator.com/docs/assets/)
   * Video Tutorial on YouTube: [How to create environments for LGSVL Simulator](https://youtu.be/S0w2ahhEPbE)


4. New vehicle creation

   * Refer to Adding and Building Assets: [https://www.lgsvlsimulator.com/docs/assets](https://www.lgsvlsimulator.com/docs/assets/)
   * Video Tutorial on YouTube: [How to create a new vehicle asset for LGSVL Simulator](https://youtu.be/R_Z65kimCII)


5. New sensor creation

   * Stay tuned for this (and other) new video tutorials (watch the blog)


6. Map annotation

   * Refer to Map Annotation: [https://www.lgsvlsimulator.com/docs/map-annotation/](https://www.lgsvlsimulator.com/docs/map-annotation/)
   * Stay tuned for this (and other) new video tutorials (watch the blog)


## 6. <a name="moreinfo">Helpful Links</a>

* LGSVL Simulator website: [LGSVLSimulator.com](https://www.lgsvlsimulator.com/)

* LGSVL Simulator blog: [https://www.lgsvlsimulator.com/blog/](https://www.lgsvlsimulator.com/blog/)

* LGSVL Simulator on GitHub: [https://github.com/lgsvl/simulator](https://github.com/lgsvl/simulator)

* LGSVL Simulator on YouTube: [https://www.youtube.com/c/LGSVLSimulator/videos](https://www.youtube.com/c/LGSVLSimulator/videos)

* LGSVL Simulator with latest Apollo: [https://www.lgsvlsimulator.com/docs/apollo-master-instructions/](https://www.lgsvlsimulator.com/docs/apollo-master-instructions/)

* Apollo Autonomous Driving Software: [https://github.com/ApolloAuto/apollo](https://github.com/ApolloAuto/apollo)

* LGSVL Simulator with Autoware.Auto: [https://www.lgsvlsimulator.com/docs/autoware-auto-instructions/](https://www.lgsvlsimulator.com/docs/autoware-auto-instructions/)

* Self-Driving Cars with ROS and Autoware: [https://www.apex.ai/autoware-course](https://www.apex.ai/autoware-course)
