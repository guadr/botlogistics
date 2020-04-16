# botlogistics
Repository for various logistics services to run on guadr.gonzaga.edu webserver

## Directory Structure
	overview of files in this repo
		.
		├── planning                # contains all services related to planning
		│   ├── planner.py          # given current order queue and fleet status, plan orders
		│   └── queuer.py           # maintain an order queue
		├── README.md
		├── run.sh                  # scripts to run logistics services
		└── tracking                # contains all services related to tracking
			├── fleet.py            # zmq and server that maintains and updates fleet state
			├── listener.py         # zmq server and client to listen to updater and update fleet, respectively
			├── run_listener.py     # script to test listener
			├── run_updater.py      # script to test updater
			└── updater.py          # updated listens to cars for updates and posts to listener server


